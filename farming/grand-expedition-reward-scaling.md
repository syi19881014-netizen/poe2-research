---
id: KB-006
title: "0.5.4 Grand Expedition：Remnant、Runic Modifier 与收益放大模型"
module: farming
status: DATA_VERIFIED
confidence: high
applicable_version: "0.5.4e (0.5.4 mechanics + Hotfix 1-4; later maintenance does not change this model)"
last_verified: "2026-08-15"
primary_sources:
  - ggg-054-patch
  - ggg-054-hotfix3
secondary_sources:
  - poe2wiki-expedition
  - poe2db-atlas-expedition
  - community-koni-grand-expedition-054
  - community-fubgun-grand-expedition-054
---

# 0.5.4 Grand Expedition：Remnant、Runic Modifier 与收益放大模型

## 核心结论

0.5.3→0.5.4 后，Grand Expedition 已从“尽量炸更多目标”的简单机制，变成一个明显的**路径依赖收益系统**：Waystone Tier 决定 Remnant 上限，Grand Expedition 自带 1–2 个地图修正，专属 Atlas Tree 可将其提高到 3 个；Remnant 会把被选中的 Rune/Runic Modifier 传播到后续目标，Runic Modifier 数量又可继续放大怪物掉落数量与 Logbook 概率。因此最优路线不是单看某一个 Remnant 的即时奖励，而是最大化“高价值传播效果 × 后续 Runic Monster 数量 × 可承受难度”。

## 官方已确认 / 数据站可验证

### 0.5.3 基线改变

- Grand Expedition 的最大 Remnant 数量随 Waystone Tier 增加，T15+ 达到最高档。
- Grand Expedition 炸药数量从 20 降为 15。
- 普通武器/护甲箱被移除，箱子价值向 Currency、Unique、Waystone、Mysterious/Trinket 高稀有度箱倾斜。
- Runic Inscriptions 给怪物带来的奖励增益在多数情况下被翻倍，部分提升更多。

### 0.5.4 结构改变

- 新增独立 Expedition Atlas Passive Tree。
- Grand Expedition 默认获得 1–2 个 Expedition Map Modifiers；可出现：更多 Runic Monster Markers、Runic Monsters Duplicated、额外 Remnants 等。
- `The Quest Continues`：Grand Expedition 最多可有 3 个 Modifiers，并获得 +1 Area Level。
- Remnant 不再按旧 recipe 随机决定传播哪条 Rune；现在会随机选择一个 Rune slot 传播，并在界面高亮显示，因此玩家可以在放炸药前据此规划路径。
- Rare Runic Monster 的出现概率现在正确受到 Monster Rarity / Rare chance 类增益影响。

### Expedition Atlas 的关键收益节点

- `Gaining Traction`：Verisium Remnants 每完成一个 Remnant，获得 50% increased Monster Rarity。Hotfix 3 之前该效果曾以隐藏区服修正存在；Hotfix 3 移除隐藏版本，并把收益正式放到此节点。界面一度错误显示 25%，实际值为 50%。
- `Sown Seeds`：Runic Monsters 每个 Runic Modifier 获得 50% increased chance to drop Logbooks。
- `Calculated Investment` 可选择：每个 Runic Modifier +1% increased Quantity of Items dropped by Monsters；或 25% chance for Remnants to count as affected by a Power Rune；或经验路线。
- `Double or Nothing` 可选择 25% chance 额外传播一个 Runic Modifier、完全不传播、或保持单传播。
- `Strategic Advantage` 可让 Runic Monsters 生成时额外缺失 20% Life，或加快爆破链推进。
- `Cultivate the Sea` 可把 Ocean/Island 同时视为 Water/Mountain/Grass/Forest/Swamp/Desert 中的一种，从而与主 Atlas 的 biome 节点联动。
- Expedition 小节点提供 Runic Monster Logbook quantity 增益。

## 判定与计算流程

### 1. 先判断地图层级

优先 T15+，因为 0.5.3 已确认 Remnant 上限在 T15+ 达到最高档。若已配置 `The Quest Continues`，再把 +1 Area Level 的底材/掉落价值纳入收益，而不是只看怪物掉落。

### 2. 扫描整张 Grand Expedition，再落炸药

记录：

- 高价值 Remnant / 高价值可传播 Rune；
- Rune 数量多的 Remnant；
- Runic Monster Markers 数量；
- 地下区域；
- Boss；
- 当前 Map Modifier（尤其 duplicated Runic Monsters / more markers / additional remnants）。

不要按看到的第一个好 Remnant 直接开链。

### 3. 区分“传播源”与“收割目标”

