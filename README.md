# 评论分析流程 Skill

这是一个用于 **评论分析全流程** 的 Codex Skill，基于《评论分析流程.pptx》中提到的分析流程和方法整理而成。它的目标不是简单总结评论，而是把大量非结构化评论拆解成可以复核、可以统计、可以转化为业务行动的分析结果。

> 本项目聚焦评论分析流程，与 AI 报告复验无关。

## 这个 Skill 能做什么

`comment-analysis-workflow` 适合处理电商评价、社媒评论、App 评论、客服反馈、问卷开放题、社区讨论等文本数据。它会按照固定流程，把原始评论转成以下结构：

```text
aspect + opinion + sentiment + evidence + business_action
```

也就是说，它不会把“一整条评论”粗略当成一个观点，而是会识别同一条评论里可能同时存在的多个方面、多个态度和多个业务信号。

例如一条手机评论可能同时包含：

- 拍照效果好
- 视频通话耗电快
- 玩游戏后手机发烫

这些需要拆成多条方面级观点，而不是合并成一句“用户整体不满意”。

## 适合使用的场景

- 从原始评论中提炼用户痛点、满意点和高频需求
- 把评论拆成方面级观点表，便于统计和复核
- 比较不同平台、产品、版本、人群或时间段的反馈差异
- 使用词频、TF-IDF、共现分析、主题模型等方法做前期探索
- 用大模型把评论转成结构化标签和业务建议
- 为产品、运营、客服、市场团队输出可执行洞察

## 分析流程

这个 Skill 按照“先探索，再归纳，最后复核和行动”的方式运行。PPT 中提到的方法不会被混在一起使用，而是根据分析阶段分别承担不同作用。

| 步骤 | 这一阶段做什么 | 使用的评论分析方法 | 主要产出 |
| --- | --- | --- | --- |
| 1. 数据准备 | 确认评论 ID、原文、来源、评分、时间、互动量、已有标签等字段 | 不建模；为后续词频、TF-IDF、分群和互动加权准备字段 | 数据范围、字段检查、样本量说明 |
| 2. 清洗过滤 | 去重、去广告、过滤空文本、无关内容和低信号模板文本 | 不建模；这是词频、共现、主题模型和情感分析的前置质量控制 | 清洗规则、删除原因、可分析样本 |
| 3. 快速探索 | 快速判断用户最常提什么、哪些词更突出、哪些问题经常一起出现 | 词频、关键词、TF-IDF、共现分析 | 初步线索、差异词、关联痛点 |
| 4. 主题发现 | 把相似评论归为候选主题，并用代表性评论命名主题 | LDA、NMF、Embedding、BERTopic、人工归类 | 候选主题、主题定义、代表关键词、代表评论 |
| 5. 观点抽取 | 把评论拆成“方面 + 观点 + 情绪 + 证据 + 业务动作” | 方面级情感分析、大模型结构化抽取、AI 标签 | 方面级观点表、codebook、原文证据 |
| 6. 统计优先级 | 分开计算提及量、负面量、负面率、互动加权负面量和业务优先级 | 基于方面级观点表统计；可结合共现理解问题链路 | 优先级排序、痛点分层、高风险方面 |
| 7. 证据校验 | 抽样复核标签，查看代表评论，把发现转成业务建议 | 抽样质检、代表评论复核、主题与 AI 标签稳定性检查 | 洞察卡片、业务动作、置信度、下一步验证建议 |

## 方法使用原则

- 词频、关键词、TF-IDF、共现分析适合前期摸底，只能作为线索，不能直接当最终结论。
- LDA、NMF、Embedding、BERTopic 适合发现候选主题，但主题命名必须回到原始评论中复核。
- 整体情感分析适合看趋势，但不适合处理“一条评论里有多个方面和多种态度”的情况。
- 方面级情感分析和大模型结构化抽取最接近业务决策，但必须配合抽样质检和原文证据。
- 最终洞察必须同时看样本量、负面率、负面量、互动量、业务风险和可行动性。

## 手机评论示例

原始评论：

```text
白天拍照很清晰，但视频通话时电量掉得太快，玩游戏十分钟后手机会发烫。
```

方面级拆解：

| aspect | opinion | sentiment | evidence | business_action |
| --- | --- | --- | --- | --- |
| camera | 白天拍照清晰 | positive | 白天拍照很清晰 | 可把白天拍照效果作为卖点 |
| battery_life | 视频通话耗电快 | negative | 电量掉得太快 | 测试视频通话耗电，并优化续航预期说明 |
| thermal_management | 游戏后手机发热 | negative | 手机会发烫 | 排查游戏发热和散热策略 |

完整样例文件在 `examples/` 目录中：

- `sample-comments.csv`：英文手机评论原始样例
- `sample-comments.zh.csv`：中文手机评论原始样例
- `expected-viewpoints.csv`：英文观点拆解样例
- `expected-viewpoints.zh.csv`：中文观点拆解样例
- `expected-priority-summary.csv`：英文优先级统计样例
- `expected-priority-summary.zh.csv`：中文优先级统计样例

## 仓库结构

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

## 如何安装

把 `comment-analysis-workflow` 文件夹复制到本地 Codex skills 目录：

```text
Windows: C:\Users\<you>\.codex\skills\comment-analysis-workflow
macOS/Linux: ~/.codex/skills/comment-analysis-workflow
```

安装后，在 Codex 中可以这样调用：

```text
使用 $comment-analysis-workflow 分析这些电商评论，按 7 步流程输出主题、方面级观点、优先级和业务建议。
```

也可以让它参考仓库里的手机样例：

```text
使用 $comment-analysis-workflow，把 examples/sample-comments.zh.csv 拆成观点表，并参考 examples/expected-viewpoints.zh.csv 的格式。
```

## 中英文自动识别

虽然这个 README 只保留中文说明，但 skill 本体仍然支持中英文任务。它会根据用户请求、评论内容和交付语言自动选择对应参考文件：

- 中文任务优先读取 `.zh.md` 参考文件
- 英文任务优先读取英文参考文件
- 中英混合任务优先按用户要求的输出语言执行
- 结构化字段名默认保留英文，便于后续 CSV、脚本和数据工具处理

## 可选脚本

校验观点表字段、情绪标签和证据是否能在原文中找到：

```bash
python comment-analysis-workflow/scripts/validate_viewpoints.py examples/expected-viewpoints.csv
```

汇总方面级优先级：

```bash
python comment-analysis-workflow/scripts/priority_score.py examples/expected-viewpoints.csv
```

默认优先级分数只是启发式方法，实际项目中应根据品类、业务风险、决策成本和团队目标调整权重。

## 输出质量标准

正式交付前，分析结果应满足以下要求：

- 说明分析范围、样本量和数据来源
- 区分探索性线索和可决策洞察
- 每个重要结论都有原始评论证据
- 不把整体情感当成方面级情感
- 不把低样本量问题包装成确定结论
- 分开呈现提及量、负面率、负面量和优先级
- 对高优先级问题给出可执行业务动作

## 隐私提醒

公开仓库只建议上传 skill 文件、模板文件和脱敏样例。不要上传真实用户隐私、客户机密、账号凭证、API key 或未脱敏评论数据。

## 推荐 GitHub Topics

```text
codex-skill
comment-analysis
sentiment-analysis
topic-modeling
customer-feedback
social-listening
product-insights
```
