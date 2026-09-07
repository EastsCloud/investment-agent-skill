# Local investment research workspace

English (primary); Chinese equivalent follows.

Files are durable memory. You own the investment logic; Codex retrieves, analyzes and proposes.
Use your preferred language for personal records.

## Basic workflow

1. Copy PDF/DOCX/XLSX/Markdown/TXT/CSV into inbox_unprocessed/.
2. Ask Codex to review unprocessed files and identify evidence and data problems.
3. Generate a context pack; optionally share selected content for deeper analysis.
4. Save model analysis under chatgpt_outputs/ and request a proposed update.
5. Review and authorize concrete changes before formal records change; retain history.

## RAG

Python 3.10+. Run from this private project:

```bash
python scripts/rag_build_index.py
python scripts/rag_build_index.py --rebuild
python scripts/rag_search.py --query "天赐材料 六氟磷酸锂 周期" --top-k 10 --json
python scripts/rag_generate_context.py --company "天赐材料" --query "cyclical rebound or long-term growth"
```

MD/TXT/CSV/basic DOCX need no extra library. After user approval, install optional PDF/XLSX parsers
in a virtual environment: `python -m pip install -r requirements-optional.txt`.
Scanned PDF needs OCR; export legacy DOC/XLS. Errors do not alter originals.
Refresh missing/stale indexes; directly inspect files that cannot be parsed. Logs: rag/logs/.
The context script creates an evidence skeleton; Codex writes the finished pack.

## New Codex chat

Open another chat in the same project and send:
`$investment-research-workbench continue this investment research project`.
AGENTS.md also explains the rules and continuity when the Skill is unavailable.

## Safety and privacy

No automatic deletion/movement, unauthorized thesis changes or trading.
Retrieval is offline; model reading follows the host's data settings. Keep rag/ private.
Source deletion does not purge old caches. Plugin updates do not replace copied scripts;
compare and review migrations.

---

# 中文

# 本地投资研究工作区

长期记忆在本地文件中。由你维护投资逻辑，Codex 协助检索、分析和提出修改。

## Basic workflow

1. 把 PDF / DOCX / XLSX / Markdown / TXT / CSV 资料复制到 inbox_unprocessed/。
2. 让 Codex review my unprocessed files，读取原件、检索并报告资料问题。
3. 生成 context pack，按需交给 ChatGPT/其他模型深入分析。
4. 把分析保存到 chatgpt_outputs/，请求 proposed update。
5. 审阅并确认；Codex 才在授权范围内写入正式长期记录并保留历史。

## RAG

Python 3.10+；默认无 API。从本目录运行：

```bash
python scripts/rag_build_index.py
python scripts/rag_build_index.py --rebuild
python scripts/rag_search.py --query "天赐材料 六氟磷酸锂 周期" --top-k 10 --json
python scripts/rag_generate_context.py --company "天赐材料" --query "周期反弹还是长期成长"
```

MD/TXT/CSV/基本 DOCX 不需要额外库。用户同意后，可在虚拟环境中安装
`python -m pip install -r requirements-optional.txt` 来读取 PDF/XLSX。
扫描 PDF 需要 OCR；旧 .doc/.xls 请导出。索引错误不会改动原件；
缺失/过期先刷新，无法解析时直接检查原件。日志在 rag/logs/。
context 脚本输出 evidence skeleton，完整 context pack 由 Codex 总结。

## New Codex chat

在同一文件夹新开 chat，说：
`$investment-research-workbench continue this investment research project`。
即使未安装 Skill，AGENTS.md 也描述了长期规则和接续步骤。

## Safety and privacy

原件不会自动删除或移动；正式投资逻辑不会擅自改变；不执行交易。
本地检索不上传数据，宿主模型读取内容仍受模型服务设置约束。
rag/ 含明文缓存，不要公开。删除源文件并不自动清除旧提取缓存。
插件更新不会覆盖已复制的脚本；请对比并审阅迁移。
