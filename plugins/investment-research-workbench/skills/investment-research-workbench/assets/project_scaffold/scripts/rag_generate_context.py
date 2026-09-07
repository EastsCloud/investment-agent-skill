"""Generate a cited evidence skeleton; Codex completes the research synthesis."""
import argparse
from pathlib import Path
from raglib import generate_context, index_status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--company", required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=12)
    args = parser.parse_args()
    try:
        if index_status(args.root)["stale"]:
            raise ValueError("Index stale; rebuild before creating context")
        print(generate_context(args.root, args.company, args.query, args.top_k))
    except Exception as exc:
        parser.exit(2, f"Context generation unavailable: {exc}\n")


if __name__ == "__main__":
    main()