若某 Remnant 高亮传播的 Rune 本身能显著提高后续怪物/奖励，则它的真实价值约等于：

`传播价值 ≈ Rune效果 × 之后仍会吃到该效果的 Runic Monsters/Remnants 数量`

因此高价值传播源通常应偏前；本身 Rune 数量很多、Boss、密集 Runic Marker 区域通常更适合作为后段收割目标。

### 4. Runic Modifier 的相对收益模型

设某批 Runic Monsters 最终拥有 N 个 Runic Modifiers：

- 选择 `Calculated Investment: Quantity` 时，相对 Item Quantity 贡献为 `+N% increased Quantity`。
- 有 `Sown Seeds` 时，Logbook drop chance 获得 `+50N% increased chance`。

因此可用一个相对模型比较两条路径：

`Logbook EV ∝ RunicMonsterCount × BaseLogbookChance × (1 + generic increased chance + 0.50N) × (1 + Logbook quantity modifiers)`

这里用于**相对路线比较**，不是官方公布的绝对掉率公式；BaseLogbookChance 当前没有可靠公开值。

### 5. Gaining Traction 的路径依赖

若先完成 R 个 Remnants，再进入主要收割段，则该节点对应的累计 increased Monster Rarity 为约：

`+50% × R`

因此后段高密度 Runic Monster/Boss 区域理论上比把它们放在开头更能吃到该节点收益。但必须和后续怪物被叠加的危险 Runic Modifiers一起权衡。

### 6. 风险调整后的实际收益

`实际 EV/h = (期望掉落价值 - Logbook/Waystone/Tablet/Liquid Verisium 等投入 - 失败损失) / 总耗时`

极限 juice 不等于最优：若额外稀有怪效果使清怪速度显著下降或死亡/丢图概率上升，收益每小时可能反而降低。

## 常见误区

1. **Remnant 越多，只要全炸到就行。** 错。0.5.4 的传播槽位已可见，爆破顺序会改变后续目标拿到的 Runic Modifiers。
2. **高价值 Rune 应该最后炸。** 若它是高价值“传播效果”，通常越早越能覆盖更多后续目标；高 Rune 数量本身与高价值传播效果必须区分。
3. **不开 Gaining Traction 也天然每完成 Remnant +50% rarity。** 这是 0.5.4 Hotfix 3 前的隐藏行为，已被移除；当前这项收益来自专属 Atlas 节点。
4. **Pack Size 与 Rare chance 是同一种收益。** 不是。0.5.4 明确修复的是 Runic Monster rare chance 对 Monster Rarity/Rare chance 的缩放；Pack Size 是否直接增加 Rune/Runic Marker 奖励应单独验证。
5. **社区一张 40d+ 地图说明平均每张都值几十 d。** 错。这是尾部样本，不是均值；应记录至少 30–100 次样本并扣除投入。
6. **地图越难收益必然越高。** 只有能稳定清完并保持高 uptime 才成立。

## 例外条件

- `Doryani's Refined Formula` 可把 Grand Expedition 的炸药数量改成 5，属于特殊玩法，不能拿普通 15 炸药路线直接套。
- Liquid Verisium 可以重置/启动带随机 Runic Inscription 的 Remnant，但 reroll 后的具体可选结果具有随机性，不能假定能稳定定向出目标 Rune。
- 地下区域曾存在生成/爆破相关 bug；0.5.4e Maintenance 已修复 Grand Expedition 地下区域不生成的问题，因此更早的地下收益样本可能偏低。
- Hotfix 3 前后的 rarity 数据不可混样。

## 社区实测（非官方规则）

0.5.4 高端玩家普遍采用：T15/T16 高难 Waystone + 高 Monster Effectiveness / Rare Monster density + Expedition Atlas quantity/Power Rune/biome 联动。社区路线常选 Desert 以放大 Rare Monster 相关收益；也有人用 Forest 降低难度。

可靠高端样本显示极限 juice 地图可以出现非常高的 raw Divine 尾部结果，但同时稀有怪有效生命和伤害会急剧上升，属于高预算、高失败成本 Farm。应把“几十 Divine 单图”视为上尾案例而非稳定基线。

社区实操还普遍建议：先扫完整张图，优先识别高价值传播 Rune；高价值传播 Remnant 置前，高 Rune 数量/Boss/密集怪区置后。该排序与 0.5.4 的高亮传播机制相符，但不同 Rune 的精确价值仍需逐项统计。

## 可复现实验

### 实验 A：Gaining Traction 实际 50% 验证

1. 固定同一档 Waystone、相近 monster mods。
2. 一组不点 Gaining Traction，一组点满。
3. 分别记录第 1、3、5、8 个 Remnant 后主要 Runic Monster 段的 rare loot 分布。
4. 至少 50 张图，记录 raw currency、rare item count、high-tier currency。
5. 不把 Hotfix 3 前数据混入样本。

