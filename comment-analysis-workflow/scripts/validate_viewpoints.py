#!/usr/bin/env python3
"""Validate an aspect-level viewpoint CSV for comment analysis work."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


REQUIRED_COLUMNS = {
    "comment_id",
    "original_text",
    "aspect",
    "opinion",
    "sentiment",
    "evidence",
    "business_action",
}

ALLOWED_SENTIMENTS = {"positive", "negative", "neutral", "mixed"}


def validate(path: Path) -> dict:
    issues = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_COLUMNS - fieldnames)
        if missing:
            issues.append(
                {
                    "row": None,
                    "issue": "missing_required_columns",
                    "detail": ", ".join(missing),
                }
            )
            return {"rows_checked": 0, "issues": issues}

        rows_checked = 0
        for line_number, row in enumerate(reader, start=2):
            rows_checked += 1
            for column in REQUIRED_COLUMNS:
                if not (row.get(column) or "").strip():
                    issues.append(
                        {
                            "row": line_number,
                            "issue": "blank_required_field",
                            "detail": column,
                        }
                    )

            sentiment = (row.get("sentiment") or "").strip().lower()
            if sentiment and sentiment not in ALLOWED_SENTIMENTS:
                issues.append(
                    {
                        "row": line_number,
                        "issue": "invalid_sentiment",
                        "detail": sentiment,
                    }
                )

            evidence = (row.get("evidence") or "").strip()
            original_text = (row.get("original_text") or "").strip()
            if evidence and original_text and evidence.lower() not in original_text.lower():
                issues.append(
                    {
                        "row": line_number,
                        "issue": "evidence_not_found_in_original_text",
                        "detail": evidence[:120],
                    }
                )

            numerator = (row.get("numerator") or "").strip()
            denominator = (row.get("denominator") or "").strip()
            if numerator and not denominator:
                issues.append(
                    {
                        "row": line_number,
                        "issue": "numerator_without_denominator",
                        "detail": numerator,
                    }
                )

    return {"rows_checked": rows_checked, "issues": issues}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Path to viewpoint CSV")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    args = parser.parse_args()

    result = validate(args.csv_path)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"Rows checked: {result['rows_checked']}")
    if not result["issues"]:
        print("No issues found.")
        return
    print(f"Issues found: {len(result['issues'])}")
    for issue in result["issues"]:
        print(f"- row {issue['row']}: {issue['issue']} ({issue['detail']})")


if __name__ == "__main__":
    main()
