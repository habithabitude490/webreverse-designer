#!/usr/bin/env python3
"""WebReverse Designer — optional static inventory.

Walk a local folder and inventory HTML / CSS / JS files
without ever executing them. Step 0 of the skill.

Usage:
    python3 scripts/check_project.py /path/to/project [--json]

- Standard library only. Reads only the head of each
  file (default: 256 KB). Tolerates missing folders, unreadable
  files, imperfect encodings.
- Excludes: .git, node_modules, dist, build, venvs, etc.
- Exit codes: 0 = OK (even empty project), 1 = usage/path, 2 = unexpected.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass, field

VERSION = "1.2.0"

DEFAULT_EXCLUDE_DIRS = {
    ".git", "node_modules", "dist", "build", ".venv", "venv",
    "__pycache__", ".tox", ".mypy_cache", ".pytest_cache",
}

RE_LINK_CSS = re.compile(r'<link[^>]+href=["\']([^"\']+)["\']', re.IGNORECASE)
RE_SCRIPT_SRC = re.compile(r'<script[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
RE_CSS_IMPORT = re.compile(r'@import\s+(?:url\()?["\']?([^"\')\s;]+)', re.IGNORECASE)
RE_JS_IMPORT = re.compile(
    r'(?:import\s+(?:[^;]*?\sfrom\s+)?["\']([^"\']+)["\']'
    r'|require\(\s*["\']([^"\']+)["\']\s*\))'
)
RE_CLASS = re.compile(r'class=["\']([^"\']+)["\']')
RE_ID = re.compile(r'id=["\']([^"\']+)["\']')


@dataclass
class FileEntry:
    path: str
    kind: str  # html | css | js | other
    size_bytes: int
    lines: int | None
    truncated: bool
    encoding_issue: bool
    refs: list = field(default_factory=list)
    classes: list = field(default_factory=list)
    ids: list = field(default_factory=list)
    error: str | None = None


@dataclass
class Inventory:
    root: str
    files: list = field(default_factory=list)
    skipped_dirs: list = field(default_factory=list)
    unreadable: list = field(default_factory=list)
    entry_points: list = field(default_factory=list)
    warnings: list = field(default_factory=list)

    @property
    def counts(self):
        counts = {"html": 0, "css": 0, "js": 0, "other": 0}
        for f in self.files:
            counts[f.kind] = counts.get(f.kind, 0) + 1
        counts["total"] = len(self.files)
        return counts


def kind_of(filename: str) -> str:
    name = filename.lower()
    if name.endswith((".html", ".htm")):
        return "html"
    if name.endswith(".css"):
        return "css"
    if name.endswith((".js", ".mjs", ".cjs")):
        return "js"
    return "other"


def read_head(path: str, max_bytes: int):
    """Read the head of a file in tolerant mode. Never executes."""
    with open(path, "rb") as fh:
        raw = fh.read(max_bytes + 1)
    truncated = len(raw) > max_bytes
    raw = raw[:max_bytes]
    try:
        return raw.decode("utf-8"), truncated, False
    except UnicodeDecodeError:
        return raw.decode("utf-8", errors="replace"), truncated, True
def extract_signals(kind, text):
    """Declarative signals extracted from text content (never executed).

    Input: kind (html|css|js|other), text (decoded file head).
    Output: (refs, classes, ids) — deduplicated lists, 50 max each.
    - html: href of <link>, src of <script>, class/id attributes.
    - css: @import + .class heuristic (simple selectors).
    - js: import/require targets (declarative, unresolved).
    Agent usage: interpret only as hints; cite file:line
    in the report, never as proof of execution.
    """
    refs = []
    if kind == "html":
        refs += RE_LINK_CSS.findall(text)
        refs += RE_SCRIPT_SRC.findall(text)
    elif kind == "css":
        refs += RE_CSS_IMPORT.findall(text)
    elif kind == "js":
        for a, b in RE_JS_IMPORT.findall(text):
            refs.append(a or b)
    classes, ids = [], []
    if kind == "html":
        for m in RE_CLASS.findall(text):
            classes.extend(m.split())
        ids.extend(RE_ID.findall(text))
    elif kind == "css":
        classes.extend(re.findall(r"\.([A-Za-z_][\w-]*)", text))
    refs = list(dict.fromkeys(r for r in refs if r.strip()))[:50]
    classes = list(dict.fromkeys(c for c in classes if c.strip()))[:50]
    ids = list(dict.fromkeys(i for i in ids if i.strip()))[:50]
    return refs, classes, ids


def scan_file(full_path, rel_path, max_bytes):
    """Inventory a single file. Never raises for unreadable content.

    Agent usage: call via scan_project, not directly.
    'other' entries (e.g. .txt) are neither read nor parsed: size only.
    The 'error' field signals a problem; 'encoding_issue' = imperfect UTF-8.
    """
    kind = kind_of(full_path)
    try:
        size = os.path.getsize(full_path)
    except OSError as exc:
        return FileEntry(rel_path, kind, -1, None, False, False, error=str(exc))
    if kind == "other":
        return FileEntry(rel_path, kind, size, None, False, False)
    try:
        text, truncated, enc = read_head(full_path, max_bytes)
    except OSError as exc:
        return FileEntry(rel_path, kind, size, None, False, False,
                         error="unreadable: %s" % exc)
    refs, classes, ids = extract_signals(kind, text)
    lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
    return FileEntry(rel_path, kind, size, lines, truncated, enc,
                     refs, classes, ids)

def scan_project(root, max_bytes, exclude=None):
    """Inventory a project folder. Recommended agent entry point.

    Example: scan_project("./my-site", 262144) then to_text() or to_dict().
    Does not follow symlinks, does not descend into exclude
    (default: .git, node_modules, dist, build, venvs, caches).
    Always returns an Inventory (never raises for a missing
    folder: see 'warnings'). Empty project = exit 0 + warning, not an error.
    """
    exclude = set(exclude or DEFAULT_EXCLUDE_DIRS)
    inv = Inventory(root=os.path.abspath(root))
    if not os.path.exists(root):
        inv.warnings.append("Folder not found: %s" % root)
        return inv
    if not os.path.isdir(root):
        inv.warnings.append("Not-a-folder path: %s" % root)
        return inv
    skipped = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        for d in [x for x in dirnames if x in exclude]:
            skipped.append(os.path.relpath(os.path.join(dirpath, d), root))
        dirnames[:] = [d for d in dirnames if d not in exclude]
        for fn in sorted(filenames):
            full = os.path.join(dirpath, fn)
            if os.path.islink(full) or not os.path.isfile(full):
                continue
            rel = os.path.relpath(full, root)
            entry = scan_file(full, rel, max_bytes)
            if entry.error and entry.error.startswith("unreadable"):
                inv.unreadable.append(rel)
            inv.files.append(entry)
    inv.skipped_dirs = sorted(set(skipped))
    inv.entry_points = sorted(
        f.path for f in inv.files
        if f.kind == "html"
        and os.path.basename(f.path).lower() in ("index.html", "index.htm"))
    if not inv.files:
        inv.warnings.append("Empty project (after exclusions).")
    if inv.unreadable:
        inv.warnings.append("%d unreadable file(s)." % len(inv.unreadable))
    return inv

def to_dict(inv):
    return {
        "tool": "webreverse-designer/check_project.py",
        "version": VERSION,
        "root": inv.root,
        "counts": inv.counts,
        "entry_points": inv.entry_points,
        "skipped_dirs": inv.skipped_dirs,
        "unreadable": inv.unreadable,
        "warnings": inv.warnings,
        "files": [asdict(f) for f in inv.files],
    }


def to_text(inv):
    out = ["Inventory: %s" % inv.root, "Tool version: %s" % VERSION]
    c = inv.counts
    out.append("Files: %d (HTML %d, CSS %d, JS %d, other %d)"
               % (c["total"], c["html"], c["css"], c["js"], c["other"]))
    if inv.entry_points:
        out.append("Entry points: " + ", ".join(inv.entry_points))
    else:
        out.append("Entry points: no index.html detected.")
    for f in inv.files:
        extra = ""
        if f.error:
            extra = " [ERROR: %s]" % f.error
        elif f.encoding_issue:
            extra = " [imperfect encoding]"
        trunc = " [truncated]" if f.truncated else ""
        lines = " — %d lines" % f.lines if f.lines is not None else ""
        out.append("  - %s (%s, %d B%s)%s%s"
                   % (f.path, f.kind, f.size_bytes, lines, trunc, extra))
        if f.refs:
            out.append("      refs: " + ", ".join(f.refs[:10]))
    if inv.skipped_dirs:
        out.append("Excluded folders: " + ", ".join(inv.skipped_dirs))
    for w in inv.warnings:
        out.append("WARNING: " + w)
    return "\n".join(out) + "\n"


def build_parser():
    p = argparse.ArgumentParser(description="Inventory a folder (no exec).")
    p.add_argument("path", help="Local project folder to inventory.")
    p.add_argument("--json", action="store_true", help="JSON output.")
    p.add_argument("--max-bytes", type=int, default=262144)
    p.add_argument("--version", action="store_true")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.version:
        print(VERSION)
        return 0
    if args.max_bytes <= 0:
        print("Error: --max-bytes must be > 0.", file=sys.stderr)
        return 1
    if not os.path.isdir(args.path):
        print("Error: folder not found: %s" % args.path, file=sys.stderr)
        return 1
    try:
        inv = scan_project(args.path, args.max_bytes)
    except Exception as exc:
        print("Unexpected error: %s" % exc, file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(to_dict(inv), ensure_ascii=False, indent=2))
    else:
        print(to_text(inv), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())

