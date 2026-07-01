# Audit Rules

## Denominator Rules

Every percentage must state:

- numerator
- denominator
- denominator scope
- filtering boundary

Bad:

```text
Sleep breathing monitoring accounts for 49.9%.
```

Good:

```text
Within 12,489 product-labeled records, sleep breathing monitoring appears in 6,230 records, or 49.9%.
```

## Ranking Rules

Separate these claims:

- highest negative rate
- largest negative volume
- highest engagement-weighted severity
- highest business priority

A low-volume aspect can have the highest negative rate but still not be the highest business priority.

## Sample-Size Rules

Do not rank or generalize from tiny samples. Small samples can be used as cases, not market conclusions.

Suggested language:

- `directional observation`
- `case-level signal`
- `hypothesis to validate`
- `not enough support for ranking`

## Subset Reproducibility Rules

Any subset count must explain:

- source population
- filters
- deduplication logic
- included and excluded labels
- confidence threshold if model labels were used

If the subset cannot be reproduced, downgrade the claim.

## Platform Persona Rules

Do not infer platform users from stereotypes. Require cross evidence:

```text
platform x label x content type x sentiment x engagement
```

Use "platform discussion profile" when the data only supports discussion behavior, not demographic identity.

## Comparable-Object Rules

Do not rank unlike objects together:

- treatment method
- product category
- brand
- product line
- medical device maker
- implant therapy

Layer the taxonomy first, then compare within a layer.

## Strategy Leap Rules

Pain point evidence is not purchase intent. Purchase intent is not positioning proof.

Flag these high-risk jumps:

- treatment discomfort -> consumer product replacement
- accuracy complaint -> medical-grade accuracy claim
- social discussion -> validated target persona
- small-sample sentiment -> market ranking

Rewrite unsupported strategy claims as narrower, testable opportunities.
