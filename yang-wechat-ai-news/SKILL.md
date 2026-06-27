---
name: yang-wechat-ai-news
description: "Yang Shuai's self-iterating WeChat Official Account AI-news production system. Use when the user asks to search AI hot topics, judge or write公众号/微信公众号 articles, rewrite in the user's voice, compare generated drafts with user-edited final drafts, update style ledgers, run self-check gates, collect evidence screenshots/videos, map images to copy, output WeChat-copyable HTML, or run the full loop from topic scan to evidence to draft to user-style iteration to final delivery. Trigger on 公众号, 微信公众号, AI 快讯, 搜国内线, 搜国外线, 配图, 截图强关联, 生成 HTML, 一键复制, 自检, 迭代, 用户终稿, 对比我的修改, 按我的 skill 组写, or 用我的循环工作流."
---

# Yang WeChat AI News

This is the user's personal 公众号 AI 快讯 workflow. It preserves the user's own `.md` logic, article judgment, evidence discipline, self-check gates, and living style iteration loop. The Skill packages the user's daily creation process into a reusable system: topic judgment, evidence mapping, article drafting, title pressure, draft-vs-user-final comparison, style-ledger updates, WeChat layout, and final HTML delivery.

## Priority Order

1. User's current instruction in chat.
2. Runtime workspace rules when present: `CLAUDE.md`, `claude1.md`, `00-每日循环工作流-SOP.md`, `00-用户画像-内容底层逻辑.md`, `01-*SOP.md`, `02-配图排版与HTML输出-SOP.md`, `03-排版规则-微信公众号.md`, `04-去AI味质检-SOP.md`.
3. This Skill's references.
4. General model judgment.

If runtime rules and bundled references disagree, use the runtime rules and say so only when it affects delivery.

## Workflow Decision

- **Hot-topic scan only**: read `references/hotspot-scan.md`; output the requested domestic or overseas watchboard; stop for user selection.
- **Full article after topic is chosen**: read all required references below, create an explicit task checklist, include the two iteration gates, and execute end to end without asking mid-way unless blocked.
- **Title only**: read `references/account-voice.md` and `references/quality-gates.md`; return tight title options and update the current HTML title if a file is open or identified.
- **Evidence or HTML only**: read `references/evidence-html.md`; keep text unchanged except for replacing marked image positions with strong evidence.
- **Revision after user feedback**: read `references/iteration-loop.md`, `references/draft-diff-style-learning.md`, `references/quality-gates.md`, and `references/account-voice.md`; patch the artifact, classify the correction, and update any living ledger when present.
- **Style learning or user-final comparison**: read `references/draft-diff-style-learning.md`; compare generated draft, user-edited final draft, and the next target draft; output reusable style deltas before rewriting.

## Full Article Flow

1. Load runtime rules if present, especially `CLAUDE.md`, `claude1.md`, and the latest user-final draft in the current material folders.
2. Load `references/workflow.md`, `references/creation-system.md`, `references/account-voice.md`, `references/iteration-loop.md`, `references/draft-diff-style-learning.md`, and `references/self-check-system.md`.
3. Before drafting, compare the current target with recent generated-vs-user-final deltas when available. Treat the user's last edits as today's starting line.
4. For timely AI facts, verify current facts with primary or credible sources before writing.
5. Build an evidence pack before final prose. Every screenshot or recording must map to a sentence.
6. Draft in the user's voice and structure. Preserve user-provided core material before polishing.
7. Run **Iteration Gate 1**: compare draft against the style ledger, hard bans, self-check gates, and recent user edits. Fix before HTML.
8. Generate title, cover short title, and摘要 only after the body angle is clear.
9. Use `references/evidence-html.md` for image naming, screenshot standards, and WeChat HTML.
10. Run `references/self-check-system.md` and `references/quality-gates.md` before handoff.
11. Deliver durable artifacts: `.md`, image folder, final `.html`, and self-check note.
12. When the user edits or rejects the result, run **Iteration Gate 2**: patch immediately, classify every change, update the living style ledger when available, and make the next draft start from the new rule.

## Required References

- `references/workflow.md`: full production loop, artifact expectations, and iteration protocol.
- `references/account-voice.md`: the user's voice, title style, and living style ledger.
- `references/evidence-html.md`: evidence-image rules, screenshot rules, and WeChat-copyable HTML rules.
- `references/quality-gates.md`: publish gates for voice, evidence, reader retention, and WeChat delivery.
- `references/hotspot-scan.md`: domestic and overseas topic scanning rules.
- `references/creation-system.md`: the account's reusable creation logic, from raw signal to publishable article.
- `references/self-check-system.md`: three success standards, AI-flavor scoring, reader six-question final gate, and HTML checks.
- `references/iteration-loop.md`: two iteration gates, correction classification, ledger updates, and "same mistake never twice" rule.
- `references/draft-diff-style-learning.md`: generated draft vs user-final comparison method and reusable style-delta extraction.

## Script

Use `scripts/render_wechat_html.py` when converting a prepared markdown draft plus an image manifest into a one-click-copy local HTML page. The script is a utility, not a writing engine; it does not decide facts or rewrite the user's voice.

## Non-Negotiables

- Do not mix old article assets into a new article. Check today's and recent material folders before using any image.
- Do not claim a screenshot proves something it does not prove. Change the caption or find a better source.
- Do not let backend/editor language reach the final article.
- Do not use green or colorful emphasis unless the user explicitly reverses the black-white-gray rule.
- Do not stop at markdown when the user asked for WeChat delivery. Produce the HTML artifact and verify it.
- Do not skip the living iteration loop. If the user provides a final edited draft, compare it against the generated draft and convert the differences into future writing rules.
- Do not repeat a user-rejected phrase, structure, title habit, evidence habit, or HTML mistake after it has been recorded once.
