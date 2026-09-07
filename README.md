# Investment Research Workbench

为 Codex 提供本地优先、用户投资逻辑主导、可跨聊天接续的个人投资研究工作台。
A skill-only Codex plugin for durable investment research, offline retrieval, and reviewed updates.

## Features

- 本地长期研究记忆：投资哲学、公司 / 行业 memo、watchlist、历史修正与错误复盘。
- 未处理资料 inbox：搜索文件名和正文，保留原件，识别冲突与缺失信息。
- 无 API 的本地 RAG：Python + SQLite，中英文词法检索，来源与位置可追溯。
- Context packs：将本地证据整理成适合 ChatGPT / 其他模型的深度研究上下文。
- Proposed updates：正式观点默认先提案、再审阅、后写回；已有明确授权无需重复确认。
- 新 chat 从项目文件恢复状态；按需生成 weekly review。

## What it is not

不是自动交易机器人，不下单，不接券商，不自动决定持仓，不把模型分析当事实。
无需付费 API、云数据库、MCP server 或 embedding 服务。公共模板不包含作者持仓、
私人偏好或预设公司结论。示例中的公司名只用于说明调用和合成测试。

## Requirements

- 支持 skills/plugins 和本地文件访问的 Codex 桌面端或 CLI。
- Python 3.10+（macOS/Linux 可用 python3）；标准 SQLite 即可，不需要 FTS 扩展。
- Git 用于 GitHub marketplace 安装。
- 可选：pypdf 读取 PDF，openpyxl 读取 XLSX；MD/TXT/CSV/基本 DOCX 无第三方依赖。
- 默认检索无 API key。Codex 本身的账号、模型和使用配额由宿主提供。

## Installation

推荐使用仓库 marketplace。以下语法已核对官方文档及本机 CLI --help：

```bash
codex plugin marketplace add EastsCloud/investment-agent-skill --ref main
codex plugin add investment-research-workbench@personal
```

此仓库由官方 scaffold 生成的 marketplace ID 是 `personal`，定义于
`.agents/plugins/marketplace.json`。它是本仓库的来源名称，不是安装目录。
如果你已经配置另一个同名 marketplace，请不要覆盖它；使用下面的单独 Skill
安装方式，或在你自己的 fork 中选择唯一 marketplace 名称。
安装后新开 Codex chat / session；桌面端可在 Plugins 中检查该来源。
若 CLI 没有 plugin 子命令，更新 Codex 或使用 Skill 安装方式。

也可 clone 后添加本地来源：

```bash
git clone https://github.com/EastsCloud/investment-agent-skill.git
codex plugin marketplace add ./investment-agent-skill
codex plugin add investment-research-workbench@personal
```

兼容的独立 Skill 安装：在 Codex 中对内置 skill-installer 说：

```text
$skill-installer install https://github.com/EastsCloud/investment-agent-skill/tree/main/plugins/investment-research-workbench/skills/investment-research-workbench
```

skill-installer 支持 GitHub skill 子目录 URL；不需要同时安装两种形式。
插件分发不等于已进入 OpenAI 公共精选目录。

