# Method Selection

Use methods in layers. Fast methods find clues; decision-level insight requires aspect-level evidence and review.

| Method | Use For | Strength | Risk |
| --- | --- | --- | --- |
| keyword counts | quick scan of frequent terms | fast and transparent | ignores meaning and sentiment |
| TF-IDF | group differences by platform, rating, or segment | highlights distinctive terms | still word-level |
| co-occurrence | issue chains and related pain points | shows associations | noisy if cleaning is weak |
| LDA | broad topic exploration | classic and explainable | unstable for short noisy comments |
| NMF | topics from TF-IDF matrices | often clearer for short reviews | still needs manual naming |
| embeddings or BERTopic | semantic grouping of varied wording | good for social comments | parameter and model sensitive |
| overall sentiment | trend monitoring | simple | loses mixed opinions in one comment |
| aspect-level sentiment | feature-level good or bad | closest to business action | needs stronger extraction and QA |
| LLM structured labels | flexible viewpoint table creation | handles nuance | requires consistency and hallucination checks |

Recommended sequence:

```text
keyword or TF-IDF exploration
-> candidate topic discovery
-> aspect-level viewpoint extraction
-> metric calculation
-> evidence and audit review
```

Use topic models for discovery, not for unsupported final claims.
