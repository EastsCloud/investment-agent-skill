"""Initialize a research workspace without replacing user files (Python 3.10+)."""
import argparse
import json
from pathlib import Path

SCAFFOLD = Path(__file__).resolve().parents[1] / "assets" / "project_scaffold"
DIRECTORIES = (
    "companies", "sectors", "context_packs", "chatgpt_outputs", "reports",
    "scripts", "data", "inbox_unprocessed", "proposed_updates",
    "rag/index", "rag/extracted_text", "rag/logs",
)


def linked(path):
    try:
        return path.is_symlink() or bool(getattr(path.lstat(), "st_file_attributes", 0) & 0x400)
    except FileNotFoundError:
        return False


def safe_path(root, relative):
    """Reject links, traversal, and file ancestors before touching a destination."""
    root = Path(root).absolute()
    relative = Path(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Expected a project-relative path")
    for part in [root, *root.parents]:
        if linked(part):
            raise ValueError(f"Linked project ancestor: {part.name}")
    target = root / relative
    for part in [target, *target.parents]:
        if part == root:
            break
        if linked(part):
            raise ValueError(f"Linked destination: {relative}")
    return target


def initialize(target):
    root = Path(target).absolute()
    safe_path(root, ".")
    root.mkdir(parents=True, exist_ok=True)
    events = []
    for relative in DIRECTORIES:
        try:
            path = safe_path(root, relative)
            existed = path.is_dir()
            path.mkdir(parents=True, exist_ok=True)
            events.append({"path": relative, "status": "existing" if existed else "created"})
        except (OSError, ValueError) as exc:
            events.append({"path": relative, "status": "conflict", "reason": str(exc)})
    for source in sorted(SCAFFOLD.rglob("*")):
        if not source.is_file() or "__pycache__" in source.parts or source.suffix == ".pyc":
            continue
        relative = source.relative_to(SCAFFOLD).as_posix()
        try:
            path = safe_path(root, relative)
            if path.exists():
                same = path.is_file() and path.read_bytes() == source.read_bytes()
                events.append({"path": relative, "status": "skipped" if same else "conflict"})
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as stream:
                stream.write(source.read_bytes())
            events.append({"path": relative, "status": "created"})
        except (OSError, ValueError) as exc:
            events.append({"path": relative, "status": "conflict", "reason": str(exc)})
    return events


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        events = initialize(args.target)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Initialization failed: {exc}\n")
    if args.json:
        print(json.dumps(events, ensure_ascii=False, indent=2))
    else:
        for event in events:
            print(f"{event['status']:8} {event['path']}")
        if any(e["status"] == "conflict" for e in events):
            print("Migration: compare conflicts against bundled templates; manually merge only authorized changes. Existing files were preserved.")
    return 1 if any(e["status"] == "conflict" for e in events) else 0


if __name__ == "__main__":
    raise SystemExit(main())
