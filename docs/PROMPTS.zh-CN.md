# Prompt 与指令文件

[English (primary)](PROMPTS.md) · 简体中文 · [首页](../README.zh-CN.md)

## 先看核心 prompt

[SKILL.md](../plugins/investment-research-workbench/skills/investment-research-workbench/SKILL.md)
就是主要的可复用 prompt。YAML name/description 让 Codex 发现和选择 Skill；
Markdown 正文规定工作方式、读取哪些文件、调用哪些脚本以及正式写入何时需要授权。
每次使用时不需要把整个文件手动粘贴。

## 指令地图

下面的文件都位于 [Skill 目录](../plugins/investment-research-workbench/skills/investment-research-workbench/)。

| 文件 | 作用 | 什么时候改 |
| --- | --- | --- |
| [SKILL.md](../plugins/investment-research-workbench/skills/investment-research-workbench/SKILL.md) | 核心指令与工作流路由 | 改变所有安装用户的 Skill 行为 |
| [references/project-model.md](../plugins/investment-research-workbench/skills/investment-research-workbench/references/project-model.md) | 项目结构、初始化与迁移 | 改变项目模型 |
| [references/research-workflow.md](../plugins/investment-research-workbench/skills/investment-research-workbench/references/research-workflow.md) | 研究、inbox、接续、context、周复盘 | 调整具体工作流 |
| [references/safety-and-write-policy.md](../plugins/investment-research-workbench/skills/investment-research-workbench/references/safety-and-write-policy.md) | 正式写入授权和证据边界 | 调整审阅与应用规则 |
| [references/rag-spec.md](../plugins/investment-research-workbench/skills/investment-research-workbench/references/rag-spec.md) | 本地检索接口与故障处理 | 调整模型如何使用检索 |
| [assets/project_scaffold/AGENTS.md](../plugins/investment-research-workbench/skills/investment-research-workbench/assets/project_scaffold/AGENTS.md) | 复制到用户目录的长期项目指令 | 改未来新项目的默认规则 |
| [agents/openai.yaml](../plugins/investment-research-workbench/skills/investment-research-workbench/agents/openai.yaml) | Skill 显示名称与默认提示语 | 改发现与界面文案 |

Plugin manifest 的 interface.defaultPrompt 只是几个聊天起始示例，不能替代主指令。
scripts 执行确定性的文件与索引操作，tests 检验这些代码。

## 发送请求后会发生什么？

1. 你说“研究这家公司”，或明确调用 $investment-research-workbench。
2. Codex 读取 SKILL.md 和对应 reference。
3. 读取**私人项目**中的 AGENTS.md、投资哲学、checklist、复盘、watchlist 和 memo。
4. 调用本地检索，结合带来源的证据分析。
5. 生成报告、context pack 或提案；只有在用户授权范围内才改正式观点。

这些文件共同构成 prompt 系统，不需要另设 prompt.txt。

## 我应该改哪个 prompt？

- 定制自己的研究方法：修改**私人项目里**的 AGENTS.md 和 investment_philosophy.md，
  或明确让 Codex 修改。真实投资原则保存在这里。
- 改进公共 Skill：修改 SKILL.md 或对应 reference，同步中文，校验并重新安装。
- 修改 scaffold 只影响**以后**的初始化，不会覆盖已有私人文件。
- 新功能的代码写在 scripts；不能仅用 prompt 声称尚未实现的能力存在。

## 可直接发送的示例

下面发到 **Codex 聊天框**，不要发到终端。

```text
$investment-research-workbench 初始化当前文件夹
$investment-research-workbench 检查并整理我的未处理资料
$investment-research-workbench 仅根据本地证据研究天赐材料，指出缺失信息
$investment-research-workbench 为天赐材料生成 context pack，重点判断周期反弹还是长期成长
$investment-research-workbench 审阅最新 ChatGPT 分析并提出修改建议
$investment-research-workbench 继续这个投资研究项目
```

测试指南还提供了提案审批和换 chat 接续的操作。
