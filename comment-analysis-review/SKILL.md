---
name: comment-analysis-review
description: Use when analyzing comments, reviews, social media feedback, ecommerce feedback, app store reviews, customer feedback exports, AI-generated insight reports, 评论分析, 社媒评论, 用户反馈, AI报告复验, aspect-level sentiment, evidence-backed insights, denominator checks, sample-size checks, ranking consistency checks, and business recommendation validation.
---

# Comment Analysis Review

## Overview

Use this skill to turn unstructured comments into evidence-backed, reviewable business insights. Treat a comment as a container of multiple viewpoints, not as one indivisible opinion.

Core unit of analysis:

```text
aspect + opinion + sentiment + evidence + business_action
```

Use this skill for two related jobs:

- producing structured aspect-level comment insights
- auditing AI-generated reports before their claims are used for business decisions

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

First detect the user's working language from the request and source materials:

- Use Chinese references when the request, report, comments, or expected deliverable is mainly Chinese.
- Use English references when the request, report, comments, or expected deliverable is mainly English.
- If the input is mixed, use the user's requested output language. If not specified, answer in the user's latest message language.
- Keep structured field names in English unless the user explicitly asks for translated column names.

English reference set:

- Read `references/workflow.md` for the full analysis sequence and deliverables.
- Read `references/method-selection.md` when choosing between keywords, TF-IDF, co-occurrence, topic models, embeddings, sentiment, or LLM extraction.
- Read `references/audit-rules.md` before reviewing AI-generated reports or making business recommendations.
- Read `references/output-schemas.md` before creating viewpoint tables, insight summaries, or audit ledgers.
- Read `references/prompt-templates.md` when extracting viewpoints or stress-testing a report.

Chinese reference set:

- Read `references/workflow.zh.md` for the full Chinese analysis workflow.
- Read `references/method-selection.zh.md` when choosing analysis methods in Chinese tasks.
- Read `references/audit-rules.zh.md` before reviewing Chinese AI reports or business recommendations.
- Read `references/output-schemas.zh.md` before creating Chinese deliverables with structured tables.
- Read `references/prompt-templates.zh.md` when extracting viewpoints or stress-testing Chinese reports.

## Scripts

- Use `scripts/validate_viewpoints.py` to check whether an extracted viewpoint CSV has required fields, valid sentiment labels, evidence text, and ratio fields.
- Use `scripts/priority_score.py` to summarize aspect-level rows into priority metrics.

Run scripts with `--help` first when the expected input format is unclear.

`priority_score.py` uses a simple default heuristic. Adjust the weights when business context, category risk, or decision cost matters more than raw negative volume.

## Quality Bar

Never present a decision-level insight unless it has:

- a clear analysis scope
- a reproducible denominator
- enough sample support for the strength of the claim
- original comment evidence
- a distinction between rate, volume, and priority
- a stated confidence level or downgrade when evidence is weak

Downgrade unsupported claims to hypotheses. Remove claims that confuse categories, rely only on platform stereotypes, or jump from pain point to product positioning without evidence.
