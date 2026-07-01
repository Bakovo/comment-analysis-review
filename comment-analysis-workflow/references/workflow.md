# Workflow

Use this 7-step sequence for end-to-end comment analysis. Follow the steps in order. Do not skip a step silently; when a step cannot be completed, state why and mark the output as unavailable or hypothesis-only.

## Flow and Method Map

| Step | Purpose | Methods from the deck | Output |
| --- | --- | --- | --- |
| 1. Data preparation | Confirm IDs, original text, source, rating, time, engagement, and existing labels | No modeling method; prepare fields for word frequency, TF-IDF, segmentation, and engagement weighting | Scope note, field check, sample-size record |
| 2. Cleaning and filtering | Remove duplicates, spam, ads, empty text, irrelevant content, and boilerplate | No modeling method; prerequisite for word frequency, co-occurrence, topic modeling, sentiment, and LLM extraction | Cleaning note, removal reasons, final analyzable sample |
| 3. Quick exploration | Identify common terms, distinctive terms, and linked issues | Word frequency/keywords, TF-IDF, co-occurrence | Early clues, distinctive terms, linked pain points |
| 4. Theme discovery | Group similar comments into candidate themes | LDA, NMF, embeddings/BERTopic, clustering, manual grouping | Candidate themes, definitions, representative keywords, representative comments |
| 5. Aspect-level viewpoint extraction | Split comments into aspect, opinion, sentiment, evidence, and action | Aspect-level sentiment, LLM structured extraction/AI labels; overall sentiment only as a trend aid | Viewpoint table, codebook, original evidence |
| 6. Priority statistics | Separate volume, negative rate, negative count, engagement, severity, and business priority | Statistics from aspect-level sentiment rows; co-occurrence can explain issue chains | Priority ranking, pain-point tiers, high-risk aspects |
| 7. Evidence check and business actions | Sample-check labels and turn findings into actions | Sampling QA, representative-comment review, stability check of topic and AI labels | Insight cards, actions, confidence, next validation |

## 1. Data Preparation

Confirm the analysis scope before counting anything:

- `comment_id`
- `original_text`
- platform or source
- rating, if available
- timestamp
- engagement count
- existing labels, if any

Record the input count, source boundary, time range, and any filters applied.

## 2. Cleaning and Filtering

Remove or flag:

- duplicates
- ads or spam
- empty or near-empty text
- irrelevant content
- boilerplate replies
- language mismatches when outside scope

Keep a cleaning note with input count, removed count, final count, and removal reasons.

## 3. Quick Exploration

Use fast methods to find early clues:

- word frequency
- keyword search
- TF-IDF
- co-occurrence

Treat these outputs as exploration. They help decide what to inspect next, but they do not replace aspect-level interpretation.

## 4. Theme Discovery

Use NMF, BERTopic, embedding clustering, or manual grouping to find candidate themes.

For each theme, record:

- theme name
- representative keywords
- representative comments
- why the comments belong together
- possible overlap with other themes

Do not treat model-generated topics as final labels until sampled comments confirm them.

## 5. Aspect-Level Viewpoint Extraction

Split comments into rows with aspect-level sentiment or LLM structured extraction. One comment can create many rows. Overall sentiment may be reported for trend monitoring, but it must not replace aspect-level rows for business conclusions.

Required fields:

- `comment_id`
- `original_text`
- `aspect`
- `opinion`
- `sentiment`
- `evidence`
- `business_action`
- `confidence`

Sentiment labels:

- `positive`
- `negative`
- `neutral`
- `mixed`

Use direct evidence spans from the original comment. If evidence cannot be quoted, lower confidence.

## 6. Priority Statistics

Compute and keep separate:

- mention count
- negative count
- negative rate
- engagement-weighted negative volume
- business priority

Do not call a problem the "top issue" without saying whether top means highest volume, highest rate, highest engagement, or highest business risk.

## 7. Evidence Check and Business Actions

Before finalizing:

- inspect representative comments for every top theme
- sample rows from each high-priority aspect
- check whether extracted evidence supports the label
- separate confirmed findings from hypotheses
- convert findings into product, support, operations, or marketing actions
- state the next validation step
