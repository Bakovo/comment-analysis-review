"""Field-name helpers for bilingual comment-analysis CSV files."""

from __future__ import annotations


COLUMN_ALIASES = {
    "comment_id": ("comment_id", "评论ID"),
    "original_text": ("original_text", "原始评论", "评论原文"),
    "source": ("source", "来源", "平台", "渠道"),
    "rating": ("rating", "评分"),
    "created_at": ("created_at", "发布时间", "时间", "日期"),
    "engagement_count": ("engagement_count", "互动量", "互动数"),
    "aspect": ("aspect", "分析方面", "方面"),
    "opinion": ("opinion", "观点概括", "观点"),
    "sentiment": ("sentiment", "情绪", "情感"),
    "evidence": ("evidence", "原文证据", "证据"),
    "business_action": ("business_action", "业务动作", "行动建议", "下一步动作"),
    "confidence": ("confidence", "置信度"),
    "numerator": ("numerator", "分子"),
    "denominator": ("denominator", "分母"),
}

CHINESE_PRIORITY_FIELDS = {
    "aspect": "分析方面",
    "mention_count": "提及量",
    "negative_count": "负面量",
    "negative_rate": "负面率",
    "engagement_sum": "互动量合计",
    "negative_engagement_sum": "负面互动量",
    "priority_score": "优先级分数",
}

SENTIMENT_ALIASES = {
    "positive": "positive",
    "正面": "positive",
    "negative": "negative",
    "负面": "negative",
    "neutral": "neutral",
    "中性": "neutral",
    "mixed": "mixed",
    "混合": "mixed",
}


def resolve_columns(fieldnames: list[str] | None) -> dict[str, str]:
    lookup = {(field or "").strip(): field for field in fieldnames or []}
    resolved = {}
    for canonical, aliases in COLUMN_ALIASES.items():
        for alias in aliases:
            if alias in lookup:
                resolved[canonical] = lookup[alias]
                break
    return resolved


def missing_columns(fieldnames: list[str] | None, required: set[str]) -> list[str]:
    resolved = resolve_columns(fieldnames)
    return sorted(column for column in required if column not in resolved)


def row_value(row: dict, canonical: str, resolved: dict[str, str]) -> str:
    actual = resolved.get(canonical, canonical)
    return row.get(actual) or ""


def normalize_sentiment(value: str | None) -> str:
    normalized = (value or "").strip().lower()
    return SENTIMENT_ALIASES.get(normalized, normalized)


def uses_chinese_fields(fieldnames: list[str] | None) -> bool:
    fields = {(field or "").strip() for field in fieldnames or []}
    chinese_aliases = {
        alias
        for aliases in COLUMN_ALIASES.values()
        for alias in aliases
        if alias and alias[0] > "\u007f"
    }
    return bool(fields & chinese_aliases)


def map_priority_output(row: dict, language: str) -> dict:
    if language != "zh":
        return row
    return {
        CHINESE_PRIORITY_FIELDS[column]: row[column]
        for column in CHINESE_PRIORITY_FIELDS
    }
