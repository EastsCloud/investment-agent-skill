# Try and test the workbench

English (primary) · [简体中文](TESTING.zh-CN.md) · [Home](../README.md)

There are two different checks: a manual Codex session tests the **prompt/workflow**, while the
automated suite tests the **Python tools**. Passing code tests alone does not prove model behavior.

## 1. Install or update

Follow [installation](../README.md#installation). If already installed from this repository:

```bash
codex plugin marketplace upgrade personal
codex plugin add investment-research-workbench@personal
```

Use these only for this repository's personal marketplace; see the naming-conflict note in the README.
Open a new Codex chat/session after installation. For local development, add the checkout as a local
marketplace, reinstall after edits and start a new chat. Do not install both standalone and plugin copies.

## 2. Initialize a separate sandbox project

Create an empty folder named investment-workbench-test **outside the plugin checkout**, and open it
as a Codex project. Send in chat:

```text
$investment-research-workbench initialize this folder
```

Expected: AGENTS.md, investment_philosophy.md, checklist.md, watchlist.md, memo templates, inbox,
companies/sectors, context/proposal directories and scripts exist. No holdings or company opinions
have been inserted. Append “Synthetic test preference: ask for evidence dates.” to the philosophy
yourself, then send the initialization request again. Expected: the text survives; differences are
reported without replacing your file.

## 3. Add synthetic evidence

Create inbox_unprocessed/sample-note.txt yourself, with this **invented** test content:

```text
Synthetic testing only. This is not a real company statement or investment claim.
Company keyword: 天赐材料
Product keywords: 六氟磷酸锂, 电解液, 锂电材料
Research question: 周期反弹还是长期成长？
Assumption to test: price recovery might reflect a cycle rather than durable growth.
Publication date: unknown. Verification status: unverified.
```

Then send:

```text
$investment-research-workbench review my unprocessed files using only local evidence
```

Expected: Codex finds the body text, identifies the source/date as unknown/unverified, reports
relevance and an archive suggestion, and preserves the original file. Indexing does not mean
the file has been approved or moved.

## 4. Research and generate a finished context pack

Send:

```text
$investment-research-workbench research 天赐材料 using only my local test evidence
$investment-research-workbench generate a context pack for 天赐材料 focused on cyclical rebound vs long-term growth
```

Expected: the reply treats the fixture as synthetic, identifies missing company/sector memos and
current data, and invents no financial numbers. A **finished** dated _context_pack.md appears,
including cited paths/locations, uncertainty, bear case and specific questions.
The script-generated _evidence.md is only an intermediate skeleton.

## 5. Exercise the formal write gate

Send:

```text
$investment-research-workbench propose a new company memo for 天赐材料 based only on this synthetic test; do not apply it yet
```

Expected: a concrete proposal appears under proposed_updates/; companies/ and watchlist.md do not
silently gain a thesis or rating. Read it. If you want to apply that exact proposal, send:

```text
Apply the proposed update you just showed me, only to the company memo. Label it synthetic testing, preserve history, and leave my philosophy and watchlist unchanged.
```

Expected: only the authorized record changes, and the proposal records what was applied.
For existing views, old/new judgments, date and reason must remain visible.
You can also ask for a revision rather than approval; do not approve a proposal you disagree with.

## 6. Test a new chat

Start a new Codex chat in the same test project:

```text
$investment-research-workbench continue this investment research project
```

Expected: it reads project files, summarizes current state and pending work, recognizes the test
memo/proposals/inbox and does not initialize again. It should not need the previous chat transcript.

## 7. Inspect retrieval directly (optional)

These commands go in a **terminal in the initialized test project**, not the plugin repository:

```bash
python scripts/rag_build_index.py
python scripts/rag_search.py --query "天赐材料 六氟磷酸锂 周期" --top-k 10 --json
python scripts/rag_generate_context.py --company "天赐材料" --query "周期反弹还是长期成长"
```

Expect citations to inbox_unprocessed/sample-note.txt and source_zone unprocessed, with verified false.
Use python3 where appropriate. To check the project structure from a plugin checkout, run:

```bash
python plugins/investment-research-workbench/skills/investment-research-workbench/scripts/validate_project.py --target ../investment-workbench-test --json
```

That example assumes your test folder is a sibling of the checkout; otherwise replace --target with its path.

## 8. Run the automated suite (developer check)

Open a terminal in the **plugin repository**, where tests/ and tools/ live:

```bash
python -m unittest discover -s tests -v
```

This uses synthetic temporary projects. PDF/XLSX tests skip if parsers are missing, and an OS without
symlink privileges can skip that one test. For the full suite and distribution checks, install
development packages in an environment you choose:

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -r plugins/investment-research-workbench/skills/investment-research-workbench/assets/project_scaffold/requirements-optional.txt
python tools/validate_distribution.py
python -m unittest discover -s tests -v
python tools/release_scan.py
```

Installing packages is optional for end-user trials. The suite verifies preservation, Chinese/English
retrieval, incremental updates, ghost removal, parser failures, citations and CLI behavior.
It does not invoke a hosted model.

[GitHub Actions](https://github.com/EastsCloud/investment-agent-skill/actions) runs the configured
checks after pushes and pull requests. Open a run, choose Ubuntu/Windows, then open a failed step
to see its output. Green CI means those code/package checks passed, not that investment analysis is correct.

## Troubleshooting

| Symptom | Next step |
| --- | --- |
| Skill not found | Confirm plugin installation, start a new chat, or use the standalone installer |
| File conflict during initialization | Compare templates; your files were preserved |
| Index missing/stale | Run rag_build_index.py in the test project |
| Parser missing / OCR required | Use TXT for the first trial; optionally install a parser or export the document |
| Windows temporary-directory access denied in code tests | Retry from a normal terminal with writable temporary storage; do not weaken data-preservation rules |
| Only _evidence.md created | Ask Codex to complete the actual context pack using the Skill workflow |
| Formal record changed without your approval | Treat the manual trial as failed; keep the file diff and prompt to report a bug |

Record what you asked, which artifacts changed and the result when reporting a problem. Share only
synthetic examples. Keep the private test project out of the public plugin repository.
