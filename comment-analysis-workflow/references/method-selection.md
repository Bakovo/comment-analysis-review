# Method Selection

Use methods in layers. Fast methods find clues; decision-ready insight requires aspect-level evidence and sampling checks.

Do not use this file as a standalone shortcut. Method selection must stay inside the 7-step workflow: prepare data, clean data, explore, discover themes, extract viewpoints, quantify priority, and check evidence.

| Method | How it runs | Best for | Strength | Watch out |
| --- | --- | --- | --- | --- |
| Word frequency / keywords | Count terms after tokenization | What do users mention most? | Fast, transparent, easy to explain | Counts words, not meaning or sentiment |
| TF-IDF | Compare whether terms are distinctive in one group | Which terms stand out in negative reviews, platforms, or segments? | Good for group difference analysis | Still word-level |
| Co-occurrence | Count terms or themes that appear together | Which issues often happen together? | Finds linked pain points | Sensitive to cleaning quality |
| LDA | Probabilistic topic model from bag-of-words | What broad topics exist? | Classic and interpretable | Often unstable for short noisy comments |
| NMF | Topic decomposition from TF-IDF matrix | What relatively clear themes exist? | Often clearer than LDA for short reviews | Requires manual naming and checking |
| Embeddings / BERTopic | Cluster semantic vectors and extract topic words | Can similar meanings be grouped despite different wording? | Good for short, varied social text | Parameter and model dependent |
| Overall sentiment | Label each whole comment positive/negative/neutral | What is the overall mood? | Simple and useful for trend monitoring | Loses detail when one comment has mixed opinions |
| Aspect-level sentiment | Extract aspect, opinion, sentiment, and evidence | Which aspects are good or bad? | Closest to business decisions | Requires stronger models and QA |
| LLM structured extraction | Convert comments into a structured viewpoint table | How do we create reusable labels and insight tables? | Flexible; can output needs, pain points, and actions | Needs consistency and hallucination control |

## Recommended Layering

```text
word frequency / TF-IDF
-> co-occurrence and candidate themes
-> NMF, BERTopic, embeddings, or manual grouping
-> aspect-level viewpoint extraction
-> priority statistics
-> evidence check and business actions
```

## Decision Rules

- Use keywords when speed and transparency matter.
- Use TF-IDF when comparing groups, platforms, segments, or time periods.
- Use co-occurrence when you need to understand issue chains.
- Use NMF or BERTopic when there are many comments and themes are unclear.
- Use overall sentiment for monitoring, not final diagnosis.
- Use aspect-level extraction when the output will inform business actions.
- Always keep original comment evidence for final insights.
