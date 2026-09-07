# Contributing / 贡献指南

English is primary. Maintain the Chinese counterpart in the same change.

- Update README.md and README.zh-CN.md together.
- Update docs/PROMPTS.md and docs/PROMPTS.zh-CN.md together.
- Update docs/TESTING.md and docs/TESTING.zh-CN.md together.
- Update VALIDATION.md and VALIDATION.zh-CN.md together when recording new results.
- Keep bundled references and project templates bilingual, English first. Preserve identical
  authorization boundaries, supported formats, commands and limitations in both languages.
- SKILL.md is the single English runtime entrypoint. Its Chinese companion is
  references/skill-guide.zh-CN.md; update that explanation when the entrypoint changes.
  Do not create a second translated Skill with another SKILL.md.
- Keep path names, CLI flags and identifiers unchanged. Translated descriptions may differ in
  wording, but examples and expected behavior must agree. Review semantics, not just file existence.
- A documentation change is incomplete when only one language reflects the new behavior.
  This is a contributor review rule, not a claim of automatic translation or semantic validation.
- Do not add real research, holdings, secrets or generated caches. Validate distribution and run
  the release scan. For changed code/scaffolding, also run the relevant behavioral tests.
- For manual Skill changes, follow the testing guide; code tests do not test model obedience.

## 中文

英文是主版本，同一次修改里维护中文对应内容。

- README、PROMPTS、TESTING、VALIDATION 都有中英文配对文件，需要同步更新。
- bundled references 和项目模板采用英文在前、中文在后，保持授权边界、格式、
  命令和已知限制一致。
- SKILL.md 是唯一英文运行入口；同步维护 references/skill-guide.zh-CN.md 中文说明，
  不创建第二个包含 SKILL.md 的翻译 Skill。
- 路径、CLI 参数、标识符不翻译；示例和预期行为要一致，审阅实际语义。
- 只更新一种语言不算完成。这是贡献审阅规则，不代表已实现自动翻译或语义校验。
- 不提交真实研究、持仓、secret 或缓存；执行分发校验和发布扫描。
  修改代码/scaffold 时还需运行相应行为测试。
- prompt 行为按手动测试指南试用；代码测试不证明模型会遵守指令。
