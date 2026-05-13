#!/usr/bin/env python3
"""Send the day's brief TOC to Telegram as HTML, with a link to the full GH Pages summary.

Why this exists: Telegram's chat messages cap at 4096 characters and don't render
GitHub-flavored Markdown well (no headers, no `**bold**` — only legacy V1's `*bold*`,
parse failures on unescaped chars in URLs/hashtags fall back to plain text). So
we ship a short, HTML-formatted TOC to Telegram and keep the full enriched brief
on the deployed GH Pages site, linked from the message.

Run after Horizon finishes (`uv run horizon ...`), before the Pages deploy step.

Env:
- TELEGRAM_WEBHOOK_URL_HORIZON  full sendMessage URL with bot token baked in
- TELEGRAM_CHAT_ID_HORIZON      target channel chat ID
- PAGES_BASE                    e.g. "https://gg-dodcom.github.io/Horizon"
- TG_LANG (optional)            which language brief to ship; default "zh"
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "docs" / "_posts"

TG_URL     = os.environ["TELEGRAM_WEBHOOK_URL_HORIZON"]
TG_CHAT    = os.environ["TELEGRAM_CHAT_ID_HORIZON"]
PAGES_BASE = os.environ.get("PAGES_BASE", "https://gg-dodcom.github.io/Horizon").rstrip("/")
LANG       = os.environ.get("TG_LANG", "zh")

# Telegram chat message hard cap.
TG_LIMIT = 4096


def latest_summary() -> Path:
    pattern = f"*-summary-{LANG}.md"
    files = sorted(POSTS.glob(pattern))
    if not files:
        sys.exit(f"::error::no {pattern} files in {POSTS}")
    return files[-1]


def extract_toc(md: str) -> list[tuple[int, str, int, float]]:
    """Pull the numbered TOC at the head of the brief.

    Horizon's TOC line shape (Markdown):
        1. [Title](#item-1) ⭐️ 9.0/10

    Returns a list of (rank, title, anchor_id, score).
    Stops at the first '---' divider that comes after at least one TOC item.
    """
    body = md
    if body.startswith("---"):
        end = body.find("\n---\n", 4)
        if end != -1:
            body = body[end + 5:]
    body = body.lstrip()

    items: list[tuple[int, str, int, float]] = []
    item_re = re.compile(
        r"^\s*(\d+)\.\s+\[(.+?)\]\(#item-(\d+)\)\s+[⭐⭐️]+\s*(\d+(?:\.\d+)?)\s*/\s*10\s*$"
    )
    for raw in body.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        if line.strip() == "---" and items:
            break
        m = item_re.match(line)
        if m:
            items.append(
                (int(m.group(1)), m.group(2).strip(), int(m.group(3)), float(m.group(4)))
            )
    return items


def jekyll_url(summary_path: Path) -> str:
    """Build the Jekyll default-permalink URL for this summary file."""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)$", summary_path.stem)
    if not m:
        return PAGES_BASE + "/"
    y, mo, d, slug = m.groups()
    return f"{PAGES_BASE}/{y}/{mo}/{d}/{slug}.html"


def file_date(summary_path: Path) -> str:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", summary_path.stem)
    return m.group(1) if m else datetime.now(timezone.utc).strftime("%Y-%m-%d")


def build_message(items: list[tuple[int, str, int, float]], page_url: str, date_str: str) -> str:
    """Compose the HTML message; each title becomes a tappable deep-link.

    If the assembled message exceeds Telegram's 4096-char cap, tail items
    are dropped and replaced with a "… (N more, see Pages)" line. The footer
    "完整 brief" link is always preserved so the user can still reach Pages.
    """
    header = f"<b>📡 M&#39;s Tech Brief — {date_str}</b>"
    footer = f'→ <a href="{escape(page_url, quote=True)}">完整 brief（含背景、社区讨论、参考链接）</a>'

    rendered: list[str] = []
    for rank, title, anchor_id, score in items:
        item_url = f"{page_url}#item-{anchor_id}"
        rendered.append(
            f'{rank}. <a href="{escape(item_url, quote=True)}">{escape(title)}</a>  ⭐️ <b>{score:.1f}</b>'
        )

    def assemble(items_subset: list[str], more_note: str = "") -> str:
        # Items separated by a blank line (\n\n) for breathing room — Chinese
        # titles wrap on phone widths, so a stacked dense list was hard to read.
        body = "\n\n".join(items_subset)
        sections = [header, body]
        if more_note:
            sections.append(more_note)
        sections.append(footer)
        return "\n\n".join(sections)

    msg = assemble(rendered)
    if len(msg) <= TG_LIMIT:
        return msg

    truncated = rendered.copy()
    while truncated:
        truncated.pop()
        more = len(rendered) - len(truncated)
        candidate = assemble(truncated, f"… (剩余 {more} 条,点下方链接看完整列表)")
        if len(candidate) <= TG_LIMIT:
            return candidate
    return f"{header}\n\n(could not parse TOC)\n\n{footer}"


def send(text: str) -> None:
    payload = json.dumps(
        {
            "chat_id": TG_CHAT,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": False,  # preview the Pages link
        },
        ensure_ascii=False,
    ).encode("utf-8")
    req = Request(TG_URL, data=payload, headers={"Content-Type": "application/json"})
    with urlopen(req, timeout=20) as r:
        status = r.status
        body = r.read().decode("utf-8", "replace")
    if status != 200:
        sys.exit(f"::error::Telegram sendMessage HTTP {status}: {body[:500]}")
    print(f"sent {len(text)} chars; HTTP {status}")


def main() -> int:
    path = latest_summary()
    print(f"reading {path.relative_to(ROOT)}")
    items = extract_toc(path.read_text(encoding="utf-8"))
    print(f"parsed {len(items)} TOC items")
    msg = build_message(items, jekyll_url(path), file_date(path))
    print(f"message length: {len(msg)}/{TG_LIMIT}")
    send(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
