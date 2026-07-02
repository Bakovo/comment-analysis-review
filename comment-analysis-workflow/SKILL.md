---
name: comment-analysis-workflow
description: Use when analyzing comments, user reviews, social media feedback, ecommerce reviews, app store reviews, customer feedback exports, open-ended survey responses, 评论分析, 社媒评论, 用户反馈, 电商评价, App评价, 主题发现, 观点抽取, 方面级情感, 词频, TF-IDF, 共现分析, NMF, BERTopic, aspect-level sentiment, evidence-backed insights, and priority ranking.
---

# Comment Analysis Workflow

## Overview

Use this skill to turn unstructured comments into aspect-level, evidence-backed business insights. Treat a comment as a container of multiple viewpoints, not as one indivisible opinion.

Professional stance:

- Separate exploration, coding, quantification, and interpretation.
- Build a stable aspect taxonomy before presenting trends.
- Quote evidence for every important interpretation.
- Treat small samples as signals, not conclusions.
- Convert findings into actions only after checking scope, volume, severity, and confidence.

Core unit of analysis:

```text
分析方面 + 观点概括 + 情绪 + 原文证据 + 业务动作
```

Use Chinese display field names for Chinese deliverables. Use English internal
field names only for English deliverables, API-style integrations, or
machine-readable CSVs that explicitly require English columns.

## Execution Contract

For any end-to-end comment analysis task, follow the 7-step workflow in order. Do not skip a step silently. If a step cannot be completed because the source data lacks fields, volume, language coverage, or user permission, state the limitation and mark the step as unavailable or hypothesis-only.

Before producing analysis:

1. Detect the working language and choose the matching reference set.
2. Read `workflow` and `method-selection` for the selected language.
3. Read `analyst-playbook`, `output-schemas`, and `quality-check` when the task asks for reusable labels, priority ranking, business insights, or a deliverable table.

Mandatory method mapping:

- Step 1 uses no modeling method; prepare fields for later frequency, TF-IDF, segmentation, and engagement analysis.
- Step 2 uses no modeling method; clean data before word frequency, co-occurrence, topic modeling, sentiment, or LLM extraction.
- Step 3 uses word frequency/keywords, TF-IDF, and co-occurrence as exploration only.
- Step 4 uses LDA, NMF, embeddings, BERTopic, clustering, or manual grouping to create candidate themes.
- Step 5 uses aspect-level sentiment and LLM structured extraction/AI labels for viewpoint rows; overall sentiment is only a trend aid.
- Step 6 computes priority from aspect-level rows and keeps volume, rate, engagement, severity, and business priority separate.
- Step 7 uses representative-comment review and sampling QA before final insights or business actions.

## Required Workflow

1. Prepare the data.
   Confirm comment ID, original text, platform/source, rating if present, timestamp, engagement, and any existing labels.
2. Clean and filter.
   Remove duplicates, ads, empty text, irrelevant records, and low-signal boilerplate before counting themes.
3. Explore quickly.
   Use keyword counts, TF-IDF, and co-occurrence only as directional clues, not final insight.
4. Discover candidate themes.
   Use NMF, BERTopic, embeddings, clustering, or manual grouping to identify candidate topics, then name them with original-text evidence.
5. Extract aspect-level viewpoints.
   Split each comment into one or more rows with aspect/opinion/sentiment/evidence/action. For Chinese output, render these columns as 分析方面、观点概括、情绪、原文证据、业务动作.
6. Quantify priority.
   Separate mention volume, negative rate, negative volume, engagement-weighted severity, and business priority.
7. Check evidence and finalize actions.
   Review representative comments, sample labels for consistency, and convert findings into practical product, support, marketing, or operations actions.

## Reference Routing

First detect the user's working language from the request and source materials:

- Use Chinese references when the request, comments, or expected deliverable is mainly Chinese.
- Use English references when the request, comments, or expected deliverable is mainly English.
- If the input is mixed, use the user's requested output language. If not specified, answer in the user's latest message language.
- For Chinese deliverables, use Chinese display field names by default, such as 评论ID、原始评论、来源、分析方面、观点概括、情绪、原文证据、业务动作、置信度、互动量.
- Use English internal field names only for English deliverables, API-style integrations, or CSV files that must match an English downstream schema.

English reference set:

- Read `references/workflow.md` for the full analysis sequence and deliverables.
- Read `references/analyst-playbook.md` when the task needs professional-grade taxonomy design, coding rules, sampling QA, segmentation, or insight writing.
- Read `references/method-selection.md` when choosing between keywords, TF-IDF, co-occurrence, topic models, embeddings, sentiment, or LLM extraction.
- Read `references/quality-check.md` before finalizing themes, viewpoint labels, priorities, or recommendations.
- Read `references/output-schemas.md` before creating codebooks, viewpoint tables, theme summaries, priority summaries, or insight cards.
- Read `references/prompt-templates.md` when preparing reusable prompts for extraction, prioritization, or summarization.

Chinese reference set:

- Read `references/workflow.zh.md` for the full Chinese analysis workflow.
- Read `references/analyst-playbook.zh.md` when Chinese tasks need professional taxonomy design, coding rules, sampling QA, segmentation, or insight writing.
- Read `references/method-selection.zh.md` when choosing analysis methods in Chinese tasks.
- Read `references/quality-check.zh.md` before finalizing Chinese themes, labels, priorities, or recommendations.
- Read `references/output-schemas.zh.md` before creating Chinese codebooks or structured tables.
- Read `references/prompt-templates.zh.md` when preparing Chinese prompts for extraction, prioritization, or summarization.

## Scripts

- Use `scripts/validate_viewpoints.py` to check whether an extracted viewpoint CSV has required fields, valid sentiment labels, and evidence text that appears in the original comment.
- Use `scripts/priority_score.py` to summarize aspect-level rows into priority metrics.

Run scripts with `--help` first when the expected input format is unclear.

`priority_score.py` uses a simple default heuristic. Adjust the weights when business context, category risk, or decision cost matters more than raw negative volume.

## Quality Bar

Never present a decision-level insight unless it has:

- a clear analysis scope
- enough sample support for the strength of the conclusion
- original comment evidence
- a distinction between rate, volume, and priority
- a stated confidence level or downgrade when evidence is weak

Downgrade weak signals to hypotheses. Keep exploration outputs separate from decision-ready insights.
