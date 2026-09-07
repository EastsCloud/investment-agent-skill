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

---

## 中文 / Chinese equivalent

Skill 保存通用指令和模板，私人项目保存个人状态。持仓、偏好与研究不写入公共插件。
AGENTS.md 是长期规则，README.md 是日常说明；投资哲学、checklist、复盘、watchlist
分别保存用户原则、分析问题、错误历史和观察名单，个人记录初始为空。
memo_template、sector_template、proposed_update_template 分别是公司、行业与提案格式。
companies/sectors 是正式记录；inbox 保留原件；chatgpt_outputs 是未验证模型输出；
reports 保存草稿；proposed_updates 保存各状态提案；context_packs 用于交接。
data 默认不索引；scripts 可编辑；rag 下分别是数据库、提取明文和诊断日志。

初始化前检查目标；缺失才创建，相同跳过，不同报告冲突，保留所有已有文件。
拒绝链接/junction；比较模板和现有内容后给出迁移提案。
初始化空白模板已由 initialize 授权。插件升级不覆盖复制到项目中的脚本。
升级时比较版本、保留用户改动，仅应用授权修改，必要时重建派生索引。
validate_project 报告结构、新鲜度、解析错误和数量。新项目无索引也可结构有效。
公司/行业目录为空正常；具体研究缺 memo 要报告。不自动操作用户项目 Git。
.gitignore 只隐藏派生缓存，不隐藏所有个人研究；公开前逐项审阅。
