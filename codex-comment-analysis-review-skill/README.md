# Comment Analysis Review Skill

Turn messy comments into evidence-backed insights, and catch weak AI report claims before they become business decisions.

`comment-analysis-review` is a Codex skill for turning unstructured comments, reviews, and social media feedback into evidence-backed business insights. It helps Codex move beyond loose summaries by forcing every decision-level claim to connect back to aspect-level viewpoints, original comment evidence, reproducible denominators, sample-size checks, and explicit business implications.

This skill is especially useful when reviewing AI-generated comment analysis reports. It is designed to catch common but costly issues: mixed denominators, small-sample rankings, unsupported platform personas, category mismatches, ranking conflicts, and strategy recommendations that jump too quickly from user pain points to product positioning.

## Bilingual Behavior

This is one skill with two language-specific reference sets. Codex should automatically choose the right version based on the user's request, source material, and expected deliverable:

- Chinese task or Chinese report -> use `references/*.zh.md`
- English task or English report -> use `references/*.md`
- Mixed-language task -> follow the user's requested output language

Structured field names stay in English by default so CSV files, scripts, and downstream analysis remain consistent across languages.

## Why This Skill Exists

Comment analysis often fails at the exact point where it becomes useful: moving from text summaries to business recommendations. AI reports can sound confident while mixing denominators, ranking tiny samples, applying platform stereotypes, or turning user pain points into unsupported product positioning. This skill gives Codex a reviewable workflow for producing insights and a stricter audit layer for challenging weak claims.

## What It Does

- Breaks comments into `aspect + opinion + sentiment + evidence + business_action`.
- Guides the full workflow from data preparation to final insight review.
- Separates keyword exploration from decision-ready conclusions.
- Checks denominator scope, sample size, ranking logic, and evidence strength.
- Provides reusable schemas for viewpoint tables, insight summaries, and audit ledgers.
- Includes lightweight scripts for validating extracted viewpoint CSV files and summarizing aspect-level priority metrics.

## Before / After

Weak AI claim:

```text
Fitbit has the best reputation because its positive sentiment rate is 66.7%.
```

Reviewed with this skill:

```text
Downgrade. Fitbit appears in only 3 comments, so the result is a case-level signal rather than a brand reputation ranking.
```

Weak AI claim:

```text
CPAP users complain about mask discomfort, so this product can be positioned as a comfortable CPAP replacement.
```

Reviewed with this skill:

```text
Rewrite. CPAP is a treatment device. A consumer monitoring product may be framed as low-burden auxiliary monitoring or trend documentation, not as a treatment replacement, unless separate evidence supports that claim.
```

## Best For

- Social media comment analysis
- Ecommerce and app store review analysis
- Customer feedback mining
- AI-generated report review
- Product pain point discovery
- Positioning and opportunity assessment
- Executive-ready insight validation

## Not For

- Scraping comments from platforms
- Replacing legal, medical, or compliance review
- Making claims from private or unverified datasets without human review
- Treating small-sample signals as market-level conclusions

## Repository Structure

```text
comment-analysis-review/
  SKILL.md
  agents/
    openai.yaml
  references/
    workflow.md
    workflow.zh.md
    method-selection.md
    method-selection.zh.md
    audit-rules.md
    audit-rules.zh.md
    output-schemas.md
    output-schemas.zh.md
    prompt-templates.md
    prompt-templates.zh.md
  scripts/
    validate_viewpoints.py
    priority_score.py
  assets/
    comment-viewpoints-template.csv
    audit-ledger-template.csv
examples/
  sample-comments.csv
  sample-comments.zh.csv
  bad-ai-report.md
  bad-ai-report.zh.md
  expected-audit-ledger.csv
  expected-audit-ledger.zh.csv
```

## Quick Start

Install or copy the `comment-analysis-review` folder into your local Codex skills directory. The `examples/` folder is for GitHub readers and testing; it does not need to be copied into the skill directory.

Typical local paths:

```text
Windows: C:\Users\<you>\.codex\skills\comment-analysis-review
macOS/Linux: ~/.codex/skills/comment-analysis-review
```

