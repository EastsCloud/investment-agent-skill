# Project model and initialization

The skill contains reusable instructions and templates. The user workspace owns all
personal state; never write user holdings, preferences or research into the public plugin.

```text
AGENTS.md                       durable rules and continuation protocol
README.md                       everyday use
investment_philosophy.md         user-owned principles, initially blank
checklist.md                     analytical questions
mistakes_and_lessons.md          user history, initially blank
watchlist.md                    empty watchlist
memo_template.md                company memo structure
sector_template.md              sector memo structure
proposed_update_template.md     reviewable changes
companies/  sectors/            formal memos
inbox_unprocessed/              untouched raw input
chatgpt_outputs/                unverified model output
reports/                       research and weekly review drafts
proposed_updates/               pending / approved / applied proposals
context_packs/                  handoffs to deeper analysis
data/                          optional data (not indexed by default)
scripts/                       editable retrieval implementation
rag/index/                     SQLite database
rag/extracted_text/             plaintext cache
rag/logs/                      diagnostics
```

Inspect existing targets first. Exclusive writes create missing files; identical templates
are skipped and differing files reported as conflicts. Existing files and blocked
directories are preserved. Links/junctions are rejected. Compare templates and user files
and propose concrete migration changes. Initial blank formal templates are authorized by
initialize. Installing a new plugin version does not upgrade copied user scripts.

For upgrades, compare versions, preserve user edits, propose migration and apply only
authorized changes. Rebuild the derived index if needed. validate_project reports structure,
freshness, parse errors and counts. A new workspace without an index can be structurally
valid. Empty company/sector directories are normal; report a missing memo when needed.
No automatic Git operations run in user workspaces. The scaffold .gitignore excludes
derived caches, not all personal research. Review everything before publication.
