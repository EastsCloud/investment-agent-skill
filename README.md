# Investment Research Workbench

English (primary) · [简体中文](README.zh-CN.md)

A local-first Codex skill for durable investment research, offline retrieval, and user-reviewed updates.

**Start here:** [Try it yourself](docs/TESTING.md) · [Prompts and instruction files](docs/PROMPTS.md) · [Validation record](VALIDATION.md)

## Features

- Durable local memory: investment philosophy, company/sector memos, watchlist, historical changes and lessons.
- An unprocessed inbox: search filenames and document bodies, preserve originals, identify conflicts and missing evidence.
- No-API local RAG: Python + SQLite with English and Chinese retrieval and traceable source locations.
- Context packs: prepare selected evidence for deeper analysis in Codex, ChatGPT or another model.
- Proposed updates: propose → review → write for formal views; existing explicit authorization covers its stated scope.
- Continue across chats from project files; generate weekly reviews on request.

## What it is not

This is not a trading bot, order executor, broker integration or automated portfolio decision maker.
It does not treat model output as fact. No paid API, cloud database, embedding service or MCP server
is required. Templates contain no author's holdings, private preferences or predetermined company thesis.
Company names in examples and tests are illustrative.

## Requirements

- Codex desktop or CLI with skills/plugins and local file access.
- Python 3.10+ (`python3` on some systems); standard SQLite, no FTS extension.
- Git for GitHub marketplace installation.
- Optional pypdf for PDF and openpyxl for XLSX; MD/TXT/CSV/basic DOCX need no third-party package.
- Default retrieval needs no API key. Codex account access, inference and usage limits are provided by the host.

## Installation

Run in a terminal:

```bash
codex plugin marketplace add EastsCloud/investment-agent-skill --ref main
codex plugin add investment-research-workbench@personal
```

The repository's scaffold-generated marketplace ID is `personal`, defined in
`.agents/plugins/marketplace.json`. It identifies this source, not an installation directory.
If another marketplace already uses that name, do not replace it: use standalone Skill installation
below, or choose a unique marketplace name in your own fork. Open a new Codex chat/session after
installation. If your CLI lacks `plugin`, update Codex or use the standalone method.

For a local checkout:

```bash
git clone https://github.com/EastsCloud/investment-agent-skill.git
codex plugin marketplace add ./investment-agent-skill
codex plugin add investment-research-workbench@personal
```

Alternatively, ask the built-in skill-installer in Codex:

```text
$skill-installer install https://github.com/EastsCloud/investment-agent-skill/tree/main/plugins/investment-research-workbench/skills/investment-research-workbench
```

