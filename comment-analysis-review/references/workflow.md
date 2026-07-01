# Comment Analysis Workflow

## 1. Data Preparation

Require these fields when available:

- `comment_id`
- `original_text`
- `platform`
- `rating`
- `timestamp`
- `engagement_count`
- `author_or_group`
- existing labels, model outputs, or source filters

Record missing fields in the final caveats. Do not hide missing metadata.

## 2. Cleaning

Apply and document:

- duplicate removal
- empty or invalid text removal
- ads, spam, campaign boilerplate, and off-topic filtering
- language filtering or translation policy
- time range and platform boundaries

Any percentage or ranking must be tied to the post-cleaning population it uses.

## 3. Exploration

Use keyword counts, TF-IDF, and co-occurrence to find clues:

- frequent product features
- repeated pain words
- platform-specific vocabulary
- likely issue chains

Do not use keyword counts as final evidence for sentiment or intent.

## 4. Theme Discovery

Use NMF, BERTopic, embeddings, clustering, or manual grouping to form candidate themes. For each theme, keep:

- theme name
- top terms or representative phrases
- example comments
- inclusion and exclusion rules
- known noise or overlap

## 5. Aspect-Level Viewpoint Extraction

Split one comment into multiple rows when it contains multiple opinions.

Example:

```text
"The design looks premium, but the battery is weak and support replies slowly."
```

Rows:

| aspect | opinion | sentiment | evidence | business_action |
| --- | --- | --- | --- | --- |
| design | looks premium | positive | design looks premium | strengthen as selling point |
| battery | battery is weak | negative | battery is weak | investigate power use and expectation gap |
| service | support replies slowly | negative | support replies slowly | improve support SLA |

## 6. Priority Calculation

Separate:

- mention volume: how often an aspect appears
- negative rate: negative mentions divided by total mentions for that aspect
- negative volume: raw count of negative mentions
- engagement-weighted severity: negative mentions weighted by reach or interaction
- business priority: severity adjusted by feasibility, strategic relevance, and risk

Never collapse these into one vague "top pain point" without explaining the metric.

## 7. Evidence Review

Every final insight needs:

- metric table
- denominator and numerator
- 3-5 representative comments
- confidence level
- decision implication
- caveat or next validation step
