# Quality Check

Use this checklist before presenting final themes, viewpoint tables, priority rankings, or business actions.

## Scope Checks

- State the input count, final count, source boundary, and time range.
- Keep raw comment count and extracted viewpoint row count separate.
- Avoid comparing groups unless they share the same collection window, filters, and source rules.
- Name whether metrics are based on comments, viewpoint rows, users, orders, or another unit.

## Flow Compliance Checks

- Confirm all 7-step workflow steps are covered in order.
- If a step is not possible, state the limitation instead of skipping it.
- Do not approve a final deliverable that skips the workflow or uses methods outside their intended step.
- Confirm the method map is explicit: quick exploration uses frequency/keywords, TF-IDF, and co-occurrence; theme discovery uses LDA, NMF, embeddings/BERTopic, clustering, or manual grouping; viewpoint extraction uses aspect-level sentiment or LLM structured extraction.
- Confirm overall sentiment is treated as a trend aid, not a replacement for aspect-level viewpoint rows.

## Taxonomy Checks

- Keep aspect labels reusable across comments.
- Merge duplicate labels with the same meaning.
- Split labels that combine unrelated dimensions, such as product feature plus emotion plus action.
- Preserve an alias note when merging labels.
- Keep the taxonomy stable before doing priority ranking.

## Label Checks

- One row should express one viewpoint.
- `aspect` should name the target area, not repeat the whole sentence.
- `opinion` should summarize what the user says about the aspect.
- `sentiment` should match the evidence span.
- `evidence` should be a direct span from `original_text`.
- `business_action` should be practical and tied to the opinion.
- `confidence` should fall when the evidence is inferred, ambiguous, translated loosely, or outside the source text.

## Method Checks

- Treat keyword, TF-IDF, and co-occurrence outputs as exploration.
- Do not use model-generated topics without representative comments.
- Use aspect-level extraction for conclusions that affect business actions.
- Sample-check high-volume and high-priority labels.
- Check whether negative, neutral, and positive rows are being coded with the same strictness.

## Sampling QA

Before final delivery:

- Check at least 20 rows for small datasets.
- For larger datasets, check 5-10% of rows or at least 50 rows when practical.
- Oversample rare but severe issues.
- Oversample rows generated from long, mixed, sarcastic, or translated comments.
- Record repeated label disagreements and update the taxonomy.

## Priority Checks

- Keep mention count, negative count, negative rate, engagement, severity, and priority score separate.
- Explain what "top" means: highest volume, highest negative rate, highest engagement, highest severity, or highest business risk.
- Do not over-rank tiny samples.
- Do not let a high negative rate with very low volume outrank a repeated severe issue without explanation.
- Include confidence or caveats when evidence is limited.

## Insight Checks

Decision-ready insights should include:

- finding
- scope
- metric
- original evidence
- interpretation
- business action
- confidence
- next validation step

## Red Flags

Pause and revise if any of these appear:

- themes are named only from keywords, with no representative comments
- most comments create exactly one row despite mixed content
- most aspect labels appear only once
- evidence is paraphrased instead of quoted
- business actions are generic, such as "improve product"
- conclusions compare segments with very different sample sizes
- recommendations ignore severity, feasibility, or decision cost