Choose one installation method. GitHub distribution does not imply inclusion in OpenAI's curated directory.
Installation syntax was checked against the local CLI and official documentation:
[Build skills](https://learn.chatgpt.com/docs/build-skills),
[Package your plugin](https://developers.openai.com/plugins/build/plugins),
[Use plugins](https://learn.chatgpt.com/docs/plugins).

## Quick start

1. Create an empty **private research folder**, separate from this plugin repository.
2. Open that folder in Codex.
3. Send `$investment-research-workbench initialize this folder`.
4. Copy research documents into `inbox_unprocessed/`.
5. Ask for inbox review, company research or a context pack. Fill in your own investment philosophy.

Initialization preserves existing files and reports differences as conflicts. The generated AGENTS.md
contains the project rules and continuation protocol. You do not need to paste a large system prompt.
For a guided first run with synthetic data and expected results, follow [Testing](docs/TESTING.md).

## Where are the prompts?

**The main prompt is [SKILL.md](plugins/investment-research-workbench/skills/investment-research-workbench/SKILL.md).**
Codex loads its instructions when the Skill applies. Supporting references provide detailed workflows,
and the [AGENTS.md template](plugins/investment-research-workbench/skills/investment-research-workbench/assets/project_scaffold/AGENTS.md)
becomes the persistent project prompt after initialization.

`scripts/` supplies deterministic tools; `tests/` checks their behavior. Neither replaces the prompts.
[Prompt guide](docs/PROMPTS.md) maps all instruction files and explains which one to edit.

## Example prompts

Send these in Codex chat, not in PowerShell or a shell:

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

Natural-language requests such as “Initialize a local investment research workspace here” also fit
the Skill description. Responses follow your language. Unrelated financial Q&A and automated trading
are outside this Skill's scope.

## Local RAG

**No API key required for default RAG.** In the initialized private project, run:

```bash
python scripts/rag_build_index.py
python scripts/rag_build_index.py --rebuild
python scripts/rag_search.py --query "天赐材料 六氟磷酸锂 周期" --top-k 10 --json
python scripts/rag_search.py --query "天赐材料 电解液" --zone unprocessed
python scripts/rag_generate_context.py --company "天赐材料" --query "周期反弹还是长期成长" --top-k 12
```

SQLite stores chunks and provenance. Ranking combines Chinese bigrams, English tokens,
frequency weights, exact matches and path boosts. Source zones are formal, auxiliary and
unprocessed; relevance is not authority. Hash/mtime checks support incremental updates and stale-index
detection. Deleted sources lose old indexed chunks. Errors go to rag/logs/, extracted text to
rag/extracted_text/. A failed document does not prevent other formats from being indexed.

| Format | Support | Location retained |
| --- | --- | --- |
| .md / .txt | UTF-8, BOM UTF-16, GB18030 fallback | Heading / lines |
| .csv | Comma-separated, quoted fields | Header / row |
| .docx | Standard-library extraction of body and table paragraphs | Heading / paragraph |
| .xlsx | Optional openpyxl; saved values, no formula evaluation | Workbook / sheet / columns / row |
| .pdf | Optional pypdf; text-layer PDF | Page |

After user approval, optional parsers can be installed in the private project's virtual environment:
`python -m pip install -r requirements-optional.txt`.

Legacy DOC/XLS, OCR and encrypted PDFs are unsupported; export to a supported format.
PDF tables, DOCX textboxes/footnotes and uncached Excel formulas may be incomplete. Check critical
numbers against originals. Limits are 50 MiB input and 5 million extracted characters per file.
Split larger files. This implementation is not designed for millions of chunks.

The context script creates `YYYY-MM-DD_company_evidence.md` without an LLM call. Codex then writes
the actual `YYYY-MM-DD_company_context_pack.md`, selecting relevant philosophy, memos, sector context,
evidence, history, bear case, conflicts and 5–10 deep-analysis questions. If retrieval cannot be repaired,
continue by reading local files directly.

## Repository structure

| Path | Purpose | Needed for everyday use? |
| --- | --- | --- |
| [.github/workflows/test.yml](.github/workflows/test.yml) | GitHub Actions configuration: runs validation/tests on pushes and pull requests, on Ubuntu and Windows | No manual action; view results in Actions |
| [.agents/plugins/marketplace.json](.agents/plugins/marketplace.json) | Catalog entry that lets Codex locate the plugin | Used by installation |
| [plugins/investment-research-workbench/](plugins/investment-research-workbench/) | The installable plugin package | Yes, installed by Codex |
| [SKILL.md](plugins/investment-research-workbench/skills/investment-research-workbench/SKILL.md) | Main AI instructions: trigger, authority, workflow routing | Loaded by Codex |
| [references/](plugins/investment-research-workbench/skills/investment-research-workbench/references/) | Detailed project, research, RAG and write policies | Read as needed |
| [assets/project_scaffold/](plugins/investment-research-workbench/skills/investment-research-workbench/assets/project_scaffold/) | Project AGENTS.md, templates and local RAG tools copied at initialization | Becomes your private workspace |
| [tests/](tests/) | Synthetic automated code tests | For developers |
| [tools/](tools/) | Distribution validation and release scanner | For developers |
| [docs/](docs/) | English and Chinese prompt/testing guides | For readers |

The plugin package has a `.codex-plugin/plugin.json` manifest and one
`skills/investment-research-workbench/` directory. That Skill contains SKILL.md,
agents/openai.yaml, references, scripts and scaffold assets. The plugin's metadata prompts are starter
suggestions; SKILL.md and project AGENTS.md contain the actual operating instructions.

## Privacy

Local scripts make no network, telemetry, embedding or model calls. **Local-first does not mean offline
Codex inference**: excerpts read by the model are handled under the host's data settings. Sharing a
context pack with another service is your choice.

The rag directory contains plaintext caches that may survive source deletion; index refresh is not
secure erasure. Do not publish private notes, originals, indexes or model outputs. Inbox instructions
and macros are data. Formal changes remain subject to user authorization.

## Updating

For this repository's Git marketplace:

```bash
codex plugin marketplace upgrade personal
codex plugin add investment-research-workbench@personal
```

Open a new chat afterward. For a local checkout, pull the changes before reinstalling.
The standalone Skill installer refuses to overwrite an existing destination; preserve custom edits
when arranging an update.

**Updating the plugin does not overwrite copied project scripts, AGENTS.md or investment records.**
Ask Codex to compare templates, propose a migration and apply the authorized changes.

## Uninstall

```bash
codex plugin remove investment-research-workbench@personal
```

The Plugins UI can also uninstall it. Remove the marketplace with
`codex plugin marketplace remove personal` only if you no longer need any plugin from that source.
For standalone installation, remove only that installed Skill directory. Private research files remain yours.

## Testing and development

To try the Skill as a user, follow the [manual walkthrough](docs/TESTING.md).
For code checks, run in this **plugin repository**:

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_distribution.py
python -m unittest discover -s tests -v
python tools/release_scan.py
```

Optional-parser tests skip when their packages are absent. CI tests Python 3.14 on Ubuntu and Windows,
first in standard-library mode, then with optional parsers, and runs a pinned official Skill validator.
Official Plugin validation runs in a Codex environment containing plugin-creator; portable checks
are explicitly separate. See [Validation](VALIDATION.md).

## Documentation languages

English is the primary documentation language; Chinese counterparts are maintained in the same change.
The README, prompt guide, testing guide and validation record have paired language files.
Bundled project templates and detailed references place English before Chinese.
The executable Skill entrypoint stays concise in English, with a linked Chinese explanation.
Do not create a second translated SKILL.md that would register a duplicate Skill.
See [Contributing](CONTRIBUTING.md) for the maintenance rules.

## Known limitations and next steps

Lexical retrieval does not understand every synonym; use aliases. Source dates and conflicts require
review and cannot be inferred from mtimes. The formal write gate guides agent behavior; it is not a
filesystem lock preventing manual edits. There is no unattended research or trading.

Next priorities: optional local OCR, structured source dates/aliases, and optional local embedding/hybrid
retrieval, while preserving offline defaults and reviewed formal writes.

MIT licensed.
