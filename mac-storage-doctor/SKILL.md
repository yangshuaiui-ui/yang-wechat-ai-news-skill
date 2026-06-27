---
name: mac-storage-doctor
description: "Safety-first Mac storage diagnosis for AI-heavy workflows. Use when the user asks why a Mac disk is full, wants to clean Mac storage, inspect AI tool caches, classify large folders, or decide what can be deleted safely. Focus on Codex, Claude Code, Cursor, Docker, Node, Playwright, browser caches, model caches, recordings, downloads, and project dependencies. Default to read-only scanning, risk classification, and user-confirmed cleanup advice; never delete automatically."
---

# Mac Storage Doctor

This Skill helps diagnose Mac storage pressure for AI-heavy users. It is not an auto-delete cleaner. Treat storage cleanup as a risk decision: explain what each large folder probably is, what deleting it may break, and what the safest next action is.

## Core Rule

Default to read-only. Do not delete, move, or rewrite files unless the user explicitly asks after seeing the diagnosis.

## Workflow

1. Clarify the target only if needed: whole Home directory, AI tool caches, downloads, project folders, or a specific path.
2. Run `scripts/scan_storage.py` for a first pass when local shell access is available.
3. Inspect the report and classify candidates into green, yellow, and red groups.
4. Explain large items in ordinary language: what it is, why it grew, what happens if it is removed.
5. Give cleanup suggestions as commands or Finder actions, but keep destructive commands separate and require user confirmation before execution.

## Risk Classes

- **Green**: cache, temporary build output, generated browser data, logs, or files that the tool can recreate.
- **Yellow**: downloads, recordings, project dependencies, offline media, local datasets, and old material folders. User should inspect before removing.
- **Red**: system files, keychains, credentials, active project source, databases, app libraries with unclear ownership, and anything under sensitive paths. Explain only; do not propose deletion.

## AI Workflow Hotspots

Check these categories first:

- Codex, Claude Code, Cursor, Windsurf, and other agent workspaces.
- Docker images, containers, volumes, and build cache.
- Node `node_modules`, package-manager caches, and monorepo build outputs.
- Python virtualenvs, pip cache, uv cache, Conda environments.
- Playwright, browser profiles, screenshots, recordings, and test artifacts.
- Hugging Face, Ollama, LM Studio, local model weights, embeddings, and datasets.
- WeChat/article material folders with duplicated source images, web-compressed copies, and exported HTML.

## Output Shape

For diagnosis tasks, output:

1. Total scope scanned.
2. Top large items table.
3. Green / yellow / red recommendations.
4. What to inspect manually.
5. Exact commands only for safe read-only checks by default.
6. If cleanup is requested, list destructive actions separately and ask for confirmation.

## Non-Negotiables

- Never hide risk behind "safe to delete" language. Say what may need to be redownloaded, rebuilt, or reconfigured.
- Never delete credentials, source code, databases, app libraries, or unknown folders.
- Never use `rm -rf` without an explicit user approval after a concrete path list is shown.
- Prefer moving user-owned yellow items to Trash over permanent deletion.
- If the report is uncertain, classify as yellow or red, not green.
