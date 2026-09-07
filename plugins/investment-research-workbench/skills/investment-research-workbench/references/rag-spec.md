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

---

## 中文 / Chinese equivalent

Python 3.10+ 与标准 SQLite 可读 MD/TXT/CSV/基本 DOCX；openpyxl 支持 XLSX，
pypdf 支持文本 PDF，均可选。安装 requirements-optional.txt 前询问用户。
无网络、embedding、LLM 或 FTS 扩展。

索引四个核心文件，以及 companies/sectors（formal），reports/chatgpt_outputs/
proposed_updates（auxiliary），inbox_unprocessed（unprocessed）。
data、context_packs、AGENTS、模板、scripts、隐藏文件、Git、虚拟环境、node_modules、
缓存不索引。不跟随链接/junction；范围内未知格式有诊断。
chunk 保存 ID、相对路径、类型、zone、标题、位置、空公司/行业猜测、mtime、
SHA-256、UTC 索引时间和正文。来源日期待审阅，所有检索结果未独立验证。
formal 是用户记录，不是外部事实证明。

chunk 最多 1,400 字符，必要时重叠 150。保留文本标题/行，PDF 页，
DOCX 标题/段落，XLSX 工作簿/表/列/行，CSV 表头/行，长行拆分。
DOCX 文本框/脚注和 PDF 表格结构可能不完整；数值结论核对原件。
Excel 不计算公式，只读缓存值；缺缓存可能漏值。CSV 逗号分隔并支持引号字段。

上次成功且 hash/mtime 都一致才跳过。变更资料以事务替换；删除或不可读源失去旧
可检索 chunk；失败下次重试。--rebuild 重提取全部，不改原件。
缓存和日志可能保留已删除内容，索引更新不是安全擦除。

search(root, query, top_k, zone) 是未来 vector/hybrid 扩展接口。
当前结合英文 token、中文 bigram、逆文档频率、精确匹配、路径加权；
zone 权重为 1.15 / 1.0 / 0.9。不按日期排名，分数不是概率/权威。
同分顺序确定，同义词需别名。CLI 查 hash 并拒绝过期索引，JSON 返回
{index_status, results}，包括排名、分数、引用、片段、metadata、正文。
--zone 可定向查询。evidence 保留 formal/inbox 命中、按 chunk ID 去重，
最多 top-k 条，每条 700 字符，片段合计 12,000 字符；Codex 仍需完成总结。

build 退出 0 完成、1 部分成功、2 失败。缺失先建，过期先刷新。
损坏 DB 先保留，只在授权修复下用新索引，同时直接读文件；未知 schema 拒绝。
缺 parser 只影响对应文件。扫描/部分无文本 PDF 需 OCR，不把部分提取当完整。
旧 DOC/XLS、图片、加密 PDF、OCR 不支持，需导出或可信工具。
限制：单源 50 MiB，提取 500 万字符；Word XML 50 MiB，展开 XLSX 200 MiB。
更大文件拆分。这不是 parser 安全沙箱，仍使用宿主沙箱。
面向个人库，不适合百万 chunk；一次一个 builder，无自动任务；
修不好 RAG 就通过原文件继续研究。
