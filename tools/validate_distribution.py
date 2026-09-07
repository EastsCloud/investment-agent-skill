"""Portable contract checks; not a replacement for official Codex validators."""
import ast
import json
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = "investment-research-workbench"
PLUGIN = ROOT / "plugins" / NAME
SKILL = PLUGIN / "skills" / NAME


def validate():
    manifest = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    assert manifest["name"] == NAME
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][a-zA-Z0-9.-]+)?", manifest["version"])
    assert manifest["skills"] == "./skills/"
    assert not ({"apps", "mcpServers", "hooks"} & manifest.keys()), "Expected a skill-only plugin"
    for name in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        assert manifest["interface"][name].strip()
    prompts = manifest["interface"]["defaultPrompt"]
    assert isinstance(prompts, list) and 1 <= len(prompts) <= 3
    assert all(isinstance(p, str) and 0 < len(p) <= 128 for p in prompts)
    market = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    assert re.fullmatch(r"[A-Za-z0-9_-]+", market["name"])
    assert len(market["plugins"]) == 1
    entry = market["plugins"][0]
    assert entry["name"] == NAME and entry["source"]["source"] == "local"
    assert (ROOT / entry["source"]["path"]).resolve() == PLUGIN.resolve()
    assert entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    assert entry["category"] == "Productivity"
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    front = yaml.safe_load(text.split("---", 2)[1])
    assert set(front) == {"name", "description"}
    assert front["name"] == NAME and 0 < len(front["description"]) < 1024
    assert len(text.splitlines()) < 150, "Keep entrypoint concise"
    assert "[TODO" not in text
    for relative in re.findall(r"\]\((references/[^)]+)\)", text):
        assert (SKILL / relative).is_file(), relative
    ui = yaml.safe_load((SKILL / "agents/openai.yaml").read_text(encoding="utf-8"))
    assert 25 <= len(ui["interface"]["short_description"]) <= 64
    assert "$" + NAME in ui["interface"]["default_prompt"]
    assert ui.get("policy", {}).get("allow_implicit_invocation", True)
    for path in SKILL.rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    assert (ROOT / "LICENSE").read_bytes() == (PLUGIN / "LICENSE.txt").read_bytes()
    assert not list(SKILL.glob("README*")), "Do not duplicate repo installation docs in the skill root"
    print("Portable distribution checks passed (manifest, marketplace, frontmatter, UI, references, Python, license).")


if __name__ == "__main__":
    validate()
