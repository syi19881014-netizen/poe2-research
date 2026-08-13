# POE2 Research / 流放之路2专家知识库

这是“流放之路2学习”项目的长期事实库、研究库与版本库。目标不是收集攻略，而是维护一套**可追溯、可纠错、可跨版本复核**的 Path of Exile 2 专家知识体系。

## 核心原则

1. **版本优先**：任何机制结论都必须注明适用版本与最后核验日期。
2. **证据分级**：官方说明、数据验证、社区实测、推断严格分离。
3. **结论可复现**：争议机制优先记录可复现实验，不以单条帖子作为最终规则。
4. **旧知识不删除**：失效结论标记 `OBSOLETE`，保留版本历史与失效原因。
5. **POE1经验不是POE2证据**：只能作为待验证假设。
6. **市场与做装必须时效化**：价格、权重、工艺和赛季机制结论必须带时间戳。

## 当前基线

- 当前研究版本：见 [`VERSION.md`](VERSION.md)
- 当前知识索引：[`data/knowledge-index.yaml`](data/knowledge-index.yaml)
- 证据等级：[`glossary/evidence-status.md`](glossary/evidence-status.md)
- 来源规范：[`sources/source-policy.md`](sources/source-policy.md)
- 待验证队列：[`research/todo/backlog.md`](research/todo/backlog.md)

## 已迁移核心知识卡

1. [`mechanics/damage-conversion.md`](mechanics/damage-conversion.md) — 伤害转换与 Gain as Extra 两阶段结算
2. [`skills/trigger-totem-minion.md`](skills/trigger-totem-minion.md) — Trigger / Totem / Minion / 亲自使用语义边界
3. [`classes/weapon-set-passives.md`](classes/weapon-set-passives.md) — Weapon Set Passive、Spirit 与快照边界
4. [`crafting/modifier-probability-model.md`](crafting/modifier-probability-model.md) — iLvl、词缀池、权重、Family 与做装概率模型

## 目录职责

- `mechanics/`：底层战斗规则
- `skills/`：主动、辅助、Persistent、Trigger 等技能规则
- `classes/`：职业、升华、被动树、Weapon Set
- `items/`：底材、暗金、词缀
- `crafting/`：通货、Omen、Desecration、概率模型
- `endgame/`：Atlas、Boss、终局系统
- `farming/`：Farm 方法与收益研究
- `economy/`：市场、价格与流动性模型
- `builds/`：开荒、终局与完整构筑案例
- `versions/`：逐版本变更与旧结论失效记录
- `research/`：实验、争议、待验证问题
- `sources/`：来源登记与证据政策
- `templates/`：知识卡、实验卡模板
- `scripts/`：知识库一致性校验

## 工作流

新补丁发布后：

1. 更新 `VERSION.md` 和 `versions/<version>.md`。
2. 搜索受影响关键词与知识卡。
3. 将旧卡标记 `NEEDS_RETEST`，不要直接覆盖历史。
4. 以 GGG 官方资料为第一证据；数据站与社区实测交叉验证。
5. 修订知识卡并更新 `last_verified`、`status`、`confidence`、`sources`。
6. 运行 `python scripts/validate_knowledge.py`。
7. 在 `CHANGELOG.md` 记录知识层变化，而不仅是游戏补丁变化。

## 证据状态

允许的主要状态：

`OFFICIAL` · `DATA_VERIFIED` · `COMMUNITY_VERIFIED` · `INFERENCE` · `DISPUTED` · `NEEDS_RETEST` · `OBSOLETE`

详细定义见 [`glossary/evidence-status.md`](glossary/evidence-status.md)。