Then invoke it in Codex with prompts like:

```text
Use $comment-analysis-review to analyze these product reviews and produce an aspect-level insight table.
```

```text
Use $comment-analysis-review to review this AI-generated social media insight report. Check denominators, sample sizes, ranking logic, platform persona evidence, and strategy leaps.
```

Chinese examples:

```text
使用 $comment-analysis-review 复验这份 AI 生成的评论分析报告，检查分母、样本量、排序逻辑、平台画像证据和策略跳跃。
```

```text
使用 $comment-analysis-review 把这些评论拆成方面级观点表，包含 aspect、opinion、sentiment、evidence、business_action 和 confidence。
```

You can test the skill against the included flawed report:

```text
Use $comment-analysis-review to audit examples/bad-ai-report.md. Compare the output with examples/expected-audit-ledger.csv.
```

Chinese test:

```text
使用 $comment-analysis-review 复验 examples/bad-ai-report.zh.md，并与 examples/expected-audit-ledger.zh.csv 对比。
```

## Core Workflow

1. Prepare the data: confirm comment ID, original text, platform, rating, timestamp, engagement, and existing labels.
2. Clean and filter: remove duplicates, ads, empty text, irrelevant records, and low-signal boilerplate.
3. Explore quickly: use keyword counts, TF-IDF, and co-occurrence as directional clues.
4. Discover themes: use topic modeling, embeddings, clustering, or manual grouping to form candidate themes.
5. Extract viewpoints: split each comment into one or more aspect-level rows.
6. Quantify priority: separate mention volume, negative rate, negative volume, engagement-weighted severity, and business priority.
7. Validate conclusions: check evidence, sample support, denominators, comparability, and recommendation risk.

## Output Standards

Decision-level insights should include:

- analysis scope
- numerator and denominator
- denominator boundary
- original comment evidence
- sample-size caveat when needed
- distinction between rate, volume, and priority
- confidence level
- recommended next validation step

Unsupported claims should be downgraded to hypotheses. Claims with category confusion, missing evidence, or excessive strategy leaps should be rewritten or removed.

## Included Scripts

These scripts are optional helpers. You can use the skill without running Python, but the scripts are useful when you have CSV outputs to validate or summarize.

Validate a viewpoint CSV:

```bash
python comment-analysis-review/scripts/validate_viewpoints.py comment-analysis-review/assets/comment-viewpoints-template.csv
```

Summarize aspect-level priority metrics:

```bash
python comment-analysis-review/scripts/priority_score.py comment-analysis-review/assets/comment-viewpoints-template.csv
```

The default priority score is a heuristic, not a universal scoring model. Adjust the weights by business context, category risk, and decision cost.

## Example Use Cases

Review an AI report:

```text
Use $comment-analysis-review to audit this report. Return a table with claim, issue type, evidence status, risk level, and corrected wording.
```

Extract structured viewpoints:

```text
Use $comment-analysis-review to convert these raw comments into a viewpoint table with aspect, opinion, sentiment, evidence, business action, and confidence.
```

Prioritize product issues:

```text
Use $comment-analysis-review to identify which issues have the highest negative volume, highest negative rate, and highest business priority. Keep these metrics separate.
```

## Quality Checklist

Before using outputs for business decisions, confirm:

- Every percentage has a numerator, denominator, and scope.
- Small samples are not ranked as market conclusions.
- Platform personas are supported by cross-tab evidence.
- Categories being compared are at the same level.
- Original comments support the stated interpretation.
- Strategy recommendations do not overclaim what the data proves.

## Suggested GitHub Topics

If this repository is public, add these topics in the GitHub sidebar:

```text
codex-skill
comment-analysis
sentiment-analysis
social-listening
ai-audit
customer-feedback
product-insights
```

## Privacy Note

Do not upload raw customer data, private comments, API keys, account credentials, or confidential reports to a public repository. Keep sensitive datasets outside this skill package and pass them only inside controlled analysis sessions.
