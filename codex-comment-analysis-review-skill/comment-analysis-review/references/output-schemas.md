# Output Schemas

## Viewpoint Table

Required columns:

```text
comment_id, original_text, platform, aspect, opinion, sentiment, evidence, business_action, confidence
```

Recommended columns:

```text
timestamp, rating, engagement_count, source_url, theme, subtheme, user_segment, extraction_notes
```

Allowed sentiment values:

```text
positive, negative, neutral, mixed
```

## Insight Summary

Use this structure:

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

## Audit Ledger

Required columns:

```text
claim_id, claim_text, issue_type, numerator, denominator, denominator_scope, evidence_status, risk_level, recommended_fix
```

Issue types:

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

Allowed risk levels:

```text
high, medium, low
```

Correction wording should preserve any valid signal while lowering the claim strength when evidence is weak.
