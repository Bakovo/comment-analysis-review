# 输出结构

## 观点表

必需字段：

```text
comment_id, original_text, platform, aspect, opinion, sentiment, evidence, business_action, confidence
```

推荐字段：

```text
timestamp, rating, engagement_count, source_url, theme, subtheme, user_segment, extraction_notes
```

允许的情绪值：

```text
positive, negative, neutral, mixed
```

默认保留字段名为英文，方便 CSV、脚本和跨语言复用。只有当用户明确要求中文字段名时，才翻译字段名。

## 洞察摘要

使用这个结构：

```text
Insight:
Scope:
Metric:
Numerator:
Denominator:
Evidence comments:
Business meaning:
Confidence:
Caveats:
Next validation:
```

中文交付时，可以把字段说明翻译为中文，但要保留分子、分母、证据、置信度和限制说明。

## 审计表

必需字段：

```text
claim_id, claim_text, issue_type, numerator, denominator, denominator_scope, evidence_status, risk_level, recommended_fix
```

问题类型：

```text
missing_denominator
mixed_denominator
small_sample_ranking
ranking_conflict
unreproducible_subset
platform_stereotype
category_mismatch
strategy_leap
unsupported_accuracy_claim
```

允许的风险等级：

```text
high, medium, low
```

修正文案应尽量保留有效信号，同时降低证据不足的结论强度。
