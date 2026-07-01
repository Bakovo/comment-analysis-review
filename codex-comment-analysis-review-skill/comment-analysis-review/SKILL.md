---
name: comment-analysis-review
description: Use when analyzing comments, reviews, social media feedback, ecommerce feedback, app store reviews, AI-generated insight reports, 评论分析, 社媒评论, 用户反馈, AI报告复验, aspect-level sentiment, evidence-backed insights, denominator checks, sample-size checks, and business recommendation validation.
---

# Comment Analysis Review

## Overview

Use this skill to turn unstructured comments into evidence-backed, reviewable business insights. Treat a comment as a container of multiple viewpoints, not as one indivisible opinion.

Core unit of analysis:

```text
aspect + opinion + sentiment + evidence + business_action
```

## Required Workflow

1. Prepare the data.
   Confirm comment ID, original text, platform/source, rating if present, timestamp, engagement, and any existing labels.
2. Clean and filter.
   Remove duplicates, ads, empty text, irrelevant records, and low-signal boilerplate before counting themes.
3. Explore quickly.
   Use keyword counts, TF-IDF, and co-occurrence only as directional clues, not final insight.
4. Discover candidate themes.
   Use NMF, BERTopic, clustering, or manual grouping to identify candidate topics, then name them with original-text evidence.
5. Extract aspect-level viewpoints.
   Split each comment into one or more rows with aspect, opinion, sentiment, evidence, and suggested business action.
6. Quantify priority.
   Separate mention volume, negative rate, negative volume, engagement-weighted severity, and business priority.
7. Validate the report.
   Check denominators, sample sizes, ranking consistency, object comparability, platform persona evidence, and strategy leap risk before finalizing.

## Reference Routing

- Read `references/workflow.md` for the full analysis sequence and deliverables.
- Read `references/method-selection.md` when choosing between keywords, TF-IDF, co-occurrence, topic models, embeddings, sentiment, or LLM extraction.
- Read `references/audit-rules.md` before reviewing AI-generated reports or making business recommendations.
- Read `references/output-schemas.md` before creating viewpoint tables, insight summaries, or audit ledgers.
- Read `references/prompt-templates.md` when extracting viewpoints or stress-testing a report.

## Scripts

- Use `scripts/validate_viewpoints.py` to check whether an extracted viewpoint CSV has required fields, valid sentiment labels, evidence text, and ratio fields.
- Use `scripts/priority_score.py` to summarize aspect-level rows into priority metrics.

Run scripts with `--help` first when the expected input format is unclear.

## Quality Bar

Never present a decision-level insight unless it has:

- a clear analysis scope
- a reproducible denominator
- enough sample support for the strength of the claim
- original comment evidence
- a distinction between rate, volume, and priority
- a stated confidence level or downgrade when evidence is weak

Downgrade unsupported claims to hypotheses. Remove claims that confuse categories, rely only on platform stereotypes, or jump from pain point to product positioning without evidence.
