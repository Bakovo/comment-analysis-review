# 输出格式

中文任务默认使用中文字段名，便于业务方阅读。只有在英文任务、API 风格交付、英文数据管道或用户明确要求时，才使用英文内部字段名。

## 字段名规则

| 场景 | 默认字段 |
| --- | --- |
| 中文报告、中文 Excel、中文 Markdown 表格 | 中文字段名 |
| 英文报告、英文 Excel、英文 Markdown 表格 | 英文字段名 |
| 同时给人看又要给脚本跑 | 优先使用中文字段；内置脚本支持中文字段和英文内部字段 |
| 下游系统固定要求英文 schema | 英文内部字段 |

## 原始评论输入

| 中文字段 | 英文内部字段 | 说明 |
| --- | --- | --- |
| 评论ID | `comment_id` | 源数据稳定 ID |
| 原始评论 | `original_text` | 原始评论或翻译后可分析文本 |
| 来源 | `source` | 平台、渠道、店铺或问卷来源 |
| 评分 | `rating` | 评分，如有 |
| 发布时间 | `created_at` | 评论日期或时间 |
| 互动量 | `engagement_count` | 点赞、回复、转发、有用票或其他互动量 |

## 观点表

一条原始评论可以生成多行观点。中文交付默认字段如下：

| 中文字段 | 英文内部字段 | 说明 |
| --- | --- | --- |
| 评论ID | `comment_id` | 源数据稳定 ID |
| 原始评论 | `original_text` | 原始评论或翻译后可分析文本 |
| 来源 | `source` | 平台或渠道 |
| 分析方面 | `aspect` | 产品、服务、体验或话题方面 |
| 观点概括 | `opinion` | 用户对该方面的判断 |
| 情绪 | `sentiment` | 正面、负面、中性或混合；英文内部值对应 `positive`、`negative`、`neutral`、`mixed` |
| 原文证据 | `evidence` | 评论里的直接证据片段 |
| 业务动作 | `business_action` | 产品、客服、市场或研究动作 |
| 置信度 | `confidence` | 高、中、低；英文内部值对应 `high`、`medium`、`low` |
| 互动量 | `engagement_count` | 从原评论继承的互动量，如有 |

## 主题摘要

| 中文字段 | 英文内部字段 | 说明 |
| --- | --- | --- |
| 主题 | `theme` | 主题名称 |
| 主题定义 | `definition` | 该主题包含什么 |
| 代表关键词 | `representative_keywords` | 帮助识别主题的关键词或短语 |
| 代表评论 | `representative_comments` | 代表性评论片段 |
| 相关分析方面 | `related_aspects` | 该主题下的分析方面标签 |
| 备注 | `notes` | 重叠、歧义或抽样 caveat |

## Codebook 标签手册

当分析会被复用、被他人复核或跨时间比较时，应输出 codebook。

| 中文字段 | 英文内部字段 | 说明 |
| --- | --- | --- |
| 分析方面 | `aspect` | 稳定的分析方面标签 |
| 定义 | `definition` | 这个标签的含义 |
| 纳入条件 | `include_when` | 什么证据应该归入这个标签 |
| 排除条件 | `exclude_when` | 哪些相似情况不应归入这个标签 |
| 示例证据 | `example_evidence` | 代表性原文证据 |
| 别名 | `aliases` | 被合并进来的旧标签或近义标签 |
| 备注 | `notes` | 边界情况或编码注意事项 |

## 优先级汇总

| 中文字段 | 英文内部字段 | 说明 |
| --- | --- | --- |
| 分析方面 | `aspect` | 方面标签 |
| 提及量 | `mention_count` | 该方面的观点行数 |
| 负面量 | `negative_count` | 负面观点行数 |
| 负面率 | `negative_rate` | 负面观点行数 / 提及量 |
| 互动量合计 | `engagement_sum` | 所有相关行的互动量 |
| 负面互动量 | `negative_engagement_sum` | 负面行的互动量 |
| 优先级分数 | `priority_score` | 启发式分数或自定义业务优先级分数 |
| 解读 | `interpretation` | 白话解释 |
| 下一步动作 | `next_action` | 下一步建议 |

## 洞察卡片

| 中文字段 | 英文内部字段 | 说明 |
| --- | --- | --- |
| 发现 | `finding` | 白话发现 |
| 分析范围 | `scope` | 数据范围和筛选边界 |
| 关键指标 | `metric` | 数量、比例或分数 |
| 原文证据 | `evidence` | 代表评论片段 |
| 解读 | `interpretation` | 为什么重要 |
| 业务动作 | `business_action` | 下一步业务动作 |
| 置信度 | `confidence` | 证据强度 |
| 下一步验证 | `next_validation` | 如何验证或加深这个发现 |
