# Quality Gates

This account uses layered publish gates: hard wording scan, living style scan, evidence scan, reader-action scan, and iteration scan. The goal is to keep the article like the user's own judgment, not a generated report.

## L1 Hard Scan

Fail and fix before delivery if any appear:

- "说人话" or "说人话就是"
- "收藏点"
- "首先 / 其次 / 最后" as mechanical structure
- "值得注意的是 / 综上所述 / 在当今时代 / 随着技术发展"
- Big claims without source
- Old article image paths in a new article
- Green or colorful emphasis in WeChat HTML
- Copy HTML with multiple confusing copy paths unless the workspace explicitly requires it
- A known rejected phrase from the living ledger or current user feedback

## L2 Voice Scan

Pass only if:

- It sounds like a real person with AI/product/business judgment.
- The article uses the user's first-person or shared "我们" voice when appropriate.
- It avoids generic AI-report tone.
- The title reads like a user-facing hook, not an internal angle note.
- The opening gives a concrete scene, fact, or conflict within the first few lines.
- It reflects the latest user-final draft deltas when available.

## L3 Content And Evidence Scan

Pass only if:

- The article has one core judgment.
- Facts, speculation, and opinion are separated.
- Each important claim has evidence or a clear boundary.
- The target reader's pain is concrete.
- Anxiety has an exit.
- Images or videos are strongly mapped to nearby copy.

## L4 Reader Action Scan

Read as a busy mobile WeChat user and answer:

1. Would I click this title?
2. Would the first screen keep me?
3. Did I learn a useful judgment, not only news?
4. Do I trust the evidence?
5. Would I share, save, or quote one sentence?
6. Do I know what to do next?

If any answer is no, revise the title, first screen, evidence, or ending before publishing.

## L5 Iteration Scan

Pass only if:

- The current draft has been checked against the latest living ledger when available.
- Recent user corrections have been applied proactively, not only after the user repeats them.
- Generated draft, final HTML, and self-check note are in sync.
- If the user provided a final edited draft, the reusable deltas were extracted for next time.

## HTML Checks

Before final response, verify:

- Final HTML exists.
- Image count matches planned evidence count.
- No old material folder references.
- No forbidden copy labels such as stale "普通复制 / 备用复制" unless deliberately used.
- JS syntax passes when the preview page uses JS.
- Remote image links return 200 when used.
- Local image fallback exists.
