#!/usr/bin/env python3
"""Read-only Mac storage scanner for AI-heavy workflows.

The script prints a Markdown report by default and never deletes files.
"""
from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path


COMMON_PATHS = [
    "Downloads",
    "Desktop",
    "Documents",
    "Movies",
    "Pictures",
    ".cache",
    ".codex",
    ".claude",
    ".cursor",
    ".npm",
    ".pnpm-store",
    ".yarn",
    ".cache/pip",
    ".cache/uv",
    ".cache/huggingface",
    ".ollama",
    "Library/Caches",
    "Library/Application Support/Code",
    "Library/Application Support/Cursor",
    "Library/Application Support/Docker",
    "Library/Application Support/Claude",
    "Library/Application Support/Playwright",
]


def du_kib(path: Path) -> int | None:
    if not path.exists():
        return None
    try:
        out = subprocess.check_output(["du", "-sk", str(path)], text=True, stderr=subprocess.DEVNULL)
        return int(out.split()[0])
    except Exception:
        return None


def human(kib: int) -> str:
    size = float(kib) * 1024
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} B"
        size /= 1024
    return f"{size:.1f} TB"


def classify(path: Path) -> tuple[str, str]:
    text = str(path)
    lower = text.lower()
    name = path.name.lower()
    if any(s in lower for s in [".ssh", ".gnupg", "keychain", "wallet", "password", "credentials"]):
        return "red", "credential or sensitive data"
    if any(s in lower for s in ["library/caches", ".cache", ".npm", ".pnpm-store", ".yarn", "playwright"]):
        return "green", "rebuildable cache or generated test data"
    if name in {"node_modules", ".venv", "venv", "dist", "build", ".next"}:
        return "yellow", "project dependency or build output; inspect project first"
    if any(s in lower for s in ["downloads", "desktop", "movies", "pictures", "docker", "huggingface", ".ollama"]):
        return "yellow", "user data, model data, media, or tool storage; inspect before cleanup"
    return "yellow", "large folder; inspect before cleanup"


def collect(home: Path, max_depth: int) -> list[tuple[int, Path, str, str]]:
    candidates: set[Path] = set()
    for rel in COMMON_PATHS:
        candidates.add(home / rel)
    for base in [home, home / "Documents", home / "Desktop"]:
        if base.exists():
            try:
                for child in base.iterdir():
                    if child.is_dir():
                        candidates.add(child)
            except PermissionError:
                pass
    rows: list[tuple[int, Path, str, str]] = []
    for path in sorted(candidates):
        try:
            if not path.exists() or not path.is_dir():
                continue
            if len(path.relative_to(home).parts) > max_depth:
                continue
        except Exception:
            continue
        size = du_kib(path)
        if size is None:
            continue
        risk, reason = classify(path)
        rows.append((size, path, risk, reason))
    rows.sort(reverse=True, key=lambda item: item[0])
    return rows


def markdown(rows: list[tuple[int, Path, str, str]], limit: int) -> str:
    lines = [
        "# Mac Storage Diagnosis",
        "",
        "Read-only report. No files were changed.",
        "",
        "| Risk | Size | Path | Why |",
        "|---|---:|---|---|",
    ]
    icon = {"green": "green", "yellow": "yellow", "red": "red"}
    for size, path, risk, reason in rows[:limit]:
        lines.append(f"| {icon[risk]} | {human(size)} | `{path}` | {reason} |")
    lines.extend(
        [
            "",
            "## Next step",
            "",
            "- Green items are usually cache-like, but still confirm before deleting.",
            "- Yellow items need manual inspection.",
            "- Red items should not be deleted from an agent session.",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--home", default=str(Path.home()))
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--max-depth", type=int, default=3)
    args = parser.parse_args()

    home = Path(args.home).expanduser().resolve()
    rows = collect(home, args.max_depth)
    print(markdown(rows, args.limit))


if __name__ == "__main__":
    main()
