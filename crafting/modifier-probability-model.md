---
id: KB-004
module: crafting
status: DATA_VERIFIED
confidence: medium-high
applies_to: "0.5.x"
last_verified: 2026-08-11
tags: [crafting, modifiers, item-level, weight, omen, desecration]
sources: [ggg-050-patch]
---

# Modifier Pool、Item Level、Weight、Family 与做装概率模型

## 直接结论

POE2 做装概率必须从**当前合法词缀池**计算，而不是从“页面上有多少词缀”计算。

目标概率近似为：

`P(target) = sum(target legal weights) / sum(all legal weights)`

前提是已正确排除：iLvl 不合法、Base 不允许、Prefix/Suffix 不匹配、Family 冲突、当前工艺条件禁止的候选。

## 基础槽位

默认常规结构：

- Magic：最多 1 Prefix + 1 Suffix
- Rare：最多 3 Prefix + 3 Suffix

特殊 Rune/Base/系统可突破默认结构，必须单独检查。

## Item Level

高 iLvl 不一定更容易做：它会解锁高 Tier，也可能同时增加垃圾候选池。应优先寻找：

**Minimum Viable iLvl = 刚好解锁全部必须目标词缀的最低 iLvl。**

## Modifier Family

已有低 Tier 目标词缀可能同时：

1. 占用一个槽位；
2. 阻挡同 Family 更高 Tier；
3. 让后续 Exalt 无法自然升级该词。

## 0.5.x 制作框架

0.5.0 是当前制作体系的重要分水岭。知识库当前按以下原则工作：

- Recombinator 旧路线不作为当前实操默认方案。
- Crafted Modifier 与 Desecrated Modifier 的身份必须分开记录。
- Omen 的核心价值往往是**控制删除/新增方向与降低报废风险**，而不是直接提高目标 Weight。
- 每条 Weight 都要记录来源；不能默认 PoE2DB 展示的权重是官方客户端数据。

## 成本模型

对多阶段制作使用条件期望成本，而不是简单把所有步骤成本相加再除总成功率。

`Net Expected Cost = Gross Expected Craft Cost - Expected Salvage Value`

失败品残值必须计入。

## 标准做装输出

以后任何“这件怎么做”至少输出：

- 最优 Base / iLvl
- 目标 Prefix/Suffix
- Family 冲突
- Weight 可信度
- 每步合法性与概率
- 失败分支与修复路线
- 平均成本与风险分布
- 失败品残值
- 自做 vs 半成品 vs 成品购买阈值

## 待验证

- 当前各类 Weight 的来源覆盖率与可信度分级。
- 特殊 Runes 对 Prefix/Suffix 上限与池子的精确改变。
- 0.5.4f 当前所有 Crafted/Desecrated 交互边界。
