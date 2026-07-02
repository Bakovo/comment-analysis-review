#!/usr/bin/env python3
"""Summarize aspect-level viewpoint rows into priority metrics for comment analysis.

The default priority score is a heuristic:

    negative_count * 0.5
    + negative_rate * 30
    + negative_engagement_sum * 0.02

Adjust these weights for the category, decision cost, and business context.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

from field_aliases import (
    CHINESE_PRIORITY_FIELDS,
    map_priority_output,
    normalize_sentiment,
    resolve_columns,
    row_value,
    uses_chinese_fields,
)


ENGLISH_PRIORITY_FIELDS = [
    "aspect",
    "mention_count",
    "negative_count",
    "negative_rate",
    "engagement_sum",
    "negative_engagement_sum",
    "priority_score",
]


def parse_number(value: str | None) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def summarize(path: Path) -> list[dict]:
    summary = defaultdict(
        lambda: {
            "aspect": "",
            "mention_count": 0,
            "negative_count": 0,
            "engagement_sum": 0.0,
            "negative_engagement_sum": 0.0,
        }
    )

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        resolved = resolve_columns(reader.fieldnames)
        for row in reader:
            aspect = row_value(row, "aspect", resolved).strip()
            if not aspect:
                continue
            sentiment = normalize_sentiment(row_value(row, "sentiment", resolved))
            engagement = parse_number(row_value(row, "engagement_count", resolved))
            item = summary[aspect]
            item["aspect"] = aspect
            item["mention_count"] += 1
            item["engagement_sum"] += engagement
            if sentiment == "negative":
                item["negative_count"] += 1
                item["negative_engagement_sum"] += engagement

    rows = []
    for item in summary.values():
        mentions = item["mention_count"]
        negative_rate = item["negative_count"] / mentions if mentions else 0
        priority_score = (
            item["negative_count"] * 0.5
            + negative_rate * 30
            + item["negative_engagement_sum"] * 0.02
        )
        rows.append(
            {
                "aspect": item["aspect"],
                "mention_count": mentions,
                "negative_count": item["negative_count"],
                "negative_rate": f"{negative_rate:.4f}",
                "engagement_sum": f"{item['engagement_sum']:.2f}",
                "negative_engagement_sum": f"{item['negative_engagement_sum']:.2f}",
                "priority_score": f"{priority_score:.2f}",
            }
        )
    return sorted(rows, key=lambda r: float(r["priority_score"]), reverse=True)


def detect_output_language(path: Path, requested: str) -> str:
    if requested != "auto":
        return requested
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return "zh" if uses_chinese_fields(reader.fieldnames) else "en"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Path to viewpoint CSV")
    parser.add_argument(
        "--output-language",
        choices=("auto", "en", "zh"),
        default="auto",
        help="Output CSV header language. Defaults to input header language.",
    )
    args = parser.parse_args()

    rows = summarize(args.csv_path)
    output_language = detect_output_language(args.csv_path, args.output_language)
    fieldnames = (
        list(CHINESE_PRIORITY_FIELDS.values())
        if output_language == "zh"
        else ENGLISH_PRIORITY_FIELDS
    )
    output_rows = [map_priority_output(row, output_language) for row in rows]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", newline="")
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(output_rows)


if __name__ == "__main__":
    main()
