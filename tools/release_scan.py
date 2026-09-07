"""Check publishable tracked/untracked files; report paths, never secret values."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    result = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                            cwd=ROOT, check=True, capture_output=True)
    names = sorted(set(n.decode("utf-8") for n in result.stdout.split(b"\0") if n))
    patterns = {
        "private key": r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----",
        "API token": r"(?:sk-[A-Za-z0-9_-]{24,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})",
        "AWS access key": r"AKIA[A-Z0-9]{16}",
        "developer absolute path": r"(?:\b[A-Za-z]:[\\/][^\\/\s]+[\\/]|/(?:Users|home)/[^/\s]+/)",
        "credential assignment": r'''(?i)(?:api_key|password|secret|token)\s*[:=]\s*["'][A-Za-z0-9_+/=-]{20,}["']''',
    }
    failures = []
    for name in names:
        path = ROOT / name
        if path.is_symlink():
            failures.append((name, "publishable symlink"))
            continue
        if path.suffix.lower() in {".sqlite3", ".db", ".pyc", ".pdf", ".docx", ".xlsx"} or any(
            p in {"__pycache__", "inbox_unprocessed", "extracted_text", "sample-investment-project", ".venv"} for p in path.relative_to(ROOT).parts
        ):
            failures.append((name, "generated/private artifact"))
            continue
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            failures.append((name, "unexpected binary"))
            continue
        for label, pattern in patterns.items():
            if re.search(pattern, text):
                failures.append((name, label))
    for path, reason in failures:
        print(f"FAIL {path}: {reason}")
    print(f"Release scan: {len(names)} publishable files; {len(failures)} findings.")
    print("Heuristic scan only. Also review source, fixtures and staged diff for private investment information.")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
