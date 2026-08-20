---
id: KB-008
title: "0.5.4f Pinnacle 控制：Freeze、Heavy Stun 与 Electrocute 阈值"
module: mechanics
status: DATA_VERIFIED
confidence: medium-high
applicable_version: "0.5.4f"
last_verified: "2026-08-20"
primary_sources:
  - ggg-upcoming-010e-control
  - ggg-020-patch
  - ggg-030-patch
secondary_sources:
  - poe2wiki-freeze
  - poe2wiki-stun
  - poe2wiki-electrocute
  - poe2db-freeze
  - poe2db-king-mists
  - poe2db-arbiter-ash
  - poe2db-arbiter-divinity
---

# 0.5.4f Pinnacle 控制：Freeze、Heavy Stun 与 Electrocute 阈值

## 核心结论

Pinnacle Boss 的控制必须拆成四层：**基础 buildup 规则、目标的 Ailment/Stun Threshold、当前控制后的抗连控机制、特定技能/阶段的临时免控状态**。Unique 敌人达到 70% buildup 后进入 Primed，只代表可被对应的“提前触发控制”技能/Crushing Blow 类效果利用，**不代表 Boss 的真实 Freeze / Electrocute / Heavy Stun 阈值只有 70%**。

## 官方已确认

### Freeze

- Cold Hit 默认贡献 Freeze Buildup；达到 100% 后目标 Frozen。
- GGG 在早期 0.1.0e 明确降低“刚被冻结过的目标”后续收到的 Freeze Buildup，用于阻止无限连冻。该机制针对同一目标的重复 Freeze，而非“冻结传播链”。
- Freeze 对 Boss 存在重复控制递减/恢复窗口，因此第一次 Freeze 所需 buildup 不能直接用于预测第二次、第三次。

### Heavy Stun

- Heavy Stun 由 Hit 造成 buildup；目标的 Stun bar 填满时触发 Heavy Stun。
- 玩家造成的 Physical damage 与 Melee damage 各自提供 50% more Heavy Stun Buildup；二者同时满足时乘算，合计为 2.25 倍相对基础 buildup。
- 0.2.0 将 Primed for Stun 门槛改为：Normal 40%、Magic 50%、Rare 60%、Unique 70%。Unique 的 70% 是 Primed 门槛，不是完整 Stun Threshold。
- Heavy Stun 结束后目标会在短时间内更难再次被 Heavy Stun。

### Electrocute

- Lightning damage **不会默认**贡献 Electrocute；必须由技能、Support 或其它效果明确允许 Lightning Hit 贡献 Electrocution Buildup。
- Electrocute 默认持续 5 秒，使目标无法行动。
- GGG 在 0.1.0e 将 Electrocute 调整为 25% harder to buildup，同时移除了 Electrocute Support 的伤害惩罚。

## 数据站可验证

### 通用规则

- Freeze 与 Electrocute 都使用 Elemental Ailment Threshold；更高 Threshold 会降低同样 Hit 所产生的 buildup。
- Freeze 达到 100% buildup 才会正常触发；重复 Freeze 后 Boss 对 Freeze 的有效 Threshold 会暂时提高，并随时间回落。
- Heavy Stun 与 Elemental Ailment Threshold 是两个独立的阈值体系，不能拿 Freeze 条的速度直接推算 Stun。

### Boss-specific 数据证明“每个 Boss 阈值不同”

PoE2DB 当前 The King in the Mists 数据记录：

- Ailment Threshold：645%（相对其基础模板缩放）；
- `cannot be stunned for ms after stun finished [4000]`，即数据层可见约 4 秒 Stun 后保护；
- `cannot be stunned while stunned`。

因此不能建立“所有 Pinnacle 都是固定 X% Threshold / 固定 4 秒”的统一规则；King 只能作为可验证个案。

Arbiter of Ash 与 Arbiter of Divinity 当前 PoE2DB 页面能直接验证大量技能级 `skill cannot be frozen` / 不可打断标签出现在特定技能或阶段行为上，但页面没有提供足够清晰、可直接引用的全局 Ailment/Stun Threshold 数值。这说明“某段技能不可冻”与“Boss 永久 Freeze Immune”是两回事。

## 判定与计算流程

### 1. 先确认技能是否有资格产生该控制

Freeze：检查命中伤害是否为 Cold，或是否有“其它伤害也贡献 Freeze Buildup”。

Heavy Stun：检查该 Hit 是否能产生 Heavy Stun Buildup；Cold damage 默认不承担 Heavy Stun buildup，Physical / Melee 有额外倍率。

Electrocute：必须先确认技能/Support 明确允许 Lightning damage contribute to Electrocute。只堆 Lightning damage、Shock chance 不会自动产生 Electrocute。

### 2. 计算单次相对 buildup

没有公开完整服务器公式时，使用相对模型：

