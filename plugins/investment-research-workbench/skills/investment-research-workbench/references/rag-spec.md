# Local retrieval contract

Python 3.10+ with standard SQLite supports MD, TXT, CSV and basic DOCX. Optional openpyxl
handles XLSX; pypdf handles text PDF. Ask before installing requirements-optional.txt.
No network, embeddings, LLM calls or FTS extension.

## Scope and metadata

Index four core files plus companies/sectors (formal), reports/chatgpt_outputs/proposed_updates
(auxiliary), and inbox_unprocessed (unprocessed). data, context_packs, AGENTS, templates,
scripts, dotfiles, Git, virtualenvs, node_modules and caches are excluded. Links/junctions
are not followed. Unsupported files in scope get diagnostics.

SQLite stores chunk ID, relative path, type, zone, heading, location, empty company/sector
guesses, mtime, SHA-256, indexed-at UTC and text. Publication date remains unknown until
source review. Every result is unverified; formal is a user record, not an external fact.

Chunks cap at 1,400 characters with 150-character overlap when needed. Preserve text
headings/lines, PDF page, DOCX heading/paragraph (including tables), XLSX workbook/sheet/
column letters/row, CSV header/row. Long rows split. DOCX layout, textboxes and footnotes,
and PDF table structure are not fully represented. Check originals before numerical use.
Excel formulas are never evaluated; only saved cached values are read and absent caches
can omit values. CSV uses comma-separated RFC-style records.

Build skips successfully parsed sources only when hash and mtime match. Changed sources
replace chunks transactionally. Deleted or newly unreadable files lose old searchable
chunks. Failed sources retry on the next build. --rebuild re-extracts all without modifying
originals. Local caches/logs can retain deleted source text; deletion is not secure erasure.

## Ranking and freshness

search(root, query, top_k, zone) is the extension point for future local vector/hybrid backends.
Current ranking combines English tokens, Chinese bigrams, inverse document frequency,
exact query-term matches and filename/path boosts. Zone multipliers: formal 1.15,
auxiliary 1.0, unprocessed 0.9. No recency ranking. Scores are not probabilities or authority.
Ties are deterministic. Lexical retrieval needs explicit aliases; it is not semantic search.

CLI search/context checks hashes and refuses stale indexes. JSON search returns
{index_status, results}. Each hit includes rank, score, citations, excerpt, metadata and
text. Use --zone for targeted review. Evidence generation reserves formal and inbox hits,
deduplicates chunk IDs, takes at most top-k chunks, 700 characters per excerpt, 12,000
excerpt characters total. Codex must still read core records and synthesize the final pack.

## Recovery and limitations

Build exit 0 = complete, 1 = partial with per-file errors, 2 = index failure.
Build missing indexes; refresh stale ones. For corrupt DB, preserve it and use a new index
only under authorized repair; scan sources directly meanwhile. Unknown schemas fail.
Missing optional parsers affect only those files; ask before installation.
Scanned or partially image-only PDFs require OCR and are not partially indexed as if complete.
Legacy DOC/XLS, images, encrypted PDFs and OCR are unsupported; request supported exports
or use available trusted document readers.

Limits: 50 MiB/source; 5 million extracted chars; Word XML 50 MiB; expanded XLSX 200 MiB.
Split larger files. These limits are not a hostile-parser sandbox; use the host sandbox.
Search scans chunks and suits a personal corpus, not millions of chunks. One builder at
a time. No automatic jobs. Do useful research through direct files when RAG cannot work.
