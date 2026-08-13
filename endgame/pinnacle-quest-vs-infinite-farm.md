---
id: KB-005
title: "0.5 终局 Pinnacle Boss：Quest 与 Infinite Farm 双层架构"
module: endgame
status: DATA_VERIFIED
confidence: high
applicable_version: "0.5.4 + Hotfix 1-4"
last_verified: "2026-08-13"
primary_sources:
  - ggg-050-patch
  - ggg-return-ancients
  - ggg-040-patch
secondary_sources:
  - poe2wiki-050
  - poe2wiki-arbiter-divinity
  - poe2wiki-arbiter-ash
  - poe2db-arbiter-divinity
---

# 0.5 终局 Pinnacle Boss：Quest 与 Infinite Farm 双层架构

## 核心结论

0.5.0 将 POE2 的终局 Boss 体系重构为两层：**确定性可达的 Quest 版本**负责推进终局故事与解锁，**可重复的 Infinite Farm 版本**承担更高难度和长期掉落循环。不能再沿用 0.3/0.4 时期“同一套钥匙按难度升级”的旧模型。

## 官方已确认

- 0.5.0 以后 Atlas 主要机制都有引导任务线，并一路指向对应 Pinnacle Boss。
- 所有 Pinnacle Boss 都有可确定性到达的 Quest 版本，同时存在更困难的可重复非任务版本。
- Burning Monolith 与 Arbiter of Ash 被移动进 Precursor Fortress。
- 0.5 新增终局总线 boss **The Arbiter of Divinity**。
- 旧 0.3 的 Primary/Secondary/Tertiary Calamity Fragment 架构在 0.5 被废弃；这些物品已成为历史内容。
- Arbiter of Ash 在 0.4 已被改为在较低生命阈值强制转阶段，并在转阶段时回满生命；该规则使其“面板 DPS → 击杀时间”的线性换算失真。

## 数据站可验证

### Arbiter of Ash

- Quest 版本区域/怪物等级：约 74。
- 可重复版本：约 82。
- 当前页面仍记录其两阶段结构；<50% 左右进入第二阶段的表现需以当前实机为最终判据，因为官方曾调整转阶段阈值。

### Arbiter of Divinity

- Quest 版本：等级 79。
- 可重复版本：等级 82。
- 位于 The Origin Tower。
- 击败后可以激活 Fortress 中的 Ancient Mechanism，自动完成对应区域并获得该区域 Atlas 被动点；总计存在五个可激活区域，因此重复击杀最多可用于快速补全 Fortress 主树进度。

## 判定流程

面对任意 Pinnacle Boss，先按以下流程判断：

1. **确认版本**：先确认资料是否为 0.5+。若仍出现 Difficulty 0–4、旧 Calamity Fragments、旧 Boss Atlas Tree，优先标记为过期。
2. **确认 Encounter Type**：Quest / Infinite Farm，不把两者的等级、生命、掉落与进入成本混用。
3. **确认 Access Item**：任务物品通常承担一次性推进；可重复版本使用当前可交易/可反复取得的钥匙、碎片或机制产物。
4. **确认失败成本**：分别记录是否无限重进、是否消耗整套门票、是否存在版本特定 bug；不要从 Arbiter of Ash 推导所有 Pinnacle。
5. **确认阶段门槛**：检查强制无敌、强制转阶段、回血、清除状态等机制。
6. **确认真实输出窗口**：把 Boss 可被攻击时间、转阶段无敌时间、走位时间和强制回血纳入 TTK。

## 真实 TTK 模型

普通木桩模型：

`TTK ≈ Boss有效生命 / 常驻DPS`

对有阶段门槛和回血的 Pinnacle，应改成：

`TTK ≈ Σ(各可伤害阶段需要实际打掉的生命 / 该阶段有效DPS) + Σ强制机制时间 + Σ失去输出时间`

若某 Boss 在阶段切换回满生命，则“显示最大生命”不能直接视为整场只需打一次的总血量。

对 DoT、召唤物、图腾或需要站桩蓄力的构筑，还应将：

- 转阶段时 DoT 是否继续存在；
- Boss 无敌时技能是否浪费；
- 召唤物是否因场地机制死亡；
- 玩家是否被迫长距离位移；

单独计入 Effective DPS。

## 常见误区

1. **旧攻略写 Difficulty 0–4，所以现在仍按这套跑。** 0.5 已重构 Pinnacle 进入与任务体系。
2. **Quest Boss = Farm Boss，只是第一次免费。** 错。0.5 明确把 Quest 与可重复高难版本拆开。
3. **旧 Calamity Fragment 仍是当前 Uber Arbiter of Ash 门票。** 错，0.5 已将旧三种 Calamity Fragment 设为不可获取历史内容。
4. **面板 DPS 足够高就能按 HP/DPS 预测击杀时间。** 错，强制阶段、无敌、回血和移动窗口都会改变真实 TTK。
5. **所有 Pinnacle 都能无限复活。** 不能统一推导；必须看具体 Encounter Type 和当前版本。
6. **Boss 75% 元素抗性意味着直接把面板元素 DPS 乘 0.25。** 错，角色面板/构筑计算往往已经包含穿透、降抗、Exposure 等，应按最终抗性与技能实际结算重新算，不能重复扣减。

