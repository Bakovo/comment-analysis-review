# 评论分析流程 Skill / Comment Analysis Workflow Skill

> 把大量非结构化评论转化为“用户说什么、针对哪个方面、态度如何、证据是什么、业务应先做什么”的双语 Codex skill。
>
> A bilingual Codex skill for turning unstructured comments into aspect-level, evidence-backed product and customer insights.

## 中文版

### 这个 Skill 是什么

`comment-analysis-workflow` 是一个覆盖评论分析全流程的 Codex skill，适合社媒评论、电商评价、App 评论、客服反馈、问卷开放题和社区讨论等场景。

### Reference 来源

这个仓库里的 reference 不是来自某一个公开模板，而是由三部分整理而来：

- 你提供的《评论分析流程》PPT：主要对应 7 步流程和方法选择表。
- 评论分析实务经验：包括标签体系设计、观点编码、抽样质检、分群比较、优先级判断和洞察写法。
- 通用文本分析方法：包括词频、TF-IDF、共现分析、LDA、NMF、Embedding、BERTopic 和大模型结构化抽取。

因此，它更像一套实战工作流，而不是论文引用清单。如果你希望做成公开学术型项目，后续可以再补充外部文献链接和 citation。

它的核心原则是：

```text
整条评论 ≠ 单个观点
```

一条评论可能同时包含多个方面、多个态度和多个业务信号。因此正式分析应尽量落到这个结构：

```text
aspect + opinion + sentiment + evidence + business_action
```

### 分析流程与 PPT 方法对应关系

本 skill 按照 PPT 中的“从快速摸底到正式洞察”的思路工作：先用轻量方法找线索，再用主题发现归纳结构，真正进入业务结论时回到方面级观点、原文证据和抽样质检。

| 流程步骤 | 这一步做什么 | 使用 PPT 中哪些评论分析方法 | 主要产出 |
| --- | --- | --- | --- |
| 1. 数据准备 | 确认评论 ID、原文、平台/来源、评分、时间、互动量和已有标签 | 不使用建模方法；为后续词频、TF-IDF、分群对比和互动加权准备字段 | 数据范围说明、字段检查、样本量记录 |
| 2. 清洗过滤 | 去重、去广告、过滤空文本、无关内容和低信号模板文本 | 不使用建模方法；这是词频、共现、主题模型和情感分析的前置质量控制 | 清洗说明、删除原因、最终可分析样本 |
| 3. 粗探索 | 快速判断用户最常提什么、哪些词在某组更突出、哪些问题经常一起出现 | 词频/关键词、TF-IDF、共现分析 | 初步线索、差异词、关联痛点，不直接作为最终结论 |
| 4. 主题发现 | 把相似评论归为候选主题，并用代表评论命名主题 | LDA、NMF、Embedding/BERTopic，也可人工归类；短评场景优先 NMF 或 BERTopic | 候选主题、主题定义、代表关键词、代表评论 |
| 5. 观点抽取 | 把一条评论拆成多个“方面 + 观点 + 情绪 + 证据 + 业务动作” | 方面级情感分析、大模型 AI 标签/结构化抽取；整体情感分析只用于辅助趋势，不替代方面级抽取 | 方面级观点表、codebook 标签手册、原文证据 |
| 6. 统计优先级 | 分开看提及量、负面量、负面率、互动加权负面量和业务优先级 | 基于方面级情感结果做统计；可结合共现分析理解问题链 | 优先级排序、痛点分层、高风险方面 |
| 7. 证据校验 | 抽样复核标签，查看代表评论，把发现转成可执行业务建议 | 抽样复核、代表评论校验；回看主题模型和 AI 标签是否稳定 | 洞察卡片、业务动作、置信度、下一步验证建议 |

方法使用原则：

- 词频/关键词、TF-IDF、共现分析适合快速摸底，但只能作为线索。
- LDA、NMF、Embedding/BERTopic 适合发现候选主题，但主题命名必须回到代表评论。
- 整体情感分析适合看趋势，不适合处理“一条评论多种态度”的情况。
- 方面级情感分析和大模型结构化抽取最接近业务决策，但必须做抽样质检和证据校验。

### 适合场景

