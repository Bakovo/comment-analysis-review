# 输出格式

## 原始评论输入

| 字段 | 说明 |
| --- | --- |
| `comment_id` | 源数据稳定 ID |
| `original_text` | 原始评论 |
| `source` | 平台、渠道、店铺或问卷来源 |
| `rating` | 评分，如有 |
| `created_at` | 评论日期或时间 |
| `engagement_count` | 点赞、回复、转发、有用票或其他互动量 |

## 观点表

一条原始评论可以生成多行观点。

| 字段 | 说明 |
| --- | --- |
| `comment_id` | 源数据稳定 ID |
| `original_text` | 原始评论 |
| `source` | 平台或渠道 |
| `aspect` | 产品、服务、体验或话题方面 |
| `opinion` | 用户对该方面的判断 |
| `sentiment` | `positive`、`negative`、`neutral` 或 `mixed` |
| `evidence` | 评论里的原文证据片段 |
| `business_action` | 产品、客服、市场或研究动作 |
| `confidence` | `high`、`medium` 或 `low` |
| `engagement_count` | 从原评论继承的互动量，如有 |

## 主题摘要

| 字段 | 说明 |
| --- | --- |
| `theme` | 主题名称 |
| `definition` | 该主题包含什么 |
| `representative_keywords` | 帮助识别主题的关键词或短语 |
| `representative_comments` | 代表性评论片段 |
| `related_aspects` | 该主题下的方面标签 |
| `notes` | 重叠、歧义或抽样 caveat |

## Codebook 标签手册

当分析会被复用、被他人复核或跨时间比较时，应输出 codebook。

| 字段 | 说明 |
| --- | --- |
| `aspect` | 稳定 aspect 标签 |
| `definition` | 这个标签的含义 |
| `include_when` | 什么证据应该归入这个标签 |
| `exclude_when` | 哪些相似情况不应归入这个标签 |
| `example_evidence` | 代表性原文证据 |
| `aliases` | 被合并进来的旧标签或近义标签 |
| `notes` | 边界情况或编码注意事项 |

## 优先级汇总

| 字段 | 说明 |
| --- | --- |
| `aspect` | 方面标签 |
| `mention_count` | 该方面的观点行数 |
| `negative_count` | 负面观点行数 |
| `negative_rate` | 负面观点行数 / 提及量 |
| `engagement_sum` | 所有相关行的互动量 |
| `negative_engagement_sum` | 负面行的互动量 |
| `priority_score` | 启发式分数或自定义业务优先级分数 |
| `interpretation` | 白话解释 |
| `next_action` | 下一步建议 |

## 洞察卡片

| 字段 | 说明 |
| --- | --- |
| `finding` | 白话发现 |
| `scope` | 数据范围和筛选边界 |
| `metric` | 数量、比例或分数 |
| `evidence` | 代表评论片段 |
| `interpretation` | 为什么重要 |
| `business_action` | 下一步业务动作 |
| `confidence` | 证据强度 |
| `next_validation` | 如何验证或加深这个发现 |
