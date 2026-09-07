# 验证记录 — 0.1.0

[English (primary)](VALIDATION.md) · 简体中文

检查日期：2026-09-07。

## 官方格式校验

- 使用内置 OpenAI skill-creator 初始化和 quick_validate.py：通过。
- 使用内置 plugin-creator 脚手架和 validate_plugin.py，包含最终三个默认 prompt：通过。
- 使用 openai/skills 固定提交
  `49f948faa9258a0c61caceaf225e179651397431` 的公开 Skill validator：通过。
- 核对 marketplace add/upgrade、plugin add/remove 的本机 CLI 帮助。
- 阅读 [Build skills](https://learn.chatgpt.com/docs/build-skills) 和
  [Package your plugin](https://developers.openai.com/plugins/build/plugins)。
- 内置 skill-installer 支持 GitHub Skill 子目录 URL。

不假设 GitHub Actions 可取得官方 Plugin validator。
CI 运行明确标注的自有可移植检查；发布时在 Codex 中运行真实 plugin-creator validator。
二者是不同检查。

## 实际安装与已安装包测试

在隔离 Codex 配置中运行：

```text
codex plugin marketplace add <repository-root> --json
codex plugin add investment-research-workbench@personal --json
```

CLI 报告 0.1.0 安装成功。使用**已安装副本**初始化独立项目，添加合成中文资料，
执行建立索引、中文搜索、context evidence 生成和项目校验，全部成功。
项目结构有效，索引新鲜，无解析错误。隔离配置和测试项目不随仓库发布。
首次 push 后还实际验证了从 GitHub marketplace 安装。

这些证明本地/远程 marketplace 安装和可执行包行为，不证明所有 Codex 界面的可用性，
也不代表进入 OpenAI 公共目录。触发描述和权限规则经过审阅；未执行宿主模型的行为
评估，也未测试真实投资决策。实际 prompt 行为请按 [手动指南](docs/TESTING.zh-CN.md) 试用。

## 行为回归测试

本机 Windows、Python 3.13.5，已有 pypdf/openpyxl。
26 项：**25 通过、1 跳过**；跳过项需要操作系统创建符号链接的权限。

覆盖初始化、保留自定义内容、目录冲突、中英文正文检索、三区来源、原件 hash 不变、
增量/重建、相同 mtime 的内容变更、删除/解析失败资料的旧 chunk 清除、损坏索引、
不可访问目录不误删索引、缺 parser、DOCX/XLSX/PDF/CSV 位置、扫描 PDF 诊断、
过期 CLI 拒绝、Unicode/空格路径、有限且带引用的 context、输出重名保护。

Windows 受限沙箱里的 TemporaryDirectory 因 ACL 行为创建失败；
相同测试在正常临时目录权限下通过，没有削弱产品保护规则。
GitHub Actions 使用 Ubuntu/Windows、Python 3.14，先测标准库模式，再测可选解析器。
首次发布的 [CI](https://github.com/EastsCloud/investment-agent-skill/actions/runs/34089086631)
两个平台均通过。后续修改以对应提交的 Actions 结果为准。

## 发布检查

可移植分发校验与 Python 编译通过。扫描可发布 tracked/untracked 文件中的 key 模式、
凭据赋值、开发机绝对路径和生成/私人文件类型，首次发布为零发现。
人工审阅确认仅通用模板和合成数据，没有个人持仓或公司结论。
原需求文本和本地验证 checkout 在仓库外，不打包第三方实现，使用 MIT License。

启发式扫描不能证明所有未来改动都无 secret。以后每次发布需重新校验并审阅 staged diff。

## 双语文档维护

本次将首页改为英文主版本，并同步中文首页、prompt 导航、手动测试指南、
验证记录、references 和项目模板。唯一运行入口仍为英文 SKILL.md。
语言配对规则见 [CONTRIBUTING.md](CONTRIBUTING.md)；不声称已实现自动语义翻译检查。
