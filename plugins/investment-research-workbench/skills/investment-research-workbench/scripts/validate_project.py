"""Read-only project health check, including missing files and stale evidence."""
import argparse
import json
import sqlite3
import sys
from pathlib import Path
from init_project import DIRECTORIES, SCAFFOLD, linked, safe_path

# Use the bundled trusted implementation, not code found in a target workspace.
sys.path.insert(0, str(SCAFFOLD / "scripts"))
from raglib import index_status, scan  # noqa: E402


def validate(root):
    root = Path(root).absolute()
    missing, conflicts = [], []
    expected_files = [p.relative_to(SCAFFOLD).as_posix() for p in SCAFFOLD.rglob("*")
                      if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"]
    for relative, directory in [(d, True) for d in DIRECTORIES] + [(f, False) for f in expected_files]:
        try:
            path = safe_path(root, relative)
            if not (path.is_dir() if directory else path.is_file()):
                missing.append(relative)
        except (OSError, ValueError):
            conflicts.append(relative)
    def count(name):
        base = root / name
        if not base.is_dir() or linked(base):
            return 0
        return sum(1 for p in scan(root) if p.relative_to(root).parts[0] == name)
    try:
        index = index_status(root)
        index["available"] = True
    except (OSError, ValueError, sqlite3.Error) as exc:
        index = {"available": False, "message": str(exc)}
    return {"valid_structure": not missing and not conflicts, "missing": missing,
            "conflicts": conflicts, "index": index,
            "inbox_files": count("inbox_unprocessed"), "proposed_updates": count("proposed_updates")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(args.target)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Project structure: {'OK' if result['valid_structure'] else 'NEEDS ATTENTION'}")
        print(f"Inbox: {result['inbox_files']}; proposed updates: {result['proposed_updates']}")
        for name in ("missing", "conflicts", "index"):
            print(f"{name}: {json.dumps(result[name], ensure_ascii=False)}")
    return 0 if result["valid_structure"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
