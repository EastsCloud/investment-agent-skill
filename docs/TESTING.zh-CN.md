# 自己试用和测试工作台

[English (primary)](TESTING.md) · 简体中文 · [首页](../README.zh-CN.md)

这里分两类：实际在 Codex 中试用，检查 **prompt 和工作流**；自动化测试检查
**Python 工具**。代码测试通过，并不能证明模型行为符合预期。

## 1. 安装或更新

按 [安装说明](../README.zh-CN.md#installation) 操作。已从本仓库安装时：

```bash
codex plugin marketplace upgrade personal
codex plugin add investment-research-workbench@personal
```

仅用于本仓库的 personal 来源；同名冲突处理见 README。安装后新开 Codex chat/session。
本地开发可把 checkout 添加为本地 marketplace，修改后重装并新开 chat。
不要同时安装独立 Skill 和 Plugin 两个副本。

## 2. 在独立测试项目初始化

在插件仓库**外面**新建空文件夹 investment-workbench-test，用 Codex 打开它。
在聊天框发送：

```text
$investment-research-workbench initialize this folder
```

预期：生成 AGENTS.md、投资哲学、checklist、watchlist、memo 模板、inbox、
companies/sectors、context/proposal 目录和 scripts。没有自动填入持仓或公司结论。
你手动在投资哲学里加一句“测试偏好：要求证据日期”，再重复初始化。
预期：这句话保留，差异会报告，不会覆盖你的文件。

## 3. 放入合成资料

你自己创建 inbox_unprocessed/sample-note.txt，写入下面这段**虚构**测试资料：

```text
仅用于合成测试，不是真实公司披露或投资判断。
公司关键词：天赐材料
产品关键词：六氟磷酸锂、电解液、锂电材料
研究问题：周期反弹还是长期成长？
待验证假设：价格回升可能反映周期，而非持续成长。
发布日期：未知。验证状态：未验证。
```

然后发送：

```text
$investment-research-workbench 只用本地证据检查我的未处理文件
```

预期：能找到正文，说明来源日期未知、未经验证，报告相关性和建议归档位置，
原件保持不变。建立索引不等于已经批准或移动资料。

## 4. 研究并生成完整 context pack

依次发送：

```text
$investment-research-workbench 仅用本地测试证据研究天赐材料
$investment-research-workbench 为天赐材料生成 context pack，重点判断周期反弹还是长期成长
```

预期：识别合成测试资料，指出公司/行业 memo 与最新数据缺失，不编造财务数字。
context_packs/ 中出现有日期的完整 _context_pack.md，包含路径/位置引用、
不确定性、bear case 和具体问题。脚本生成的 _evidence.md 只是中间骨架。

## 5. 检查正式写入关卡

发送：

```text
$investment-research-workbench 仅基于这份合成测试，为天赐材料提出新公司 memo 的修改提案，暂不应用
```

预期：proposed_updates/ 出现具体提案，companies/ 和 watchlist.md 不会悄悄增加
投资结论或评级。阅读提案。如果确实同意这份具体修改，再发送：

```text
应用刚才展示的 proposed update，仅写入公司 memo。标记为合成测试，保留历史，不修改我的投资哲学和 watchlist。
```

预期：只修改授权记录，提案记录实际应用情况。已有观点变化时保留原判断、新判断、
日期和原因。你也可以要求修改提案，而不是批准；不同意的内容不要批准。

## 6. 换 chat 测试

在同一个测试项目新开 Codex chat：

```text
$investment-research-workbench continue this investment research project
```

预期：读取项目文件，总结当前状态和未完成事项，识别测试 memo、提案和 inbox，
不再次初始化，也不需要你粘贴上一段聊天记录。

## 7. 直接检查检索（可选）

下面命令在**初始化后的测试项目终端**运行，不是在插件仓库运行：

```bash
python scripts/rag_build_index.py
python scripts/rag_search.py --query "天赐材料 六氟磷酸锂 周期" --top-k 10 --json
python scripts/rag_generate_context.py --company "天赐材料" --query "周期反弹还是长期成长"
```

预期：结果引用 inbox_unprocessed/sample-note.txt，source_zone 为 unprocessed，
verified 为 false。部分系统需改用 python3。
如果从插件 checkout 检查项目结构，运行：

```bash
python plugins/investment-research-workbench/skills/investment-research-workbench/scripts/validate_project.py --target ../investment-workbench-test --json
```

例子假设测试文件夹与插件 checkout 是同级；不是同级时替换 --target 为实际路径。

## 8. 运行自动化测试（开发者检查）

在有 tests/ 和 tools/ 的**插件仓库根目录**打开终端：

```bash
python -m unittest discover -s tests -v
```

测试使用临时合成项目。没有 parser 时跳过 PDF/XLSX 测试；
操作系统不允许创建符号链接时，相应测试可能跳过。
需要完整测试与分发校验时，可在你选择的环境安装：

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -r plugins/investment-research-workbench/skills/investment-research-workbench/assets/project_scaffold/requirements-optional.txt
python tools/validate_distribution.py
python -m unittest discover -s tests -v
python tools/release_scan.py
```

普通用户试用不必安装开发依赖。测试覆盖原件保护、中英文检索、增量更新、
删除残留 chunk、解析失败、引用和 CLI 行为，不调用宿主模型。

[GitHub Actions](https://github.com/EastsCloud/investment-agent-skill/actions) 在 push
和 pull request 后执行检查。打开一次 run，选择 Ubuntu/Windows，再打开失败步骤看输出。
绿色只说明该次代码/打包检查通过，不代表投资分析正确。

## 常见问题

| 现象 | 下一步 |
| --- | --- |
| 找不到 Skill | 确认安装成功并新开 chat，或用独立 Skill 安装方式 |
| 初始化报告冲突 | 对比模板；已有文件已经保留 |
| 索引缺失/过期 | 在测试项目运行 rag_build_index.py |
| 缺 parser / 需要 OCR | 首次试用先用 TXT，再选择安装 parser 或导出资料 |
| Windows 代码测试临时目录权限不足 | 在正常终端使用可写临时目录重试，不放松原件保护规则 |
| 只生成 _evidence.md | 要求 Codex 按 Skill 流程完成真正的 context pack |
| 未批准就改了正式记录 | 视为手动试用失败，保留 prompt 和文件 diff 报告问题 |

报告问题时记录请求、修改了哪些文件和结果，只分享合成样本。
私人测试项目不要放进公共插件仓库。
