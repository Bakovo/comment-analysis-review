# Prompt 模板

## 完整流程

```text
使用 $comment-analysis-workflow 按 7 步流程分析这些评论：
1. 数据准备；先不要建模
2. 清洗过滤；准备可分析文本
3. 粗探索；使用词频/关键词、TF-IDF 和共现分析
4. 主题发现；使用 LDA、NMF、Embedding/BERTopic、聚类或人工归类
5. 方面级观点抽取；使用方面级情感分析和大模型结构化抽取/AI 标签
6. 优先级统计；基于方面级观点行，分开声量、比例、互动量、严重性和优先级
7. 证据校验和业务动作；使用代表评论复核和抽样质检

返回：
- 分析范围和清洗说明
- 每一步使用了什么方法的方法映射表
- 可复用 aspect 标签手册
- 候选主题
- 方面级观点表
- 优先级汇总
- 3-5 条带原文证据的可执行洞察
```

## 抽取观点

```text
使用 $comment-analysis-workflow 从这些评论中抽取方面级观点。

返回 CSV 风格表格，字段为：
comment_id, original_text, source, aspect, opinion, sentiment, evidence, business_action, confidence, engagement_count

规则：
- 一条评论可以产生多行。
- evidence 必须是原始评论中的直接短语。
- sentiment 只用 positive、negative、neutral 或 mixed。
- 证据弱或属于推断时降低 confidence。
```

## 发现主题

```text
使用 $comment-analysis-workflow 从这些评论中识别候选主题。

可以把词频、TF-IDF 式差异词、共现关系、LDA、NMF、Embedding/BERTopic、聚类和语义归类作为探索工具。

返回：
- 主题名称
- 定义
- 代表关键词
- 代表评论
- 相关 aspect 标签
- 重叠或不确定说明
```

## 建立标签手册

```text
使用 $comment-analysis-workflow 为这些评论建立可复用 codebook。

返回：
- aspect
- definition
- include_when
- exclude_when
- example_evidence
- aliases
- notes

合并重复或重叠标签。标签要宽到可以复用，也要窄到能支持具体动作。
```

## 排列问题优先级

```text
使用 $comment-analysis-workflow 根据这张观点表排列问题优先级。

必须分开：
- 提及量
- 负面量
- 负面率
- 互动加权负面量
- 业务优先级

返回排序表，并说明每个“最高”问题到底是声量最高、负面率最高、互动最高还是业务风险最高。
```

## 示例调用

```text
使用 $comment-analysis-workflow 把 examples/sample-comments.zh.csv 转成方面级观点表。
然后输出优先级汇总，并参考 examples/expected-viewpoints.zh.csv 的结构。
不要跳过 7 步流程；如果样例文件无法支持某一步，请说明限制。
```
