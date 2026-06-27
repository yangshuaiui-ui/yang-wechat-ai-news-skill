# Draft Diff Style Learning

Use this when there is a generated draft and a user-edited final draft, or when the user asks why the output still does not sound like them.

## Inputs

Look for:

- generated draft path
- user-final draft path
- current target draft
- screenshots or comments from the user
- living style ledger such as `claude1.md`

If exact matching files are unavailable, compare the closest generated draft and user-final draft from the recent material folders and say which files were used.

## Comparison Method

Compare at four levels:

1. **Words and phrases**: what the user replaced, softened, banned, or repeated.
2. **Sentence shape**: whether the user shortened, expanded, merged, broke, or reordered sentences.
3. **Judgment stance**: where the user made the claim more precise, more grounded, less self-important, or more direct.
4. **Ending and structure**: where the user added emotional complexity, concrete lists, exit paths, or stronger final rhythm.

Do not only list differences. Convert each difference into a future-generation rule.

## Output Shape

Use this compact format:

| Area | Generated Habit | User Final Habit | Future Rule |
|---|---|---|---|
| wording | ... | ... | ... |
| structure | ... | ... | ... |
| evidence | ... | ... | ... |
| ending | ... | ... | ... |

Then provide:

- updated hard bans
- updated positive style tendencies
- one paragraph rewriting instruction for the next draft

## Current Known Style Deltas

- Prefer "我们 / 咱们" when talking about shared fate or action.
- Prefer "说得再直接一点" over "说人话" or "翻译成人话".
- Prefer precise labels such as "订阅制往准入制靠" over clever but vague labels.
- Expand endings: emotional complexity -> cold reality -> optimistic exit -> concrete action.
- Use "大佬" directly; avoid clever detours.
- Add evidence captions in the form `↑ what this proves（source, date）`.
- Do not flatten the user's structure into a generic summary.
- Do not force jokes or catchphrases when they change the original meaning.

## Applying The Deltas

Before writing a new article:

1. Pick the latest 3-7 style deltas.
2. Turn them into a short drafting constraint list.
3. Draft.
4. During Gate 1, check whether each delta appeared in the new draft.
5. If not, revise before delivery.
