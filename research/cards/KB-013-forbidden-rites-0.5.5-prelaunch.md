# POE2 专家知识卡 13
## 0.5.5 Forbidden Rites：预发布版本的赛季、Ritual 与终局 Farm 框架

- 适用版本：0.5.5 预发布信息；现行实装基线仍为 0.5.4f
- 研究日期：2026-09-01
- 模块：地图、赛季机制与 Farm
- 状态：PRE_RELEASE / 官方已确认 + 部分社区实测待复核

## 一、版本边界

截至 2026-09-01，GGG 已确认 0.5.5 与 Forbidden Rites 将于 2026-09-04 13:00 PDT 开放；中国大陆时间为 2026-09-05 04:00。Forbidden Rites 使用新鲜独立经济，玩家需要在角色选择界面新建活动角色；Runes of Aldur 不会被删除或强制迁移，而是继续并行存在。Duelist 不在 0.5.5，而是在 1.0 正式版加入。

0.5.5 正式 Patch Notes 截至本卡创建时仍未发布，因此下列内容必须与 0.5.4f 实装规则分层，不能把预告直接当作最终数值。

## 二、官方已确认

### 1. 新活动与经济

- Forbidden Rites 是新活动联赛，拥有独立新经济、新挑战与限定奖励。
- 0.5.5 发布后，Runes of Aldur 继续存在。
- 活动入口：角色选择界面选择 Forbidden Rites，新建角色进入。
- 活动结束日期、是否与 1.0 同步结束、完整迁移规则：官方 FAQ 尚未给出完整细节。

### 2. Campaign Ritual

已公布的玩法结构是：

1. 先击败守护 Effigy 的怪物；
2. 激活 Effigy，使已经击败的敌人再次复活并进行第二轮战斗；
3. 通过 Ritual 取得 Tribute；
4. 用 Tribute 兑换奖励。

特殊 Ritual Cluster 会把多个区域/首领串联起来，后续区域会累计前面遇到的 Boss，最终可能形成多 Boss 汇战；官方预告明确强调“累计 Boss”是该活动的核心卖点。

### 3. 终局扩展

官方预告已确认：

- Ritual 会进入终局；
- Sacred Bloom 可用于向地图加入 Wildwood 入口；
- Wildwood 内存在 Primal / Vivid / Wild Wisps，强化怪物并提高潜在奖励；
- 还存在稀有 Sacred Wisp；
- 终局会加入 Abyssal Ravines；
- Trial of Chaos 将大幅重做；
- Runes of Aldur 的部分系统会进入核心内容。

## 三、数据站可验证 / 预发布结构

目前二次资料与数据站对下列结构的描述高度一致，但最终数值仍须等正式 Patch Notes 或实机数据：

- Trial of Chaos 可扩展到 30 个房间；
- 房间之间可暂停并离开，稍后继续；
- 目标设计更偏向直接击杀怪物；
- 新增 Wager Modifiers，以风险换奖励；
- 高层 Trial 可在一次尝试中获得更多 Trialmaster 相关材料；
- Expedition 部分内容进入核心池，并可能通过 Expedition Tablets 定向加入地图；
- Abyssal Ravines 贯穿 Atlas，并在深处导向 Boss 遭遇。

这些内容在当前知识库中统一标记为 PRE_RELEASE，直到 0.5.5 notes 与实机数据同步后再升格为 STABLE。

## 四、核心规则与收益模型（当前只能建立相对模型）

### 1. Ritual 事件的两阶段价值

Ritual 的基础收益可拆成：

`第一轮清场价值 + 第二轮复战价值 + Tribute 商店价值 + Cluster/Boss 额外奖励价值`

如果第二轮是第一轮敌人的复活/再战，则单位区域收益不应按“只打一次怪”估算。对开荒而言，Ritual 的价值通常不在单次击杀速度，而在于：

- 额外经验与掉落机会；
- Tribute 兑换的定向性；
- Cluster 终点 Boss 的叠加奖励。

### 2. 多 Boss Cluster 的风险调整 EV

对一个包含 k 个累计 Boss 的终点遭遇，可先使用：

`EV_cluster = expected_reward - input_cost - failure_probability × failure_loss`

而不是只看“最终奖励稀有度”。当 k 增大时，不能线性假设奖励一定按 k 倍增长；必须同时提高：

- 机制重叠惩罚；
- 目标切换损失；
- 场地占用与不可输出时间；
- 失败导致的整次 Cluster 机会成本。

### 3. Wildwood Wisps 的收益-难度曲线

预发布信息只确认 Wisps 会同时增强怪物与潜在奖励，没有公开完整函数。当前只允许使用相对模型：

`RiskAdjustedEV = LootValue(WispAmount) - ClearTimeCost - DeathRisk(WispAmount)`

不能在没有实测样本前直接断言“拿满所有 Wisps 必然最优”。

## 五、常见误区

1. 把 Forbidden Rites 误认为 Runes of Aldur 的强制重置；正确理解是独立新经济活动并行开启。
2. 把 0.5.5 预告中的“Trial 30 房”直接当作已上线的最终数值；正式 Patch Notes 尚未发布。
3. 认为 Ritual 只提供普通怪掉落；预告明确存在 Tribute 商店与特殊 Cluster 奖励。
4. 认为所有 Wisps 都应该一次性拿满；更高怪物强化可能让 EV/hour 下降。
5. 看到社区单次高收益截图就当平均收益；必须区分均值、中位数、上尾样本。
6. 把 Duelist/剑系内容提前并入 0.5.5；官方 FAQ 已明确 Duelist 属于 1.0。

