# Evidence And HTML

## Evidence Mapping

Every image or recording must answer:

1. Which exact sentence does it prove?
2. Is the source correct and current?
3. Would deleting it weaken reader trust or comprehension?

If the answer is weak, remove it or find a better source.

## Image Standards

- Use one image for one conclusion.
- Crop to a complete, readable module.
- Center the subject with balanced margins.
- Remove sidebars, ads, popups, floating bars, half-cut elements, unrelated feeds, and login banners.
- For English screenshots, provide a Chinese caption that explains the key point.
- Caption format: `↑ <what this proves>（来源 <source>，<date>）`.
- Never use old assets for a new article unless the user explicitly says to reuse them.

## Source Priority

1. Official blog, official X, official docs, official changelog.
2. Model page, benchmark page, GitHub repo, system card.
3. Credible media or expert quote.
4. Social screenshots only when they are the event itself or the best available source.

If a screenshot proves less than the draft claims, either change the claim or change the caption. Do not pretend.

## Video Standards

Use real recordings, official clips, or real demos only. No AI-generated fake evidence. If video is used, it should be the first-screen hook only when it directly proves the opening claim.

## HTML Style

- Use inline styles.
- Keep article body free of `<script>`, `<style>`, `<iframe>`, and fixed/sticky positioning. Preview pages can contain scripts.
- Body typography: 16px, line-height about 1.8, black-white-gray.
- No green or colorful emphasis by default.
- Emphasis uses black bold only.
- Use natural paragraphs as the base. Use blocks sparingly for quotes, evidence, or key judgments.
- Keep `h1` out of the copy body; WeChat backend title is separate.

## Copy Flow

Preferred current flow:

1. Put final files in `素材包/YYYY-MM-DD-主题/`.
2. Compress images for web copy when remote links are slow.
3. Use a one-click-copy local HTML preview.
4. Verify image count, copy button, JS syntax, old asset leakage, and link reachability.
5. Keep local images as manual drag-in fallback.

Use `scripts/render_wechat_html.py` for simple markdown-to-HTML conversion with image manifest.
