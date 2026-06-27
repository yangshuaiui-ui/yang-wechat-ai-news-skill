# Hotspot Scan

## Boundary

When the user asks to scan topics, scan only the requested line:

- 国内线: Chinese AI companies, official accounts, ModelScope/Hugging Face pages, Chinese media and domestic conferences.
- 国外线: OpenAI, Anthropic, Google, xAI, Meta, Mistral, official X/blog/docs/changelog/status, AI media, and overseas conferences.

Do not mix lines unless the user asks for both.

## Freshness

Default fast-news window is 4 hours for hard news. Exceptions:

- Ongoing conferences or live events.
- Evergreen high-frequency user pain points with verified solutions.
- Retrospective analysis where the value is a new judgment, not first speed.

## Watchboard Output

For scan-only tasks, output:

- S/A/B/C topic table.
- Earliest seen time, time since first seen, and source.
- Why the topic matters to this account.
- Evidence state.
- Top competitors already covered or not.
- Main recommendation and two backups.
- Known gaps or inaccessible sources.

Stop after the watchboard and let the user choose.

## Writeability Test

Recommend a topic only if at least two are true:

- Hot enough to click.
- Painful or useful to the account's readers.
- Has evidence that can be shown.
- Has a concrete user action.
- Has a clear domestic-vs-overseas or open-vs-closed contrast.

Do not force a weak topic because it is new.
