#!/usr/bin/env python3
"""Render a WeChat-copyable HTML preview from markdown and an image manifest.

Usage:
  python render_wechat_html.py draft.md manifest.json out.html --title "标题"

Manifest format:
[
  {"src": "https://example.com/a.jpg", "caption": "↑ 图注（来源，日期）"},
  {"src": "local.png", "caption": "↑ 图注（来源，日期）"}
]

Markdown lines beginning with ↑ are replaced by the next image in the manifest.
This script intentionally does not rewrite article content.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


def para(text: str) -> str:
    return f'<p style="margin:1em 0;">{html.escape(text)}</p>'


def quote(text: str) -> str:
    return (
        '<section style="margin:1em 0;padding:12px 14px;background:#f7f7f7;'
        'border-left:3px solid #ddd;color:#666;font-size:15px;">'
        f"{html.escape(text)}</section>"
    )


def image_block(src: str, caption: str) -> str:
    return (
        '<figure style="margin:1em 0;text-align:center;">'
        f'<img src="{html.escape(src, quote=True)}" style="width:100%;border-radius:4px;" alt="证据截图"/>'
        f'<figcaption style="margin:.3em 0;font-size:13px;color:#999;">{html.escape(caption)}</figcaption>'
        "</figure>"
    )


def render_article(markdown: str, images: list[dict[str, str]]) -> str:
    blocks: list[str] = []
    image_index = 0
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.startswith(">"):
            blocks.append(quote(line.lstrip("> ").strip()))
            continue
        if line.startswith("↑"):
            if image_index >= len(images):
                raise SystemExit(f"not enough manifest images for line: {line}")
            item = images[image_index]
            blocks.append(image_block(item["src"], item["caption"]))
            image_index += 1
            continue
        blocks.append(para(line))
    if image_index != len(images):
        raise SystemExit(f"manifest has unused images: used {image_index}, total {len(images)}")
    return "".join(blocks)


def render_page(title: str, article_html: str, image_count: int) -> str:
    safe_title = html.escape(title)
    copy_text = f"一键复制图文（正文 + {image_count} 张证据图）→ 去微信粘贴"
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>公众号成稿 · {safe_title}</title>
<style>
body{{margin:0;background:#ececec;font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC",sans-serif;}}
#copybar{{position:fixed;top:0;left:0;right:0;z-index:9999;background:#222;color:#fff;text-align:center;padding:14px;font-size:17px;font-weight:700;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.15);}}
.howto{{max-width:620px;margin:64px auto 0;padding:14px 18px;background:#fff7e6;border:1px solid #ffe1a8;border-radius:10px;color:#7a5b00;font-size:13px;line-height:1.8;}}
.titles{{max-width:620px;margin:12px auto 0;padding:14px 18px;background:#fff;border-radius:10px;font-size:13px;line-height:1.8;color:#444;}}
.phone{{max-width:420px;margin:18px auto 50px;background:#fff;border-radius:14px;box-shadow:0 6px 24px rgba(0,0,0,.08);overflow:hidden;}}
.copyzone{{padding:8px 14px 22px;}}
img{{max-width:100%;}}
</style></head>
<body>
<div id="copybar" onclick="copyAll()">{copy_text}</div>
<div class="howto">用 Chrome 打开本文件，点顶部黑条复制，然后到微信公众号编辑器粘贴。若远程图未进入微信，使用本地图片兜底拖入对应图注位置。</div>
<div class="titles"><b>标题：</b>{safe_title}</div>
<div class="phone"><div class="copyzone">
<section id="article" style="font-size:16px;line-height:1.8;color:#3f3f3f;letter-spacing:0.3px;padding:0 4px;">
{article_html}
</section>
</div></div>
<script>
function copyAll(){{
  var bar=document.getElementById('copybar');
  var art=document.getElementById('article').cloneNode(true);
  try{{
    navigator.clipboard.write([new ClipboardItem({{
      'text/html':new Blob([art.outerHTML],{{type:'text/html'}}),
      'text/plain':new Blob([art.innerText],{{type:'text/plain'}})
    }})]);
    bar.textContent='图文已复制，去公众号编辑器粘贴';
    bar.style.background='#444';
    setTimeout(function(){{bar.textContent='{copy_text}';bar.style.background='#222';}},4500);
  }}catch(e){{
    bar.textContent='复制失败，请用 Chrome 打开本文件再点';
    bar.style.background='#c0392b';
  }}
}}
</script>
</body></html>'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("draft")
    parser.add_argument("manifest")
    parser.add_argument("out")
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    draft = Path(args.draft).read_text(encoding="utf-8")
    images = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    article = render_article(draft, images)
    page = render_page(args.title, article, len(images))
    Path(args.out).write_text(page, encoding="utf-8")
    print(f"OK {args.out} {len(images)} images")


if __name__ == "__main__":
    main()
