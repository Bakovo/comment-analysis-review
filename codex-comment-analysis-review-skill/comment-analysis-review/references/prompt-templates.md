# Prompt Templates

## Viewpoint Extraction

```text
Use $comment-analysis-review to extract aspect-level viewpoints from these comments.

Return a table with:
comment_id, original_text, platform, aspect, opinion, sentiment, evidence, business_action, confidence.

Split one comment into multiple rows when it contains multiple opinions.
Use only evidence that appears in the original text.
Mark uncertain rows with lower confidence instead of inventing details.
```

## AI Report Review

```text
Use $comment-analysis-review to review this AI-generated comment analysis report.

Check:
1. denominators and numerator/denominator consistency
2. sample sizes and whether rankings are allowed
3. ranking conflicts between rate, volume, and priority
4. platform persona evidence
5. category comparability
6. strategy leaps from pain point to recommendation

Return:
claim, issue, evidence, risk level, and corrected wording.
```

## Pressure Tests

Use these cases to test whether the skill catches common failures:

- A report says 52.3% is the highest negative rate while another section says 69.6% is second highest.
- A brand with only 3 comments is ranked above brands with 100+ comments.
- A percentage is stated without numerator, denominator, or scope.
- A platform is described as "young seed users" without cross-tab evidence.
- CPAP discomfort is used to claim a monitoring product can replace therapy.
