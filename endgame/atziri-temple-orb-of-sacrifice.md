# KB-012｜0.5.4f Atziri's Temple：入口链、双阶段Boss与Orb of Sacrifice

- 适用版本：0.5.4f 基线；核心改动来源为 0.5.4（2026-06-24/25）
- 专题模块：剧情、终局与 Boss
- 证据状态：DATA_VERIFIED / high for access flow and 0.5.4 drop rule; medium for exact drop-rate and some encounter edge cases

## 1. 核心规则

Atziri's Temple 不是“拿一张门票直接进Boss房”，而是一个由 Temple Console 规划的房间网络。要解锁 Boss，必须：

1. 通过房间布局通往 Architect's Chamber；
2. 击败 Xipocado, Royal Architect；
3. 使用 Xipocado's Console 放置 Royal Access Chamber；
4. 再通过房间布局通往 Royal Access Chamber；
5. 完成 Royal Access Chamber 后，Atziri's Chambers 才会真正解锁；
6. 进入 Atziri's Chamber，挑战 Atziri, the Red Queen。

关键判定不是“是否能走到 Atziri 房间”，而是“Royal Access Chamber 是否已经完成”。即使视觉上已经接近/连通，未完成该条件时 Boss 门仍不会开启。

击败 Atziri 后，必须把 Atziri's Medallion 带回入口处的检查点，才能开启 Atziri's Vault 与六个 Royal Trove 箱。Atziri 本体不是直接掉落全部专属物；主要奖励在 Vault 与 Trove 中结算。

## 2. 0.5.4 新增：Orb of Sacrifice

0.5.4 官方补丁新增：击败 Atziri 后，她的 Vault 有机会掉落 4 种新的 Orb of Sacrifice。其共同功能是：

- 升级物品上的 Corrupted Enchantment；
- 代价是随机移除一条 Explicit Modifier。

因此它不是“白嫖升级腐化附魔”，而是一个带不可逆词缀损失的风险型改造工具。使用前必须把目标物品看成：

`当前物品价值 + 腐化附魔增益 - 随机丢词损失`

## 3. Boss阶段与有效击杀模型

Atziri 有两个阶段：

### Phase 1：Atziri, the Red Queen

- 主要伤害类型：Fire / Lightning / Physical；当前资料记录三类抗性均约30%。
- 关键技能：Blood Spear、Spinning Flame Wall、Flameblast、Empowered Flameblast、Lightning Bolt、Lightning Spear、Storm Call。
- Blood Spear 会造成 Corrupted Blood 与 Maim；地面火焰会施加 Ignite。
- 当生命降至 10% 时，她会通过镜像传送进入 The Cradle，切换为第二形态并回满生命。

### Phase 2：Atziri, the Fell Serpent

- 生命条重新开始，不能按“第一阶段剩余10%”理解总有效伤害。
- Vaal Storm Call 会覆盖大部分场地，仅留下狭窄安全线。
- Flesh Bubble 在约20%生命时出现，最终覆盖大部分场地并造成高额、近乎致命的物理法术伤害；数据资料描述为该动画阶段可继续造成伤害。
- 约5%生命时进入无敌/过场，战斗结束。

因此更合理的真实击杀模型是：

`Real TTK ≈ Phase1有效伤害时间 + 强制位移/机制时间 + Phase2有效伤害时间 + 过场/不可伤害时间`

至少要按“两条生命段 + 一次强制换阶段”估算，不能用单一血条除以 PoB DPS。

## 4. 计算/判定流程

### 4.1 入口是否可打

`Royal Access Chamber 已完成` → Atziri's Chambers 解锁 → 可进入 Boss。

### 4.2 奖励是否已结算

`击杀 Atziri` → 获得 Medallion → 回到入口检查点 → 开启 Vault + 6 Troves。

如果只击杀而未完成 Medallion 交付，不应把本次视为完整收益结算。

### 4.3 是否值得用 Orb of Sacrifice

设：
- `V_upgrade` = 腐化附魔升级后的预期增值；
- `V_loss` = 随机移除一条显式词造成的预期损失；
- `C_orb` = Orb 本身机会成本；
- `p_useful` = 随机移除后仍保留可接受成品的概率。

则可用简化模型：

`EV = V_upgrade - C_orb - (1 - p_useful) × V_loss`

对已有 4~5 条高价值词缀、难以复制的装备，`V_loss` 往往很大；对已经有一条明显垃圾显式词的装备，风险相对可控。

## 5. 常见误区

1. 以为 Atziri 房间能走到就能打：错误，必须先完成 Royal Access Chamber。
2. 以为 Boss 只掉 Vault 专属物：错误，奖励还包括六个 Royal Trove 的货币/房间奖励。
3. 以为 Atziri 10% 后只是短暂过场：错误，这是第二形态的独立有效生命段。
4. 以为 Orb of Sacrifice 是安全升级：错误，它会随机移除 Explicit Modifier。
5. 以为旧版“Boss Bugged at 5%”可以直接当当前规则：早期社区报告不能替代当前版本验证。
6. 以为 Temple 中所有房间都会在 Boss 后保留：当前资料显示击杀后大量非奖励房间、Royal Access Chamber 与部分路径会 destabilise。

