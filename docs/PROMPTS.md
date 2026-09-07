# Prompts and instruction files

English (primary) · [简体中文](PROMPTS.zh-CN.md) · [Home](../README.md)

## Start with the main prompt

[SKILL.md](../plugins/investment-research-workbench/skills/investment-research-workbench/SKILL.md)
is the main reusable prompt. Its YAML name/description makes the Skill discoverable; its Markdown
body tells Codex how to operate, what to read, which scripts to call and when formal updates require
authorization. You do not paste this entire file each time.

## Instruction map

All paths below are inside the [Skill directory](../plugins/investment-research-workbench/skills/investment-research-workbench/).

| File | Role | When to change it |
| --- | --- | --- |
| [SKILL.md](../plugins/investment-research-workbench/skills/investment-research-workbench/SKILL.md) | Main instructions and workflow routing | Change behavior for every installed user |
| [references/project-model.md](../plugins/investment-research-workbench/skills/investment-research-workbench/references/project-model.md) | Project layout, initialization and migration rules | Change the project model |
| [references/research-workflow.md](../plugins/investment-research-workbench/skills/investment-research-workbench/references/research-workflow.md) | Research, inbox, continuation, context and weekly workflows | Change a particular workflow |
| [references/safety-and-write-policy.md](../plugins/investment-research-workbench/skills/investment-research-workbench/references/safety-and-write-policy.md) | Formal write authorization and evidence boundaries | Change review/application rules |
| [references/rag-spec.md](../plugins/investment-research-workbench/skills/investment-research-workbench/references/rag-spec.md) | Local retrieval contract and recovery | Change how the agent uses retrieval |
| [assets/project_scaffold/AGENTS.md](../plugins/investment-research-workbench/skills/investment-research-workbench/assets/project_scaffold/AGENTS.md) | Persistent project instructions copied to the user's folder | Change defaults for future projects |
| [agents/openai.yaml](../plugins/investment-research-workbench/skills/investment-research-workbench/agents/openai.yaml) | Skill UI label and suggested starting prompt | Change discovery/UI wording |

The plugin manifest's interface.defaultPrompt contains a few suggested chat starters. It does not
replace the main instructions. Scripts perform deterministic file/index operations; tests verify them.

## What happens when you send a request?

1. You send “research this company” or explicitly invoke $investment-research-workbench.
2. Codex loads SKILL.md and the relevant reference.
3. It reads the **private project's** AGENTS.md, philosophy, checklist, lessons, watchlist and memos.
4. It calls local retrieval tools and reasons over cited evidence.
5. It creates a report/context pack/proposal; it changes formal views only within user authorization.

These files form the prompt system. There is no required standalone prompt.txt.

## Which prompt should I edit?

- To customize your own research process: edit AGENTS.md and investment_philosophy.md **in your private
  project**, or explicitly ask Codex to change them. Your actual investment principles belong there.
- To improve the public Skill: edit its SKILL.md or appropriate reference, update the Chinese
  counterpart, validate and reinstall.
- Editing the scaffold changes **future** initializations. Existing private files are not overwritten.
- Keep code changes in scripts; instructions should not pretend that a new feature exists before it does.

## Copy-and-send examples

These go into **Codex chat**, not a terminal.

```text
$investment-research-workbench initialize this folder
$investment-research-workbench review my unprocessed files
$investment-research-workbench research 天赐材料 using only my local evidence; identify missing data
$investment-research-workbench generate a context pack for 天赐材料 focused on cyclical rebound vs long-term growth
$investment-research-workbench review the latest ChatGPT analysis and propose updates
$investment-research-workbench continue this investment research project
```

The testing guide includes prompts for reviewing a concrete proposal and checking new-chat continuity.
