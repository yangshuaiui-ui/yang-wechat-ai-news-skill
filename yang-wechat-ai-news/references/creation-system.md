# Creation System

This file defines the account's reusable creation logic. Treat it as the creator's own process, not a public explanation of implementation sources.

## Core Thesis

The account does not publish AI news as raw updates. It turns fast-moving AI signals into practical judgment for product managers, UX designers, AI builders, and business owners.

The useful article usually answers one question:

`This thing happened. What does it change for people who actually need to use AI in work?`

## Creation Loop

1. Catch the signal.
2. Judge whether it is worth writing.
3. Separate confirmed facts, reported claims, market noise, and personal judgment.
4. Find evidence before writing the final body.
5. Map every key screenshot or recording to a nearby sentence.
6. Write from first-person working judgment.
7. Run the first iteration gate: self-check the draft against hard bans, style ledger, evidence fit, and reader value.
8. Pressure-test title and first screen.
9. Turn the draft into WeChat-copyable HTML.
10. Run the publish gates before handoff.
11. After user edits, compare the generated draft with the user-final draft and update the next-run style rules.

## Article Skeletons

Use one of these shapes when it fits the material:

- `真实现场 -> 反常点 -> 为什么这事重要 -> 对普通人的影响 -> 我的判断 -> 可执行建议`
- `一句话事实 -> 大多数人的误读 -> 真正变化 -> 证据 -> 业务/产品/设计视角 -> 下一步`
- `我看到的信号 -> 我为什么停下来研究 -> 证据链 -> 这不是热闹而是变化 -> 怎么应对`

Do not force every article into a dramatic story. If the user's draft is a practical judgment piece, preserve that structure first.

## Work Modes

- **New article from a topic**: scan or verify the topic, gather evidence, draft, self-check, generate HTML, and wait for user review.
- **User-provided draft**: preserve the user's core structure first; rewrite for voice, evidence, title, and WeChat layout without compressing the content into a thin summary.
- **Generated draft revision**: patch the current draft and sync Markdown, HTML, and self-check outputs.
- **User-final learning**: when the user edits a generated draft into a final version, diff the two versions and turn the user's changes into future style rules.
- **Rejected output recovery**: classify what failed: topic, structure, voice, title, evidence, HTML, or workflow. Fix the artifact and add a reusable rule.

## First-Screen Rule

The first screen must make the reader feel one of these:

- "这事和我有关。"
- "原来不是我以为的那个问题。"
- "我得继续看，不然后面可能会错过判断。"

Use a concrete scene, a sharp fact, or a direct conflict. Avoid policy-summary tone, generic background, and empty industry language.

## Evidence Rule

Evidence is not decoration. Each material must earn its place:

- Screenshot proves a claim.
- Recording proves a workflow or real result.
- Caption explains the key point in Chinese.
- Nearby paragraph tells the reader why this image matters.

If a material only looks impressive but does not support a sentence, remove it.

## Voice Rule

Write like a creator who has actually stopped, looked, compared, and made a judgment.

Prefer:

- "我今天看到这个信号，第一反应不是兴奋，而是..."
- "这件事真正麻烦的地方在于..."
- "如果你只是看发布稿，很容易漏掉..."
- "普通人要看的不是谁最强，而是谁还能稳定用。"

Avoid:

- fake neutrality
- mechanical transitions
- forced jokes
- empty summary paragraphs
- backend/editor language

## Output Rule

A finished task is not finished at Markdown. For WeChat delivery, the expected finish line is:

- final `.md`
- evidence images or recordings
- image-to-sentence mapping
- WeChat-copyable HTML
- title, cover short title, summary
- final self-check
- style-delta note when a user-final draft is available