## 6. 例外条件与资料边界

- 0.4.0c Hotfix 5 曾调整 Temple 的怪物稀有度随 Temple 等级缩放，并把高等级角色创建的新 Temple 设为 Level 81；这属于旧版本历史背景，不能直接替代 0.5.4f 的当前数值。
- 0.4.0c Hotfix 6 修复过 Atziri 第二阶段偶尔无法死亡的问题，并让 Atziri 与 Architect 不再受 Vaal Temple 地图词缀影响。旧版本 bug 报告必须标注版本。
- Vault 中具体 Unique / Orb 的掉率，目前公开页面部分采用旧版本估计样本，不应当视为 0.5.4f 的官方概率。

## 7. 可复现实验

### 实验A：入口链验证

记录 5 次 Temple：
- 是否完成 Architect's Chamber；
- 是否完成 Royal Access Chamber；
- 是否能进入 Atziri's Chambers；
- 失败时门锁提示。

目标：验证“可达”和“已解锁”是两个独立状态。

### 实验B：两阶段有效伤害

固定一个可重复 Boss BD，记录：
- Phase1 开始到 10%；
- Phase 转换持续时间；
- Phase2 开始到 20%；
- Flesh Bubble 动画中实际可造成伤害的时间；
- 5% 过场前最后可伤害窗口。

目标：建立 Atziri 的 Real TTK，而不是木桩除血量。

### 实验C：Orb of Sacrifice 风险矩阵

准备不同词缀质量的腐化装备，记录：
- 原显式词数量；
- 是否存在明显垃圾词；
- Orb 使用后保留关键词概率；
- 附魔升级前后市场估值。

禁止在不可复制的高价值毕业装上直接做首测。

## 8. 对 BD、做装、Farm 的影响

### 对 BD

Atziri 不是纯单体站桩检测，而是“持续输出 + 大范围地面机制 + Corrupted Blood/元素伤害处理”的综合测试。移动中输出、远程覆盖、异常防护和短窗口爆发的价值高于纸面木桩 DPS。

### 对做装

Orb of Sacrifice 让“腐化附魔毕业装”出现新的风险决策层。后续做装不能只问“能否升级附魔”，还要问：随机丢一条显式词后，成品是否仍有可接受用途。

### 对 Farm

Temple 收益必须按整套流程计算：

`建庙/铺路成本 + 失败风险 + Boss耗时 + Medallion交付 + Vault/Troves奖励 + Orb/Unique期望价值`

不能只统计 Boss 房掉落。由于击杀后部分路径会 destabilise，准备阶段的房间规划本身也有机会成本。

## 9. 资料冲突与当前结论

- 官方 0.5.4 明确确认 Orb of Sacrifice 的新增与“升级腐化附魔、随机移除显式词”规则；这是最高优先级事实。
- Wiki 当前对 Atziri 房间链、两阶段技能和奖励流程描述较完整，但 Vault 具体掉率混有旧版本估计样本，降级为 medium。
- 社区仍有旧版本 Atziri 5% 无法死亡的报告；因官方在 0.4.0c Hotfix 6 已修复过相关 bug，不能把旧报告直接视为 0.5.4f 常态。

### 当前专家结论

Atziri's Temple 的核心不是“Boss 机械难度高”，而是一个**房间规划、解锁状态、双阶段 Boss、延迟奖励结算、以及带显式词损失的腐化附魔升级工具**组成的完整终局链。0.5.4 后，Atziri 的经济价值不应只按 Unique 掉落评价，还应把 Orb of Sacrifice 的风险调整 EV 纳入。

## 10. 下一次继续验证

1. 0.5.4f 下 Orb of Sacrifice 四种具体类型、对应附魔层级与实际掉率。
2. Atziri Vault 各 Unique/Orb 的最新市场价格与自刷 EV。
3. Atziri 两阶段是否存在仍未记录的控制免疫/阶段清除行为。
4. Temple 房间 destabilise 后，哪些路径/奖励房仍可安全回收。
5. 0.5.5 是否会改动 Fate of the Vaal / Atziri 的奖励与经济地位。

## Sources

- GGG official 0.5.4 Patch Notes: https://www.pathofexile.com/forum/view-thread/3975218
- PoE2 Wiki — Atziri, the Red Queen: https://www.poe2wiki.net/wiki/Atziri%2C_the_Red_Queen
- PoE2 Wiki — Temple of Atziri: https://www.poe2wiki.net/wiki/Temple_of_Atziri
- GGG 0.4.0c Hotfix 5/6 historical references for Temple/Atziri fixes