## 六、例外条件

- 0.5.5 的机制可能同时包含“活动专属内容”和“补丁级系统改动”；在正式 Notes 出来前，不能默认所有改动只对 Forbidden Rites 生效。
- Runes of Aldur 继续存在，不代表其交易流动性和活跃人口不受新经济分流影响；这是经济推断，不是官方硬规则。
- 终局 Ritual、Wildwood、Abyssal Ravines 与 Trial of Chaos 之间的 Atlas 互相作用，当前未公开完整节点/掉率，不能提前做精确刷法。

## 七、可复现实验

### 实验 A：Campaign Ritual 单区收益

固定角色等级和区域，记录 20 个同等级区域：

- 首轮清场时间；
- 二轮复战时间；
- 总怪物数量；
- Tribute 产出；
- 商店兑换物品；
- 经验与总掉落价值。

输出：

`Tribute/minute`、`Loot value/minute`、`XP/minute`

### 实验 B：Cluster Boss 数量曲线

按 1/2/3/4 Boss 分组，记录：

- 总耗时；
- 死亡率；
- 有效输出占比；
- 奖励总价值；
- 失败损失。

输出：

`RiskAdjustedEV/hour`

### 实验 C：Wildwood Wisp 梯度

固定地图与角色，逐步增加 Wisp 拾取量，分层记录：

- 怪物生命/伤害变化；
- 清图时间；
- 掉落价值；
- 死亡率；
- 每分钟净收益。

### 实验 D：Trial of Chaos 房间收益曲线

记录 1-5、6-10、11-20、21-30 房的：

- 进入成本；
- 时间；
- Wager 选择；
- 失败率；
- 最终奖励。

## 八、对 BD、做装、Farm 的实际影响

### 对 BD

0.5.5 活动会更偏好：

- 能处理重复战斗的持续输出；
- 多 Boss 场景下的目标切换能力；
- 可移动输出；
- 对怪物强化/异常压力有余量的防御。

开荒阶段不应只按单体 Boss DPS 选 BD；应加入：

`Encounter Density Adaptation` 与 `RiskAdjustedClearSpeed`

### 对做装

由于是独立新经济，旧经济中的高价毕业装不能直接作为新活动开荒成本基准。更合理的做法是按：

- 早期可获得 Base；
- 活动初期常见通货供给；
- 低成本抗性/生命/伤害阈值；
- 关键技能断点；

建立“开荒可复制装备”而不是直接复制 Aldur 末期毕业装。

### 对 Farm

优先测试顺序建议是：

1. Campaign Ritual 的 Tribute/min；
2. Cluster Boss 的 RiskAdjustedEV/hour；
3. Trial of Chaos 的稳定层数；
4. Wildwood Wisp 梯度；
5. Expedition 核心化后的 Tablet 价值。

## 九、资料冲突与当前结论

### 官方已确认

- 0.5.5 于 2026-09-04 13:00 PDT 开放；
- Forbidden Rites 使用新经济；
- Runes of Aldur 并行存在；
- Duelist 不在 0.5.5，而在 1.0；
- Patch Notes 会在上线前发布，但截至 2026-09-01 尚未出现。

### 数据站可验证

- 0.5.5 预发布结构已被多个资料源整理为 Ritual Campaign、Wildwood、Trial of Chaos 重做、Abyssal Ravines、Expedition 核心化等。

### 社区实测

当前只有少量预览与讨论，尚未形成可重复的 0.5.5 实机样本，因此不能把社区对“最佳开荒机制”“最赚钱 Trial 层数”的判断写入稳定层。

### 尚待验证

- 活动准确结束时间与结束后的迁移规则；
- Ritual Tribute 的实际兑换池与刷新机制；
- Cluster Boss 的累计数量上限与掉落权重；
- Wildwood Wisps 的具体增强函数；
- Trial of Chaos 30 房的真实收益曲线；
- Expedition Tablets 的掉率与市场价格；
- Abyssal Ravines 的 Boss 入口与专属掉落；
- 0.5.5 是否存在未在预告中强调的系统级改动。

## 十、当前专家结论

> 0.5.5 不是简单的“新地图机制”，而是一次以独立新经济为前提、把 Campaign Ritual、终局 Wildwood、Abyss 与 Trial of Chaos 重做绑在一起的活动型版本。当前最可靠的准备策略不是提前猜某个绝对最赚的玩法，而是围绕“单位时间 Tribute、单位时间净收益、跨 Boss 稳定性、失败损失”建立可复现实验框架，等正式 Patch Notes 与开服样本后再快速升级为 STABLE。

## 十一、下一次应继续验证的问题

按轮换优先进入“市场经济与构筑案例”，但在 0.5.5 开服后优先做：

1. Forbidden Rites 新经济的首周价格与流动性；
2. Campaign Ritual 与 Trial of Chaos 的实际开荒收益比较；
3. 旧 Aldur 资产是否因人口迁移出现明显流动性折价；
4. 哪类开荒 BD 能在 Cluster 多 Boss 与 Wildwood 高强化下保持最高 RiskAdjustedEV/hour。