### 实验 B：Sown Seeds 的 N-mod Logbook 曲线

按 Runic Monster 最终拥有的 Runic Modifiers 数 N=0/1/2/3/... 分组，记录：

- Runic Monster 数；
- Logbook 掉落数；
- generic logbook quantity；
- map rarity/effectiveness。

至少每组 500 个 Runic Monsters，比较 `logbooks / runic monsters` 是否符合 +50% increased chance per mod 的相对梯度。

### 实验 C：Pack Size 是否影响 Rune loot

保持 Runic Marker/Remnant/rarity/effectiveness接近，做高 Pack Size 与低 Pack Size两组，每组至少 30张，分别记录：

- Runic Monster 数；
- Rune recipe drops；
- raw currency；
- Logbooks；
- 非 Expedition 普通怪掉落。

用于验证社区“Pack Size 对 rune loot 无价值”的说法究竟是完全无效还是只是不如 rarity/effectiveness。

### 实验 D：传播顺序

选择具有相同 Remnant 集合的可比布局，分别执行：

- 高价值传播 Rune 前置；
- 高价值传播 Rune 后置。

录像并记录每段最终 Runic Modifiers、怪数和掉落，以建立 Rune 的边际传播价值表。

## 对 BD 的实际影响

- Grand Expedition 的 BD 门槛应按“高稀有怪 burst + 高 monster effectiveness + ailment/control”评估，而非普通 T15 清图 DPS。
- 高 juice 时，持续移动输出、范围覆盖、对 Rare/Unique 的单体收尾和 Freeze/Chill 等异常防护价值上升。
- 若 build 清图很快但无法稳定处理叠加多 Runic Modifiers 的 Rare，应该主动降低 effect/rare juice，而非机械复制顶级玩家配置。

## 对做装的实际影响

`The Quest Continues` 的 +1 Area Level 与 T15/T16/irradiation 等组合会改变高 ilvl/特殊底材的可获取性，因此 Grand Expedition 不只是 raw currency Farm，也可以纳入高等级底材获取模型。具体哪些底材需要哪一档 area level，应在做装问题中按目标 affix / base 单独计算。

## 对 Farm 的实际影响

当前最重要的优先级不是“更多 Pack Size”，而是先保证：

1. T15+ Remnant 上限；
2. Expedition Atlas points；
3. 高价值 Map Modifiers（更多 Runic Markers / duplication / additional Remnants）；
4. 能被后续大量怪物继承的优质传播 Rune；
5. Rare chance / Monster Rarity / Effectiveness 与角色承受能力的平衡；
6. 再优化 Liquid Verisium、biome、tablets 和高成本 Waystone。

低预算玩家应优先做稳定版本；只有角色死亡率接近 0 且高稀有怪击杀时间足够短时，才值得切到极限 juice。

## 资料冲突与当前结论

- 0.5.4 Hotfix 3 是最大的资料分界线：Hotfix 前“隐藏每 Remnant +50% rarity”与 Hotfix 后 `Gaining Traction` 的显式效果不能混为一谈。
- 社区对 Pack Size 的评价偏低，但目前缺乏严格对照实验，暂不升级为稳定机制结论。
- 社区极端收益案例说明上限很高，却不能代表均值；绝对 d/h 必须结合当日市场价格重新测。

**当前结论：Grand Expedition 的核心收益变量是路径依赖。** 最优决策应最大化高价值 Runic Modifier 对后续 Runic Monster 的覆盖，同时利用专属 Atlas 的 per-Remnant rarity 与 per-Runic-Modifier quantity/logbook scaling；任何收益最大化都必须经过死亡率和清怪时间的风险调整。

## 下一次继续验证

按轮换顺序进入“市场经济与构筑案例”，优先研究：

**0.5.4e 当前交易环境下，Grand Expedition 的投入品（Logbook/Aldur Saga、Liquid Verisium、Waystone/Tablets）与核心产出（Divine、Logbook、Runes、Alloys）的 EV / opportunity cost 模型；建立‘自己跑 vs 直接出售门票/素材’的实时决策公式。**

本模块后续待验证：

- Pack Size 对 Rune/Runic Monster 专属掉落的真实影响；
- 各 Rune/Runeshape 的独立收益权重；
- Power Rune 与 Double or Nothing 的长期 EV；
- 不同 biome（Desert/Forest等）在相同预算和角色强度下的收益/死亡率边界；
- Hotfix 3 后至少 100 张 Grand Expedition 的稳定 d/h 样本。
