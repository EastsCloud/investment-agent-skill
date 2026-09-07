"""Build or incrementally refresh the local research index."""
import argparse
import json
from pathlib import Path
from raglib import build


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()
    try:
        result = build(args.root, args.rebuild)
    except Exception as exc:
        parser.exit(2, f"Index failed: {exc}. Read local sources directly if rebuilding cannot repair it.\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    # 1 indicates partial success; good sources remain searchable.
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