- 从原始评论中提炼用户痛点和卖点
- 把评论拆成方面级观点表
- 对不同平台、产品、版本或人群做反馈对比
- 用词频、TF-IDF、共现、主题模型做前期探索
- 用大模型把评论转成结构化标签
- 生成产品、运营、客服或市场团队可用的洞察摘要

### 示例

原始评论：

```text
白天拍照很清晰，但视频通话时电量掉得太快，玩游戏十分钟后手机会发烫。
```

方面级拆解：

| aspect | opinion | sentiment | evidence | business_action |
| --- | --- | --- | --- | --- |
| camera | 白天拍照清晰 | positive | 白天拍照很清晰 | 把白天拍照效果作为卖点 |
| battery_life | 视频通话耗电快 | negative | 电量掉得太快 | 测试视频通话耗电并优化续航预期说明 |
| thermal_management | 游戏后手机发烫 | negative | 手机会发烫 | 排查游戏发热和散热策略 |

### 仓库结构

```text
comment-analysis-workflow/
  SKILL.md
  agents/
    openai.yaml
  references/
    analyst-playbook.md
    analyst-playbook.zh.md
    workflow.md
    workflow.zh.md
    method-selection.md
    method-selection.zh.md
    quality-check.md
    quality-check.zh.md
    output-schemas.md
    output-schemas.zh.md
    prompt-templates.md
    prompt-templates.zh.md
  scripts/
    validate_viewpoints.py
    priority_score.py
  assets/
    comment-viewpoints-template.csv
    priority-summary-template.csv
examples/
  sample-comments.csv
  sample-comments.zh.csv
  expected-viewpoints.csv
  expected-viewpoints.zh.csv
  expected-priority-summary.csv
  expected-priority-summary.zh.csv
README.md
```

### 快速使用

把 `comment-analysis-workflow` 文件夹复制到本地 Codex skills 目录：

```text
Windows: C:\Users\<you>\.codex\skills\comment-analysis-workflow
macOS/Linux: ~/.codex/skills/comment-analysis-workflow
```

然后在 Codex 中这样调用：

```text
使用 $comment-analysis-workflow 分析这些电商评论，按 7 步流程输出主题、方面级观点、优先级和业务建议。
```

```text
使用 $comment-analysis-workflow 把 examples/sample-comments.zh.csv 拆成观点表，并参考 examples/expected-viewpoints.zh.csv 的格式。
```

### 可选脚本

校验观点表字段、情绪标签和证据是否能在原文中找到：

```bash
python comment-analysis-workflow/scripts/validate_viewpoints.py examples/expected-viewpoints.csv
```

汇总方面级优先级：

```bash
python comment-analysis-workflow/scripts/priority_score.py examples/expected-viewpoints.csv
```

默认优先级分数只是启发式方法，应根据品类、业务风险和决策成本调整。

### 隐私提醒

公开仓库只放 skill、模板和脱敏示例。请不要上传真实用户隐私、客户机密、账号凭证、API key 或未脱敏评论。

### 推荐 GitHub Topics

```text
codex-skill
comment-analysis
sentiment-analysis
topic-modeling
customer-feedback
social-listening
product-insights
```

---

## English Version

### What This Skill Is

`comment-analysis-workflow` is a Codex skill for end-to-end comment analysis across social media comments, ecommerce reviews, app store reviews, support feedback, open-ended survey responses, and community discussions.

### Reference Basis

The references in this repository are synthesized from three sources:

- Your provided comment analysis workflow deck, especially the 7-step workflow and method selection table.
- Practical comment analysis experience, including taxonomy design, viewpoint coding, sampling QA, segmentation, priority judgment, and insight writing.
- Common text analytics methods, including word frequency, TF-IDF, co-occurrence, LDA, NMF, embeddings, BERTopic, and structured LLM extraction.

This is a practitioner workflow rather than an academic citation list. If the repository later needs a research-style bibliography, external sources and citations can be added separately.

Its core principle is:

```text
One comment is not one viewpoint.
```

A single comment may contain multiple aspects, opinions, sentiments, and business signals. Formal analysis should therefore work at this level:

```text
aspect + opinion + sentiment + evidence + business_action
```

### Workflow and PPT Method Mapping

The skill follows the deck's "quick exploration to formal insight" logic: use lightweight methods to find clues, use theme discovery to organize structure, and use aspect-level viewpoints, original evidence, and sampling QA for decision-ready insights.