`Relative Buildup ∝ Eligible Hit Damage × Buildup Modifiers × Ailment/Stun Application / Target Threshold`

Heavy Stun 的玩家 Physical Melee Hit 可额外乘：

`1.5 × 1.5 = 2.25`

这是与同等伤害、既非 Physical 又非 Melee 的 Hit 相比的 buildup 倍率，不代表最终 Stun 百分比必然是伤害的 2.25 倍，因为仍受目标 Threshold 和技能专属修正影响。

### 3. 以 UI buildup 实测反推目标

若固定技能一击使 Boss 从 0% → B%，则第一次控制约需：

`hits_to_control ≈ ceil(100 / B)`

但这只适用于第一次控制且 Boss 处于可控状态。

### 4. 第二次控制必须重新测

第一次 Freeze / Stun / Electrocute 后：

- 记录控制结束时刻；
- 每隔固定时间测试同一技能的一击 buildup；
- 得到 `B(t)`；
- 只有当 `B(t)`恢复到接近首次 B0 时，才能认为抗连控窗口基本结束。

不能简单写成“第二次固定需要两倍 buildup”，因为 GGG 没公开这样的统一倍率。

### 5. 检查 Boss 技能/阶段免控

如果 buildup 长时间停在 99% 或使用 Primed 技能无法触发控制，优先排查：

- Boss 正处于阶段转换；
- 当前技能标签包含不能被 Frozen/Stunned/Interrupted；
- Boss 有短时控制保护；

而不是先判断“buildup 公式失效”。

## Primed 与真实控制阈值

当前 Unique Primed 门槛为 70%。正确理解：

- 0–69%：未 Primed；
- ≥70%：可以被要求“Primed for Stun/Freeze”的特定技能提前触发；
- 普通 buildup 路线仍然需要走到 100%。

因此“Arctic Howl/Boneshatter 在 70% 应该工作”与“普通 Cold Hit 到 70% 就应该 Freeze”不是同一个命题。

## 常见误区

1. **Unique 70% = Boss Freeze/Stun Threshold。** 错，70% 是 Primed 门槛。
2. **Shock chance 很高，所以一定容易 Electrocute。** 错，Shock 与 Electrocute 是两套判定；Lightning Hit必须先获得 Electrocute 资格。
3. **第一次两击冻住，所以后面永远两击。** 错，GGG明确存在反连冻机制。
4. **Boss buildup 卡 99%就是Bug。** 不一定；Boss技能/转阶段可能临时不可被控制。
5. **Freeze、Heavy Stun、Electrocute共用一个阈值。** 错；Heavy Stun 使用 Stun Threshold，Freeze/Electrocute使用 Elemental Ailment Threshold。
6. **更多 Damage 和更多 Freeze Buildup 永远等价。** 仅在“该伤害全部有资格贡献 Freeze、且其它条件相同”的局部相对比较中近似成立；Damage还会改变阶段触发、击杀时间和其它机制。

## 例外条件

- Boss某一技能带 `skill cannot be frozen` 不代表整个 Boss 永久 Freeze Immune。
- 多人模式会改变怪物生命/相关阈值环境，不能把单人 70% Primed 实测直接拿到组队场景推算一击所需伤害。
- Map/Expedition modifiers 可以增加 Monster Ailment Threshold / Stun Threshold；普通地图 Boss测试必须记录地图词缀。
- 通过技能或装备让 Chaos/Lightning 等其它伤害“也贡献 Freeze/Electrocute”时，应把所有有资格的伤害类型合并进入对应 buildup 计算。

## 社区实测

### 高可信观察

- 玩家反复报告 Boss 在转阶段或特定不可打断动作中 Freeze/Stun buildup 会停在约 99%，动作结束后下一次合格 Hit 才触发控制。
- 2026 年社区仍能稳定观察到 Boss 第一次 Freeze 快、第二次 Freeze buildup 显著降低，符合 GGG 已确认的反连冻设计。

### 尚不能固化

- “任意一种 CC 后都会让其它 CC 一起进入固定 4 秒保护”目前只有社区观察，缺少官方统一规则和逐 Boss 数据。
- 早期社区报告 Electrocute 单 Hit 在 Unique 上会停在 96% 之类现象，可能属于旧版本行为/上限/Bug；当前 0.5.4f 不应直接沿用。

## 可复现实验

### 实验 A：Boss Freeze 衰减曲线

1. 选固定 Pinnacle、固定角色、无地图 Threshold Mod。
2. 用稳定非暴击 Cold Hit，记录首次一击 Freeze buildup B0。
3. 完成第一次 Freeze。
4. Freeze结束后在 t=0、1、2、3、4、6、8 秒分别重新开战测试单 Hit buildup。
5. 每个时间点至少重复5次。
6. 计算 `FreezeRecoveryRatio(t)=B(t)/B0`。

