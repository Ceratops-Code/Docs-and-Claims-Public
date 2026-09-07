"""Validate the public site and save diagnostics outside the source checkout.

Usage: python scripts/validate-repository.py --evidence-file PATH
The caller owns the evidence file and removes it after inspection; CI removes it
with the temporary runner. The HTML check remains owned by validate-pages.mjs.
"""

import argparse
import json
import subprocess
from pathlib import Path


def main() -> int:
    """Report the real HTML linter result without writing into the publication tree."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-file", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    evidence = args.evidence_file.resolve()
    if evidence.is_relative_to(root):
        parser.error("The evidence file must be outside the source checkout.")
    try:
        result = subprocess.run(
            ["node", "scripts/validate-pages.mjs"],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=240,
            check=False,
        )
        report = {"exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    except (OSError, subprocess.TimeoutExpired) as error:
        report = {"exit_code": 1, "error": str(error)}
    evidence.parent.mkdir(parents=True, exist_ok=True)
    evidence.write_text(
        json.dumps({"schema": "public-pages-validation.v1", "html": report}, indent=2) + "\n",
        encoding="utf-8",
    )
    if report["exit_code"]:
        print("Validation failed; see the requested evidence file.")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