| Step | What Happens | PPT Methods Used | Main Output |
| --- | --- | --- | --- |
| 1. Data preparation | Confirm comment ID, original text, source, rating, timestamp, engagement, and existing labels | No modeling method; prepares fields for frequency, TF-IDF, segmentation, and engagement weighting | Scope note, field check, sample-size record |
| 2. Cleaning and filtering | Remove duplicates, ads, empty text, irrelevant content, and low-signal boilerplate | No modeling method; prerequisite for frequency, co-occurrence, topic modeling, and sentiment analysis | Cleaning note, removal reasons, final analyzable sample |
| 3. Quick exploration | Check what users mention most, which terms are distinctive, and which issues appear together | Word frequency/keywords, TF-IDF, co-occurrence analysis | Early clues, distinctive terms, linked pain points, not final conclusions |
| 4. Theme discovery | Group similar comments into candidate themes and name them with representative evidence | LDA, NMF, embeddings/BERTopic, or manual grouping; prefer NMF or BERTopic for short reviews | Candidate themes, definitions, representative keywords, representative comments |
| 5. Viewpoint extraction | Split each comment into aspect, opinion, sentiment, evidence, and business action | Aspect-level sentiment analysis, LLM structured extraction/AI labels; overall sentiment is only a trend aid | Viewpoint table, reusable codebook, original evidence |
| 6. Priority statistics | Separate mention volume, negative volume, negative rate, engagement-weighted negative volume, and business priority | Statistics based on aspect-level sentiment; co-occurrence can help explain issue chains | Priority ranking, pain-point tiers, high-risk aspects |
| 7. Evidence check | Sample-check labels, inspect representative comments, and turn findings into business actions | Sampling QA and representative-comment review; re-check topic and AI labels for stability | Insight cards, business actions, confidence, next validation steps |

Method principles:

- Word frequency/keywords, TF-IDF, and co-occurrence are best for quick exploration, not final claims.
- LDA, NMF, embeddings, and BERTopic are useful for candidate themes, but theme names must be checked against representative comments.
- Overall sentiment is useful for trend monitoring, but it loses detail when one comment contains multiple attitudes.
- Aspect-level sentiment and LLM structured extraction are closest to business decisions, but they require sampling QA and evidence checks.

### Best For

- Finding user pain points and product strengths from raw comments
- Creating aspect-level viewpoint tables
- Comparing feedback across platforms, products, versions, or segments
- Using keyword, TF-IDF, co-occurrence, and topic modeling for early exploration
- Using LLMs to structure comments into reusable tags
- Producing insight summaries for product, operations, support, and marketing teams

### Example

Raw comment:

```text
The camera is sharp in daylight, but the battery drops too fast during video calls and the phone gets hot after ten minutes of gaming.
```

Aspect-level extraction:

| aspect | opinion | sentiment | evidence | business_action |
| --- | --- | --- | --- | --- |
| camera | camera is sharp in daylight | positive | camera is sharp in daylight | Use daylight camera quality in product messaging |
| battery_life | battery drops too fast during video calls | negative | battery drops too fast during video calls | Test video-call battery drain and set clearer expectations |
| thermal_management | phone gets hot after gaming | negative | phone gets hot after ten minutes of gaming | Investigate gaming heat and thermal throttling |

### Quick Start

Copy the `comment-analysis-workflow` folder into your local Codex skills directory:

```text
Windows: C:\Users\<you>\.codex\skills\comment-analysis-workflow
macOS/Linux: ~/.codex/skills/comment-analysis-workflow
```

Then invoke it in Codex:

```text
Use $comment-analysis-workflow to analyze these ecommerce reviews. Follow the 7-step workflow and return themes, aspect-level viewpoints, priority metrics, and business actions.
```

```text
Use $comment-analysis-workflow to convert examples/sample-comments.csv into a viewpoint table following examples/expected-viewpoints.csv.
```

### Included Scripts

Validate viewpoint fields, sentiment labels, and evidence spans:

```bash
python comment-analysis-workflow/scripts/validate_viewpoints.py examples/expected-viewpoints.csv
```

Summarize aspect-level priority:

```bash
python comment-analysis-workflow/scripts/priority_score.py examples/expected-viewpoints.csv
```

The default priority score is a heuristic. Adjust it for category context, business risk, and decision cost.
