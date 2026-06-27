# Workflow

## Core Position

The account is an AI fast-news and judgment account. It wins by speed, useful pain-point interpretation, hard evidence, and a recognizably human voice. The north star is not "complete information"; it is whether a Chinese mobile WeChat reader clicks, reads, trusts, shares, and remembers one judgment.

## Two-Stage Rule

1. **Scan stage**: when the user asks to search topics, output only a watchboard and stop. Do not choose the final topic without the user.
2. **Writing stage**: once the user chooses or provides the article topic/material, run the whole chain to delivery: facts -> evidence -> draft -> title -> layout -> quality check -> HTML.

## Full Chain

1. Read runtime rules if they exist in cwd.
2. Check current and recent material folders to avoid duplicate work or old image leakage.
3. Decide article type: hot news, deep judgment, comparison, tutorial, product experience, or warning.
4. Establish one core sentence. Every section must serve this sentence.
5. Gather evidence first. Prefer real recordings when they prove a user-visible action; use screenshots for fixed facts, official statements, data tables, or quotes.
6. Write around the user's own structure when the user provides a draft. Do not compress the user's core sections into a thin summary.
7. Keep body length appropriate:
   - Hot-news article: usually 2500-3000 Chinese characters, max about 3000 unless user asks long-form.
   - Deep essay or story-heavy analysis: can expand when story, evidence, and emotional arc justify it.
8. Generate title after the article angle is stable.
9. Build HTML only after image positions and captions are settled.
10. Verify and hand off paths.

## Iteration Protocol

The user values iterative memory. When the user corrects style, logic, title, evidence, or HTML:

1. Patch the current artifact immediately.
2. Identify whether the correction is a hard ban, a voice tendency, an evidence rule, or a workflow rule.
3. If the current workspace has a living ledger such as `claude1.md` or `CLAUDE.md`, treat it as the source of truth for future turns.
4. Do not repeat the same rejected pattern.

## Delivery Artifacts

For publishable work, create a dated material folder containing:

- Final markdown draft.
- Final image/video files, named in article order.
- Build script if one was used.
- Final one-click-copy HTML.
- Optional self-check note when the article is complex.

## Handoff Standard

Final handoff must include exact file paths, what was verified, and any remaining manual step. If images use remote links, keep local image files as a fallback.