目标：得到实际反连冻恢复曲线，而不是猜“固定几秒/固定几倍”。

### 实验 B：Heavy Stun 独立保护

1. 使用固定 Physical Melee Hit。
2. 记录首次每击 Stun buildup。
3. Heavy Stun结束后按时间点测试再次 buildup。
4. 对 King in the Mists 特别测试0–4秒和>4秒，验证 PoE2DB `4000ms` 数据是否对应实机完全无法再次Stun，还是仅某类Stun保护。

### 实验 C：跨控制干扰矩阵

分别做：

- Freeze → Heavy Stun
- Freeze → Electrocute
- Heavy Stun → Freeze
- Heavy Stun → Electrocute
- Electrocute → Freeze
- Electrocute → Heavy Stun

记录第一种控制结束后第二种 buildup 是否下降/卡99%。这能回答“控制保护是各自独立还是共享”这一核心未知问题。

### 实验 D：Boss阶段免控表

对 Arbiter of Ash / Arbiter of Divinity逐技能录像，记录：

- buildup能否继续增长；
- 是否停99%；
- Primed技能能否触发；
- 动画结束后的首个Hit是否立即控制。

最终建立 `Boss × Skill/Phase × Freeze/Stun/Electrocute` 矩阵。

## 对 BD 的实际影响

- 控Boss构筑不能只看“+X% Freeze Buildup”面板，要看**首次控制时间、重复控制恢复曲线、Boss阶段覆盖率**。
- Physical Melee 在 Heavy Stun 方向天然具有很强的基础乘区；如果构筑本身能稳定近战命中，Stun投资可能比从零堆Freeze更便宜。
- Electrocute适合作为可规划的安全输出窗，但必须先确认技能有Electrocute资格；纯Shock构筑不能直接视为Electrocute构筑。
- 对阶段很多的Pinnacle，控制的价值取决于是否能在“危险且可控”的动作前把 buildup推到100%，而不是整场平均控制次数。

## 对做装的实际影响

- Freeze BD要区分 `Damage`、`Freeze Buildup`、`Ailment Application` 三种来源的边际价值；只在控制是瓶颈时专属 buildup 才可能优于纯伤害。
- Stun BD应优先评估 Physical/Melee天然倍率，再决定是否购买昂贵的Stun专属词缀。
- Boss专用装备比较应加入 `time-to-first-control` 与 `time-to-second-control`，而不只是DPS。

## 对 Farm 的实际影响

- 普通地图或Expedition词缀可显著提高Ailment/Stun Threshold，所以“控制型Farm BD”的稳定性会随地图词缀波动。
- 若主要收益机制依赖超级Rare/Runic Rare，控制能提高生存和站桩输出，但不应默认Pinnacle测试结果等于Rare怪结果。
- 对Boss Farm，控制减少死亡率的价值应进入风险调整EV/hour；一次5秒Electrocute/Freeze可能比少量纸面DPS更值钱。

## 资料冲突

- Wiki某些 Primed 页面仍混有旧门槛（Unique 80%）文本；0.2.0官方补丁明确把Unique改成70%，因此以官方0.2.0为准。
- PoE2DB Boss页面可显示技能级不可冻/不可打断标签，但很多Pinnacle的全局Ailment/Stun Threshold没有以可直接引用的形式暴露，不能自行补数字。
- 社区关于“所有CC共享4秒保护”的说法尚不足以升级为规则；目前只确认King in the Mists存在数据层4秒Stun后保护，Freeze本身则有GGG确认的独立反连冻机制。

## 当前结论

Pinnacle控制不是一个“把buildup堆到100”就结束的问题。正确模型是：

`控制可用性 = 技能资格 × 单Hit有效buildup / Boss Threshold × 当前重复控制衰减 × 当前阶段可控状态`

其中后三项都可能随Boss、时间与动作变化。当前能够稳定固化的是：Unique Primed=70%；Freeze存在反连冻衰减；Heavy Stun结束后有再控惩罚；Electrocute必须显式获得buildup资格。**每个Pinnacle的精确Threshold与跨CC共享保护仍必须实测，不能猜统一数值。**

## 下一次继续验证

按轮换进入“技能与辅助宝石”。优先研究：

**0.5.4f Trigger 技术语义矩阵：Cast/Trigger/Invocation/Meta Skill 对“你亲自使用”“Cast yourself”“Trigger yourself”、能量获取、Support适配、击杀归属和On-Hit/On-Cast条件的精确边界。**

Boss控制模块保留P0：

- Arbiter of Ash / Divinity 首次与第二次 Freeze buildup比值；
- Heavy Stun保护持续时间；
- Freeze/Stun/Electrocute 是否存在共享控制保护；
- 转阶段与特定技能的99% buildup锁定矩阵。
