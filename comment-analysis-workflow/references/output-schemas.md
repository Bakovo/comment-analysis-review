# Output Schemas

## Raw Comment Input

| Field | Description |
| --- | --- |
| `comment_id` | Stable ID from the source data |
| `original_text` | Original comment text |
| `source` | Platform, channel, store, or survey source |
| `rating` | Rating score, if available |
| `created_at` | Comment date or timestamp |
| `engagement_count` | Likes, replies, shares, helpful votes, or another engagement count |

## Viewpoint Table

One source comment can create multiple viewpoint rows.

| Field | Description |
| --- | --- |
| `comment_id` | Stable row ID from source data |
| `original_text` | Original comment text |
| `source` | Platform or channel |
| `aspect` | Product, service, experience, or topic aspect |
| `opinion` | User claim or judgment about the aspect |
| `sentiment` | `positive`, `negative`, `neutral`, or `mixed` |
| `evidence` | Direct text span from the comment |
| `business_action` | Suggested product, support, marketing, or research action |
| `confidence` | `high`, `medium`, or `low` |
| `engagement_count` | Engagement value carried from the source comment, if available |

## Theme Summary

| Field | Description |
| --- | --- |
| `theme` | Theme name |
| `definition` | What belongs in the theme |
| `representative_keywords` | Keywords or phrases that helped identify it |
| `representative_comments` | Short evidence snippets |
| `related_aspects` | Aspect labels under this theme |
| `notes` | Overlap, ambiguity, or sampling caveats |

## Codebook

Use a codebook when the analysis will be reused, reviewed by others, or compared over time.

| Field | Description |
| --- | --- |
| `aspect` | Stable aspect label |
| `definition` | What the label means |
| `include_when` | What evidence should be coded here |
| `exclude_when` | Similar cases that should not be coded here |
| `example_evidence` | Representative evidence span |
| `aliases` | Previous or similar labels merged into this one |
| `notes` | Edge cases or coding cautions |

## Priority Summary

| Field | Description |
| --- | --- |
| `aspect` | Aspect label |
| `mention_count` | Number of viewpoint rows for the aspect |
| `negative_count` | Number of negative rows |
| `negative_rate` | Negative rows divided by mention count |
| `engagement_sum` | Total engagement across rows |
| `negative_engagement_sum` | Engagement on negative rows |
| `priority_score` | Heuristic score or custom business priority score |
| `interpretation` | Plain-language meaning |
| `next_action` | Recommended next step |

## Insight Card

| Field | Description |
| --- | --- |
| `finding` | Plain-language finding |
| `scope` | Dataset and filter boundary |
| `metric` | Count, rate, or score |
| `evidence` | Representative comment snippets |
| `interpretation` | Why the finding matters |
| `business_action` | What to do next |
| `confidence` | Strength of evidence |
| `next_validation` | How to verify or deepen the finding |
