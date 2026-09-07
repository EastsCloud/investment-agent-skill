# Validation record — 0.1.0

Checked on 2026-09-07.

## Official format checks

- Used the installed OpenAI skill-creator initializer and quick_validate.py: passed.
- Used the installed OpenAI plugin-creator scaffold and validate_plugin.py: passed
  after final manifest edits (including the three default prompts).
- Also ran the public OpenAI Skill validator from openai/skills commit
  `49f948faa9258a0c61caceaf225e179651397431`: passed.
- Verified CLI help for marketplace add/upgrade, plugin add and plugin remove.
- Reviewed [Build skills](https://learn.chatgpt.com/docs/build-skills) and
  [Package your plugin](https://developers.openai.com/plugins/build/plugins).
- GitHub subdirectory URL installation is supported by the installed skill-installer.

The public official Plugin validator is not assumed available to GitHub Actions.
CI runs our explicitly labeled portable distribution checks; release validation
uses the actual plugin-creator validator in Codex. These are different checks.

## Real installation and installed-package smoke

In an isolated Codex profile, successfully ran:

```text
codex plugin marketplace add <repository-root> --json
codex plugin add investment-research-workbench@personal --json
```

The CLI reported plugin version 0.1.0 installed. Using the **installed copy**, initialized
a separate sample workspace, inserted synthetic Chinese evidence, ran index build,
Chinese search, context evidence generation and project validation. All succeeded.
Validation reported valid structure, a fresh index and zero parse errors.
Neither this profile nor the generated sample project is shipped in the repository.

This proves local marketplace ingestion and executable package behavior, not universal
availability on every Codex surface or automatic inclusion in OpenAI's public directory.
Trigger wording and authority rules were reviewed; no hosted-model behavioral evaluation
or live investment decision test was run.

## Behavioral regression tests

Local platform: Windows, Python 3.13.5, installed pypdf and openpyxl.

26 tests: **25 passed, 1 skipped**. The skipped test needs OS symlink creation privileges.
Coverage includes initialization, preserving custom content, directory conflicts,
English and Chinese body retrieval, all three source zones, input hashes unchanged,
incremental/rebuild operation, same-mtime content changes, deleted and failed-source
chunk removal, corrupt indexes, unreadable-directory preservation, optional parser absence,
DOCX/XLSX/PDF and CSV locations, scanned-PDF diagnostics, stale CLI refusal,
Unicode/spaced paths, bounded cited context and output collision protection.

TemporaryDirectory creation under the restricted Windows sandbox failed because of
Windows ACL behavior. The identical suite passed with normal temporary-directory access;
no product code was weakened to work around that environment.

GitHub Actions is configured for Ubuntu and Windows with Python 3.14, first without
optional parsers and then with them. Remote CI status is visible on the repository's
Actions tab; a configured matrix alone is not a claim that remote jobs have passed.

## Publication checks

Portable distribution validation and Python compilation passed.
The release scanner checks publishable tracked/untracked files for key patterns,
credential assignments, developer absolute paths and generated/private file types.
The pre-publication scan returned zero findings. A manual review confirmed generic
templates, synthetic tests and no authored portfolio, holdings or company conclusions.
The original user request files and local helper checkouts remain outside this repo.
No third-party implementation code is bundled; MIT license applies to this repository.

Heuristic scanning is not proof that arbitrary future changes contain no secrets.
Run validation and review the staged diff before each later release.