## 例外条件

- Wiki 或社区页面若写“technically N respawns”“likely due to a bug”，只作为 BUG/实测线索，不固化为稳定规则。
- Boss 技能页面中的阶段百分比可能滞后于官方后续阈值调整；官方明确改过 Arbiter of Ash 转阶段阈值，因此当前阶段触发点必须实机复核。
- Quest 版本的核心价值是推进与学习，不应拿其击杀体验直接预测 Infinite Farm 版的装备门槛。

## 可复现实验

### 实验 A：Quest 与 Infinite Farm 数值差异

对同一 Pinnacle：

1. 固定角色、技能、装备、配置。
2. 分别录制 Quest 与可重复版本。
3. 记录区域等级、Boss 血条阶段、第一次有效命中到转阶段所需时间、整场时长。
4. 禁止使用斩杀、随机暴击爆发等会放大波动的条件，至少重复 5 次。
5. 用击杀时间比例反推有效生命/减伤差异。

### 实验 B：阶段切换是否清除状态

分别测试 Poison、Ignite、Freeze buildup、Heavy Stun buildup、Curse、Exposure、玩家生成的持续地面效果：

1. 转阶段前施加状态。
2. 在 Boss 进入无敌/回血阶段时录像。
3. 转阶段后检查图标、伤害跳字、buildup 进度和持续时间。
4. 按状态逐项记录，不允许用一个状态推导其他状态。

### 实验 C：有效 DPS

用录像统计 60 秒 Boss 战中：

`有效输出占比 = Boss可受伤且角色实际输出的帧数 / 总战斗帧数`

`Boss有效DPS ≈ 木桩DPS × 有效输出占比 × 实战命中/覆盖修正`

这比单纯比较面板 DPS 更适合评估终局 Boss 构筑。

## 对 BD 的实际影响

- Boss 构筑要独立评价 **burst admission**：爆发是否能完整塞进可伤害窗口，而不是只看 10 秒峰值。
- DoT 构筑若状态跨阶段保留，理论上可缩小走位损失；若阶段清除，则需要重新启动，价值相反。
- Minion/Totem 构筑必须把实体存活率和重新部署时间算入 Boss DPS。
- 高机动技能与防御层的价值在 Pinnacle 中可能显著高于木桩 DPS 排名显示的收益。

## 对做装的实际影响

终局 Boss 装备不应只按 DPS/Divine 排序。应增加：

- 对应元素/物理生存门槛；
- 移速和 Dodge Roll 相关机动性；
- Recovery 在禁回复/高压阶段的可靠性；
- 技能启动时间与资源恢复；
- 能否在短可伤害窗口完成爆发。

如果某次升级只提高理论持续 DPS，却降低机动性或需要更长站桩，Boss 实战可能反而下降。

## 对 Farm 的实际影响

- Quest 版应视为“推进/学习成本”，Infinite Farm 版才进入收益/小时模型。
- Boss 门票是否自己跑或出售，应比较：

`EV(run) = 平均掉落价值 - 门票机会成本 - 失败概率×失败损失`

而不是只看“能不能打过”。
- Arbiter of Divinity 还具有 Atlas 进度加速价值；前几次击杀的收益不仅是掉落，还包括 Fortress 区域自动完成带来的 Atlas 点，因此不能用纯掉落 EV 评价第一次到第五次击杀。

## 资料冲突

- 旧 0.3/0.4 资料大量采用 Difficulty 0–4 / Calamity Fragment / Uber Arbiter 的旧终局结构；0.5 已重构，不能直接沿用。
- 当前 Wiki 对部分 Boss 的重进次数仍夹带“technical/bug”描述，证据等级低于官方规则。
- Boss-specific Freeze、Heavy Stun、Electrocute 阈值目前没有形成足够可靠的统一公开表；PoE2DB能确认通用 buildup 规则，但不能由此猜出每个 Pinnacle 的精确阈值。

## 当前结论

0.5 的终局设计已经从“同钥匙逐级提高难度”转为 **Quest 确定性推进 + Infinite Farm 重复高难循环**。以后所有 Boss 攻略、构筑门槛与经济判断，都必须首先区分这两种 Encounter。对真实 DPS 的评价必须把阶段无敌、强制机制、回血与输出覆盖率纳入，而不能用面板 DPS 直接除以 Boss 血量。

## 下一次继续验证

按轮换顺序进入“地图、赛季机制与 Farm”，优先研究：

**0.5.4 Runes of Aldur Grand Expedition：Remnant、Runic Modifier、Monster Potency、Waystone Tier 与收益的真实乘区，以及 0.5.3→0.5.4 后哪些旧 Farm 结论已经失效。**

Boss 模块后续 P0：

- Arbiter of Divinity Quest/Farm 两版精确生命、抗性和阶段阈值；
- Arbiter of Ash 当前 Quest/Farm 两版实际重进规则；
- Pinnacle 对 Freeze / Heavy Stun / Electrocute 的精确阈值与重复控制抗性；
- 转阶段是否清除 Poison/Ignite/Curse/Exposure/buildup。
