"""Search indexed local evidence with source citations."""
import argparse
import json
from pathlib import Path
from raglib import index_status, search


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--zone", choices=["formal", "auxiliary", "unprocessed"])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        status = index_status(args.root)
        hits = search(args.root, args.query, args.top_k, args.zone)
        # Never return deleted or changed cached text as current evidence.
        if status["stale"]:
            parser.exit(2, "Index is stale. Run scripts/rag_build_index.py, or scan source files directly.\n")
    except Exception as exc:
        parser.exit(2, f"Retrieval unavailable: {exc}\n")
    if args.json:
        print(json.dumps({"index_status": status, "results": hits}, ensure_ascii=False, indent=2))
    else:
        for hit in hits:
            print(f"{hit['rank']}. score={hit['score']} | {hit['file_path']} | {hit['source_zone']} | {hit['location']} | {hit['verification_status']}\n{hit['excerpt']}\n")
        if not hits:
            print("No matches. Try aliases, ticker, product, sector, or direct source inspection.")
        for error in status["parse_errors"]:
            print(f"Unindexed: {error['file_path']} — {error['error']}")


if __name__ == "__main__":
    main()
