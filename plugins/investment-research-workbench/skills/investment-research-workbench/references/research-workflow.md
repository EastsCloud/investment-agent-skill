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

---

## 中文 / Chinese equivalent

### 跨 chat 接续

先读 AGENTS 与核心文件，再查看相关近期 memo、待处理提案、pack、报告、ChatGPT 输出、
inbox 和索引。mtime 用于发现文件，实际历史依靠有日期的条目。
总结目标、状态、未完成和下一步，不初始化，不依赖旧 chat。

### 导入与研究

1. 结合用户框架确定问题，读公司/行业 memo；缺失报告，有用时起草提案。
2. 刷新 RAG，查询公司、ticker、已知别名、产品、行业、竞争对手、财报、政策、价格；
   不编造关联。多个短 query 加 --zone unprocessed，避免 top-k 隐藏 inbox。
3. 读命中正文和周边内容，用可信工具检查解析失败/不支持资料，说明未读页/表/OCR 缺口。
4. 找历史修正、复盘、ChatGPT 输出与反证；报告副本不算独立证据。
5. 展示路径/位置、来源日期、相关性、zone、验证、新鲜度、冲突和建议归档位置。
6. 正常分析，区分事实、用户判断、外部意见和推理。变动事实需可靠来源日期；
   缺失写“缺少最新数据”。加入 bear case、风险、下一步验证；正式改动另行提案。

inbox review 生成 reports/YYYY-MM-DD_inbox_review.md，同名加序号，
包括不可读和不支持文件。保留原件；索引不是批准。

### Context pack

脚本生成 YYYY-MM-DD_company_evidence.md 后，Codex 结合核心文件、正式 memo、
inbox 和历史，另写完整 YYYY-MM-DD_company_context_pack.md：
本次问题、相关用户哲学（空白则说未提供）、当前 thesis/类型/变量/买卖条件/风险、
行业、带路径/位置/类型/zone/日期/验证/冲突的证据、inbox、历史变化、最强 bear case、
冲突与缺口、5–10 个具体问题。通常 1,500–3,000 词，资料少则更短。
不拼全文、不编造财务数据，保留引用，告知文件位置；是否分享由用户选择。

### 模型输出与周复盘

ChatGPT 输出要核实并与正式观点比较，找冲突和假设后提具体修改；遵循写入规则。
周复盘需读 watchlist、memo、复盘、报告、新增资料和 RAG，明确时间段，
写 reports/YYYY-MM-DD_weekly_review.md：新增研究、授权观点变化、新证据、
冲突、待验证、长期未更新公司、下周建议。mtime 不是观点变化证明，
新鲜度阈值若是假设需说明。建议保持草稿，不安装定时器。
