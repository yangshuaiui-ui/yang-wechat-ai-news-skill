# Iteration Loop

The account's core value is not one good draft. It is a loop that makes the next generated draft closer to the user's own edit.

## Two Required Gates

### Gate 1: Post-Draft Self-Check

Run this after drafting and before HTML:

1. Read the living style ledger when available, especially `claude1.md`.
2. Read hard bans or correction ledgers when available, especially the current workspace rules.
3. Compare the draft against recent user-final deltas.
4. Run quality gates and self-check gates.
5. Fix the draft before moving to HTML.

This gate must be visible in the task checklist for full article work.

### Gate 2: User Feedback And Learning

Run this after the user reviews, edits, screenshots, or rejects the draft:

1. Patch the artifact immediately.
2. Classify each correction:
   - hard ban
   - voice tendency
   - evidence rule
   - title habit
   - structure habit
   - HTML or image workflow rule
3. Update the living ledger when available.
4. Sync Markdown, HTML, and self-check outputs.
5. Treat the new rule as the starting point for the next article.

If the same mistake appears again after it has been recorded, treat it as a serious workflow failure.

## Living Files

When present in the workspace, use these as higher priority than bundled references:

- `CLAUDE.md`: current execution rules, two-stage workflow, hard bans, and delivery path.
- `claude1.md`: positive style ledger extracted from the user's own edits.
- `00-每日循环工作流-SOP.md`: success standards, quality loops, reader six-question final gate.
- `04-去AI味质检-SOP.md`: AI-flavor scan and scoring.
- today's and recent `素材包/*用户终稿.md`: the newest real examples of how the user edits generated text.

## Update Rule

When allowed to edit the living files, add concise rules instead of long explanations:

- bad pattern -> corrected pattern
- why the user changed it
- where it should affect future drafts

When not allowed to edit the living files, output a "style delta note" that the user can inspect.

## Checklist Template

For full article tasks, the working checklist should include:

1. Read current rules, style ledger, and recent user-final draft.
2. Check whether the topic or assets were already used.
3. Gather evidence and map each item to a sentence.
4. Draft with the user's current style.
5. Gate 1: self-check against ledger, AI-flavor, evidence, and reader six questions.
6. Build HTML and verify artifacts.
7. Deliver for user review.
8. Gate 2 after feedback: patch, classify, update ledger, sync artifacts.
