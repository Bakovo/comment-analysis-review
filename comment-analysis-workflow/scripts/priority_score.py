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
        for row in reader:
            aspect = (row.get("aspect") or "").strip()
            if not aspect:
                continue
            sentiment = (row.get("sentiment") or "").strip().lower()
            engagement = parse_number(row.get("engagement_count"))
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Path to viewpoint CSV")
    args = parser.parse_args()

    rows = summarize(args.csv_path)
    fieldnames = [
        "aspect",
        "mention_count",
        "negative_count",
        "negative_rate",
        "engagement_sum",
        "negative_engagement_sum",
        "priority_score",
    ]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)


if __name__ == "__main__":
    main()
