# Analyst Playbook

Use this playbook when the task needs professional-grade comment analysis rather than a quick summary.

## Source Basis

This skill is based on:

- the user-provided comment analysis workflow deck, especially the 7-step workflow and method selection table
- standard customer feedback analysis practice: data cleaning, coding, theme discovery, aspect-level sentiment, evidence sampling, and insight prioritization
- common text analytics methods used as exploratory tools: keyword frequency, TF-IDF, co-occurrence, LDA, NMF, embeddings, BERTopic, and structured LLM extraction

Do not present these references as academic citations unless external sources are added separately.

## Taxonomy Design

Create an aspect taxonomy before serious counting.

Good aspect labels:

- name a stable target area, such as `battery_life`, `pricing`, `delivery`, `comfort`, `setup`, or `customer_service`
- are broad enough to group repeated feedback
- are narrow enough to support action
- avoid mixing product attributes, user emotions, and business actions in one label

Avoid:

- one-off labels for every comment
- labels that repeat the whole sentence
- labels that mix cause and effect, such as `battery_bad_need_refund`
- parallel labels with overlapping meaning, such as `overheating`, `phone_heat`, and `thermal_issue`

When labels overlap, merge them and keep an alias note.

## Coding Rules

Use one row per viewpoint.

Split a comment when:

- it mentions multiple aspects
- praise and complaint appear together
- one aspect has both cause and consequence
- a service issue and a product issue appear in the same comment

Do not split a comment when:

- two phrases repeat the same viewpoint
- a phrase is only background context
- the second clause is just intensification, not a new aspect

Keep `evidence` as a direct span. If the meaning is inferred, lower `confidence`.

## Sentiment Rules

Use sentiment at the aspect level.

- `positive`: clear praise, satisfaction, delight, recommendation, or exceeded expectation
- `negative`: complaint, friction, failure, unmet expectation, refund intent, or churn signal
- `neutral`: factual mention without clear evaluation
- `mixed`: inseparable positive and negative sentiment toward the same aspect

Prefer splitting mixed comments into separate positive and negative rows when different aspects are involved.

## Sampling QA

For professional deliverables, sample-check labels before finalizing:

- Review at least 20 rows for small datasets.
- For larger datasets, check 5-10% of rows or at least 50 rows, whichever is practical.
- Oversample high-priority aspects, rare but risky issues, and model-generated labels.
- Track recurring coding disagreements and update the taxonomy.

If the extraction is produced by an LLM, inspect for missing viewpoints, invented evidence, over-specific labels, and sentiment drift.

## Segmentation

Segment only when it answers a business question.

Useful segments:

- platform or channel
- product variant
- rating band
- customer type
- geography or language
- time period
- acquisition source

Before comparing segments, check whether sample sizes, collection rules, and time windows are comparable.

## Priority Logic

Do not rank issues by one metric alone.

Consider:

- volume: how often it appears
- negative rate: how concentrated the problem is
- severity: how much harm, churn, refund, or safety concern it implies
- engagement: whether the issue attracts public attention
- fixability: whether the team can act on it
- strategic value: whether the issue affects positioning, retention, or conversion

Use this default interpretation:

```text
high priority = repeated + negative + severe or actionable
medium priority = repeated but low severity, or severe but low evidence
low priority = isolated, ambiguous, or not actionable
```

## Insight Writing

A strong insight should include:

- what users are saying
- which aspect it concerns
- how common or important it is
- representative evidence
- why it matters
- what the business should do next
- confidence and caveat

Weak insight:

```text
Users dislike the product.
```

Strong insight:

```text
Thermal management is an early product-risk signal: 1 of 5 sample comments says the phone gets hot after ten minutes of gaming, and that row has the highest engagement among negative viewpoints. Treat this as a hypothesis from a small sample, then inspect support tickets and run a larger review pull focused on gaming heat complaints.
```

## Common Failure Modes

- Counting comments instead of viewpoint rows without saying so
- Treating keywords as themes without reading representative comments
- Calling a tiny sample a trend
- Mixing negative rate, negative count, and priority
- Creating labels that are too granular to reuse
- Translating emotional language too literally and losing intent
- Giving business recommendations that are not tied to evidence
