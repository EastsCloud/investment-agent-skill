# Research workflows

## Continue across chats

Read AGENTS and core files first. Inspect relevant recent company/sector memos, pending
proposals, packs, reports and ChatGPT outputs. Check inbox and index health. Use timestamps
for discovery, then dated entries for actual history. Summarize goals, state, unfinished
tasks and next action. Do not initialize again or depend on old chat history.

## Ingest and research

1. Establish the question and user framework. Read company and sector memos; report missing
   memos and draft a proposal when useful.
2. Refresh RAG. Search company, ticker, known aliases, products, sector, competitors,
   financial reports, policies and industry prices. Do not invent alias relationships.
   Use multiple short queries and --zone unprocessed so top-k cannot hide inbox evidence.
3. Read matching bodies with surrounding context. Inspect parse failures and unsupported
   files using available trusted document readers. Disclose unread pages/sheets and OCR
   gaps rather than claiming completeness.
4. Retrieve historical changes, lessons, prior ChatGPT outputs and conflicting evidence.
   Multiple copies of one report do not count as independent support.
5. Present evidence with path/location, origin/date, relevance, zone, verification,
   staleness, conflict with memo and suggested archive destination. Unknown dates stay unknown.
6. Analyze normally in Codex. Separate facts, user judgments, outside opinions and inference.
   Use reliable dated sources for changing market facts when available; otherwise say
   缺少最新数据. Include bear case, uncertainty and next verification steps. Propose formal changes.

Inbox review creates reports/YYYY-MM-DD_inbox_review.md, with collision suffix if needed,
including unreadable and unsupported files. Preserve originals. Indexing is not approval.

## Context pack

Run rag_generate_context.py for context_packs/YYYY-MM-DD_company_evidence.md. It is a
deterministic skeleton. Read it, core files, current memos, inbox evidence and history;
then write the actual context_packs/YYYY-MM-DD_company_context_pack.md with:

1. Exact research question.
2. Only relevant user-authored philosophy; say not supplied when blank.
3. Current thesis, type, variables, buy/sell conditions, risks and gaps.
4. Sector context.
5. Curated evidence with path, location, type/zone, excerpt/summary, verification, date, conflict.
6. Unverified inbox evidence.
7. Dated thesis changes and lessons.
8. Strongest evidence-backed bear case.
9. Conflicts, missing/old evidence and uncertainty.
10. Five to ten case-specific deep-analysis questions.

Aim for focused information (normally 1,500–3,000 words, shorter for sparse sources), not
document concatenation. Preserve citations and never invent financial facts. Tell the
user where the finished pack is. Sharing to ChatGPT/another service remains user-chosen.

## ChatGPT output and formal updates

Read relevant chatgpt_outputs, verify claims, compare current formal views, surface
conflicts and assumptions, and propose exact updates. Follow safety-and-write-policy.
LLM analysis is input, not proof.

## Weekly review on request

Read watchlist, memos, lessons, reports, recent files and RAG. State review date range.
Create reports/YYYY-MM-DD_weekly_review.md covering new research, authorized thesis changes,
new evidence, major conflicts, verification questions, stale company reviews and next
week's suggestions. mtime alone is not a confirmed thesis change. Label assumed freshness
thresholds. Suggestions remain draft. Do not install recurring monitoring.
