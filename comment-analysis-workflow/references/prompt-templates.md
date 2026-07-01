# Prompt Templates

## Full Workflow

```text
Use $comment-analysis-workflow to analyze these comments with the 7-step workflow:
1. data preparation; do not model yet
2. cleaning and filtering; prepare valid text for analysis
3. quick exploration with word frequency/keywords, TF-IDF, and co-occurrence
4. theme discovery with LDA, NMF, embeddings/BERTopic, clustering, or manual grouping
5. aspect-level viewpoint extraction with aspect-level sentiment and LLM structured extraction/AI labels
6. priority statistics from aspect-level rows, keeping volume, rate, engagement, severity, and priority separate
7. evidence check and business actions with representative-comment review and sampling QA

Return:
- scope and cleaning notes
- method map showing which method was used in each step
- codebook for reusable aspect labels
- candidate themes
- viewpoint table
- priority summary
- 3-5 decision-ready insights with original evidence
```

## Extract Viewpoints

```text
Use $comment-analysis-workflow to extract aspect-level viewpoints from these comments.

Return a CSV-style table with:
comment_id, original_text, source, aspect, opinion, sentiment, evidence, business_action, confidence, engagement_count

Rules:
- One comment can produce multiple rows.
- Evidence must be a direct phrase from the original comment.
- Keep sentiment as positive, negative, neutral, or mixed.
- If evidence is weak or inferred, lower confidence.
```

## Discover Themes

```text
Use $comment-analysis-workflow to identify candidate themes from these comments.

Use keyword frequency, TF-IDF-style distinctiveness, co-occurrence, LDA, NMF, embeddings/BERTopic, clustering, and semantic grouping as exploratory tools.

Return:
- theme name
- definition
- representative keywords
- representative comments
- related aspect labels
- notes on overlap or uncertainty
```

## Build a Codebook

```text
Use $comment-analysis-workflow to build a reusable codebook for these comments.

Return:
- aspect
- definition
- include_when
- exclude_when
- example_evidence
- aliases
- notes

Merge duplicate or overlapping labels. Keep labels broad enough to repeat and narrow enough to support action.
```

## Prioritize Issues

```text
Use $comment-analysis-workflow to prioritize issues from this viewpoint table.

Keep separate:
- mention count
- negative count
- negative rate
- engagement-weighted negative volume
- business priority

Return a ranked table and explain whether each "top" issue is top by volume, rate, engagement, or business risk.
```

## Example Invocation

```text
Use $comment-analysis-workflow to convert examples/sample-comments.csv into an aspect-level viewpoint table.
Then run a priority summary and compare the structure with examples/expected-viewpoints.csv.
Do not skip the 7-step workflow; if a step is not possible on the sample file, state the limitation.
```