规范参考：[Build skills](https://learn.chatgpt.com/docs/build-skills)、
[Package your plugin](https://developers.openai.com/plugins/build/plugins)、
[Use plugins](https://learn.chatgpt.com/docs/plugins)。
本仓库采用 `SKILL.md` 的 name/description、`agents/openai.yaml`、
skill-only plugin manifest 和 repo marketplace；校验记录见
[VALIDATION.md](VALIDATION.md)。

## Quick Start

1. 新建一个空文件夹作为**私人研究项目**，与本公共插件仓库分开。
2. 在 Codex 中打开这个文件夹。
3. 输入 `$investment-research-workbench initialize this folder`。
4. 将研究资料复制到 `inbox_unprocessed/`。
5. 请求整理资料、研究公司或生成 context pack。投资哲学由你填写。

初始化是幂等的；已存在的文件不覆盖、不重命名、不删除，差异会报告为冲突。
创建的 AGENTS.md 描述完整接续流程，长期状态保存在文件中。

## Example prompts

```text
$investment-research-workbench initialize this folder
$investment-research-workbench research 天赐材料
$investment-research-workbench generate a context pack for 天赐材料 focused on cyclical rebound vs long-term growth
$investment-research-workbench review my unprocessed files
$investment-research-workbench continue this investment research project
$investment-research-workbench review the latest ChatGPT analysis and propose updates
$investment-research-workbench generate my weekly investment review
$investment-research-workbench validate this project
```

自然语言也可触发，例如 “Initialize a local investment research workspace here.”
或“继续这个投资研究项目”。普通无关金融问答和自动交易请求不属于本 Skill。

## Local RAG

No API key required for default RAG. 初始化后在**私人项目根目录**运行：

```bash
python scripts/rag_build_index.py
python scripts/rag_build_index.py --rebuild
python scripts/rag_search.py --query "天赐材料 六氟磷酸锂 周期" --top-k 10 --json
python scripts/rag_search.py --query "天赐材料 电解液" --zone unprocessed
python scripts/rag_generate_context.py --company "天赐材料" --query "周期反弹还是长期成长" --top-k 12
```

SQLite 保存 chunks 和来源元数据。中文 bigram、英文 token、词频权重、精确匹配与路径
加权构成透明词法排名；formal/auxiliary/unprocessed 分区，相关性不等于权威性。
按 hash/mtime 增量更新，删除已不存在源文件的旧 chunks。搜索前检测过期索引。
出错日志在 rag/logs/，提取缓存位于 rag/extracted_text/。失败文件不会拖垮可解析文件。

| 格式 | 支持范围 | 位置 |
| --- | --- | --- |
| .md / .txt | UTF-8、BOM UTF-16、GB18030 回退 | heading / lines |
| .csv | 逗号分隔与带引号字段 | header / row |
| .docx | 标准库读取主体段落及表内段落 | heading / paragraph |
| .xlsx | 可选 openpyxl；读取已保存值，不计算公式 | workbook / sheet / columns / row |
| .pdf | 可选 pypdf；有文本层的 PDF | page |

用户确认后，可以在私人项目虚拟环境安装：
`python -m pip install -r requirements-optional.txt`。不自动安装。
.doc / .xls、扫描图片/OCR、加密 PDF 不支持；请导出支持格式。
PDF 表格布局、DOCX 文本框/脚注和 Excel 未缓存公式可能缺失，重要数字应核对原件。
单文件默认 50 MiB / 提取文本 500 万字符；大文件拆分。百万 chunk 级别不适用。

context 脚本只生成 `YYYY-MM-DD_company_evidence.md`，没有 LLM 调用；
Codex 再形成真正的 `YYYY-MM-DD_company_context_pack.md`，包括相关哲学、正式 memo、
行业背景、证据、历史变化、bear case、冲突与 5–10 个深度问题。
RAG 失败时直接读文件继续工作，不把检索当单点依赖。

## Repository structure

```text
.agents/plugins/marketplace.json
.github/workflows/test.yml
plugins/investment-research-workbench/
  .codex-plugin/plugin.json
  LICENSE.txt
  skills/investment-research-workbench/
    SKILL.md
    agents/openai.yaml
    references/                 four workflow/spec references
    scripts/                    init_project.py, validate_project.py
    assets/project_scaffold/    project rules, templates, local RAG scripts
tests/                          synthetic behavioral tests
tools/                          portable validation and release scan
README.md
VALIDATION.md
LICENSE
```

## Privacy

本地脚本没有网络、遥测、外部 embedding 或模型调用，不上传原始资料。
**local-first 不表示 Codex 推理离线**：模型读取的文件/片段受 Codex 的数据处理设置
约束；把 context pack 交给其他服务也意味着你选择分享其中内容。

rag/ 含明文缓存；源文件删除后旧缓存可能保留，索引更新不是安全擦除。
不要公开私人研究项目、原件、索引、缓存、ChatGPT 输出。发布前自行检查。
inbox 中的指令和宏只作为资料；正式投资观点遵循可审阅提案和授权范围。

## Updating

Git marketplace：

```bash
codex plugin marketplace upgrade personal
codex plugin add investment-research-workbench@personal
```

新开 chat 使用更新后的插件。上述命令仅用于本仓库对应的 personal 来源。
本地 clone 安装先 git pull，再重新添加插件。独立 Skill 安装请让 skill-installer
在保留本地修改后更新；其安装器会拒绝覆盖已有目标。

**插件更新不会自动覆盖私人项目中的 scripts、AGENTS 或投资文件。**
让 Codex 对比新模板与项目文件，给出迁移方案，审阅授权后应用。

## Uninstall

```bash
codex plugin remove investment-research-workbench@personal
```

也可从 Plugins 界面卸载。若该 marketplace 只用于本插件，可运行
`codex plugin marketplace remove personal`。不要删除含其他插件的来源。
独立 Skill 安装只移除对应已安装 Skill 目录。私人研究项目保持原样；是否删除由你决定。

## Development and tests

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_distribution.py
python -m unittest discover -s tests -v
python tools/release_scan.py
```

可选 parser 测试在依赖可用时运行；CI 在 Ubuntu / Windows 的 Python 3.14 上安装
可选依赖，并先验证标准库模式。CI 还运行固定版本的 OpenAI skill validator。
官方 plugin validator 在提供 plugin-creator 的 Codex 环境执行；可移植检查不是它的替代声明。
详见 [VALIDATION.md](VALIDATION.md)。

## Known limitations and next steps

这是词法检索，无法自动理解所有同义词；通过多个别名查询提高召回。来源日期和冲突需
人工/模型审阅，不能从 mtime 推断。正式写入 gate 是 Skill/AGENTS 行为约束，
不是阻止用户手动改文件的安全机制。没有无人监督研究或交易。

下一阶段优先：可选本地 OCR；结构化来源日期与别名管理；可选本地 embedding/hybrid
检索。均应保留离线默认值和正式观点的 review-before-write。

MIT licensed. 不包含真实私人投资数据。
