# 提示词模板

## 观点抽取

```text
使用 $comment-analysis-review 从这些评论中抽取方面级观点。

返回表格字段：
comment_id, original_text, platform, aspect, opinion, sentiment, evidence, business_action, confidence。

如果一条评论包含多个观点，请拆成多行。
只能使用原文中出现的证据，不要补编细节。
不确定的行降低 confidence，不要强行判断。
```

## AI 报告复验

```text
使用 $comment-analysis-review 复验这份 AI 生成的评论分析报告。

检查：
1. 分母、分子和口径是否一致
2. 样本量是否足以支撑排名
3. 负面率、负面声量和业务优先级是否混用
4. 平台画像是否有交叉证据
5. 比较对象是否属于同一层级
6. 是否存在从痛点到策略建议的跳跃

返回字段：
claim_id, claim_text, issue_type, numerator, denominator, denominator_scope, evidence_status, risk_level, recommended_fix。

风险等级：
- high：可能误导战略、排名、定位或管理层决策
- medium：方向可能成立，但需要限制说明、分母或更窄表达
- low：主要是措辞、追溯性或格式问题
```

## 压力测试

用这些案例测试 skill 是否能抓住常见错误：

- 报告说 52.3% 是最高负面率，同时另一段又说 69.6% 是第二高。
- 只有 3 条评论的品牌被拿来做口碑排名。
- 百分比没有分子、分母或口径。
- 平台被描述为“年轻种草人群”，但没有交叉表证据。
- 因为 CPAP 不舒服，就声称监测产品可以替代治疗设备。

## 示例仓库测试

```text
使用 $comment-analysis-review 复验 examples/bad-ai-report.md。
返回审计表，并与 examples/expected-audit-ledger.csv 对比。
说明差异是否可以接受。
```
