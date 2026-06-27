# Safety Model

## Green Candidates

These are usually safe to clean after explaining that the app may rebuild them:

- package-manager caches
- browser test caches
- temporary logs
- derived build output
- old screenshots or generated previews
- duplicated compressed image exports

## Yellow Candidates

These need user inspection:

- `Downloads`
- `Desktop`
- article material folders
- `node_modules`
- virtualenvs
- Docker volumes
- local videos and recordings
- large app support folders with unclear project ownership

## Red Candidates

Do not recommend deletion:

- `.ssh`, `.gnupg`, keychains, credentials
- databases and wallets
- active source folders
- system folders
- app libraries needed by running apps
- model weights if the user may need offline use

## Cleanup Language

Use concrete, non-alarmist wording:

- "This looks like rebuildable cache."
- "Deleting this may force the tool to download it again."
- "This is probably a project dependency; inspect the project first."
- "I would not delete this from an agent session."
