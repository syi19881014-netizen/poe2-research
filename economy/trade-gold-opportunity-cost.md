---
id: KB-007
title: "0.5.4e 交易经济：Currency Exchange、Merchant's Tab 与 Gold 机会成本"
module: economy
status: DATA_VERIFIED
confidence: high
applicable_version: "0.5.4e"
last_verified: "2026-08-18"
source_tiers:
  - official
  - wiki
  - community
---

# 0.5.4e 交易经济：Currency Exchange、Merchant's Tab 与 Gold 机会成本

## 核心结论
POE2 当前存在两套经济上完全不同的自动交易通道：

1. **Merchant's Tab（异步物品交易）**：卖家挂牌和成交不支付 Gold；买家支付额外 Gold。只用于 Currency Exchange 不支持的物品。
2. **Currency Exchange（通货/可批量物品市场）**：发起订单时支付 Gold；Gold 成本取决于“想获得的物品”及数量。因而买入和卖出都可能消耗 Gold，只是 Gold 的计价对象不同。

因此 Gold 不是无价值 UI 费用，而是交易、倒货、批量做装和 Farm 变现必须进入 EV 的**不可交易影子成本（shadow cost）**。

## 官方规则
GGG 的 Asynchronous Trade FAQ 明确：
- Merchant's Tab 的 Gold 由买家承担；卖家挂牌/成交无 Gold 成本。
- Merchant's Tab 不能销售 Currency Exchange 已支持的物品。
- 收益进入 Ange 的 Earnings Tab。
- 调价/移除存在防滥用冷却与初始上架宽限。

0.3.0 正式加入该系统；截至 0.5.4e 未发现改变上述基本经济分工的官方补丁。

## Currency Exchange 判定流程
设订单为：

`I Have = A`，`I Want = B`

则 Gold 成本的可复用近似为：

`GoldCost = quantity(B) × unit_gold_cost(B)`

也就是说，Gold 取决于你**得到什么**，而不是简单取决于你“买还是卖”。

例：若用 Divine 换取 2000 Exalted，而 Exalted 当前规则表的单位 Gold 成本为 120，则：

`GoldCost = 2000 × 120 = 240,000 Gold`

这与社区实际订单报告吻合，可作为规则的交叉验证；但具体单位 Gold 表仍应在版本更新后复核。

## Gold 的影子价格
Gold 不能交易，因此不能简单写成 `1 Gold = X Divine`。应计算机会成本：

`ShadowValueGold = BestAlternativeNetProfitPerHour / GoldFarmedPerHour`

若某角色最优替代 Farm 净赚 8 Divine/h，并同时能稳定获得 400,000 Gold/h，则：

`1 Gold 的机会成本 = 8 / 400000 = 0.00002 Divine`

一笔 240,000 Gold 的交易，其机会成本约为：

`240000 × 0.00002 = 4.8 Divine-equivalent`

注意：这不是市场兑换价，而是该角色自己的时间机会成本。不同 BD、地图策略与玩家效率会得到不同数值。

## Currency Exchange 实际成交成本
单次订单真实成本应写成：

`EffectiveCost = MarketCurrencyCost + GoldCost × ShadowValueGold + Slippage + CapitalTimeCost`

若用于倒货，两腿都要计算：

`NetArbitrage = SellRevenue - BuyCost - GoldLeg1 - GoldLeg2 - Slippage - TimeRisk`

只有 `NetArbitrage > 0` 且单位时间收益高于替代 Farm，才是真正可做的套利。

## Merchant's Tab 的经济不对称
Merchant's Tab 的卖家没有 Gold 交易税，因此对高价值、非 Currency Exchange 物品：

- 卖家更适合长期异步挂牌；
- 买家才承担 Gold 摩擦；
- 倒货者买入时承担一次 Gold，但再次出售时自身不承担 Gold，下一位买家承担其购买 Gold。

因此 Merchant's Tab 倒货与 Currency Exchange 倒货不能使用同一套“双腿 Gold 税”模型。

## Grand Expedition：自己跑 vs 卖素材
对任何可交易 Expedition 入口/材料，决策不能只比较“掉落均值”和“卖价”。

### 卖素材
`EV_sell = MarketSaleValue - ExchangeGoldCost - Slippage - Listing/ExecutionTimeCost`

### 自己跑
`EV_run = ExpectedLootValue - InputOpportunityCost - JuiceCost - FailureLoss`

`EV_run_per_hour = EV_run / TotalRunTime`

当：

`EV_run_per_hour > EV_sell_per_hour`

才值得自己跑。

对于不可通过 Currency Exchange 处理、而经 Merchant's Tab 出售的物品，应把卖方 GoldCost 设为 0；对于 Currency Exchange 物品则不能忽略 Gold。

## 对批量做装的影响
批量做装常需要把高价值通货拆成大量低单位通货。例如 Divine -> Exalted、Essence、Rune、Omen。

此时即使市场兑换比例合理，Gold 也可能成为真正瓶颈。应先算：

`GoldPerCraftCycle = Σ(quantity_wanted_i × unit_gold_i)`

再判断当前 Gold 储备能支持多少轮。

因此“有足够 Divine”不等于“能无限批量做装”。Gold 是独立的 crafting throughput constraint。

## 常见误区
1. **“只有买家才花 Gold。”**——只对 Merchant's Tab 成立；Currency Exchange 发起卖出订单同样可能花 Gold。
2. **“Gold 免费掉，所以成本为零。”**——错。Gold 占用 Farm 时间，存在机会成本。
3. **“价差为正就能倒货。”**——错。必须扣除两腿 Gold、滑点、资本占用和成交时间。
4. **“Merchant's Tab 与 Currency Exchange 是同一套税制。”**——错，卖方 Gold 负担完全不同。
5. **“官方给出了 Merchant's Tab 精确 Gold 公式。”**——目前没有。Wiki/开发者问答只确认其与物品等级、稀有度/商店价格层级等因素有关，精确公式仍未知。
6. **“Expedition Artifact 仍是当前 0.5 交易核心。”**——错。旧 Expedition Artifacts 在 0.5.0 已被移出 Currency Exchange 并成为 legacy/drop-disabled 内容。

## 例外条件
- SSF 无 Merchant's Tab 异步交易。
- Merchant's Tab 无法出售 Currency Exchange 支持的物品。
- 特定旧 Expedition Artifacts 在 0.5.0 后已失效，不应加入当前 Farm EV。
- Currency Exchange 单位 Gold 表可能随补丁调整；任何长期计算器必须把单位 Gold 成本作为版本化输入，而非硬编码永恒常数。

## 可复现实验
### 实验 A：Currency Exchange Gold 线性关系
固定“想要”的物品 B，分别填写 1/10/100/1000 个，记录 Gold。验证 Gold 是否严格按数量线性变化。

### 实验 B：交换方向
A->B 与 B->A 分别下单，记录 Gold。验证费用跟随 `I Want` 物品，而非“买/卖”标签。

### 实验 C：Merchant's Tab 买方费用函数
选同一 Base、相同 ilvl，不同 rarity；以及同 rarity、不同 drop level 的物品，记录买方 Gold，建立经验回归。精确公式未公开，结果只能标 DATA_ESTIMATE。

### 实验 D：Gold 影子价
连续 30 张固定策略地图，记录净利润、Gold 和总时间，计算个人 `Divine/hour` 与 `Gold/hour`，由此得到该角色的 Gold shadow value。

## 对 BD / 做装 / Farm 的实际影响
- 高 Gold/hour 的 BD 不只是“顺便多金币”，而是拥有更高市场流动性与 crafting throughput。
- 批量制作、频繁换汇、低毛利套利应优先提升 Gold 获取效率。
- 高毛利非 Currency Exchange 装备适合 Merchant's Tab 长期异步出售，因为卖家无 Gold 成交税。
- Farm 策略比较时应新增指标：`Net Divine/hour after Gold opportunity cost`。

## 资料冲突
- GGG 已确认 Merchant's Tab 买家付 Gold、卖家不付；这是 OFFICIAL。
- Currency Exchange 的单位 Gold 表由 PoE2 Wiki 整理，可用社区订单反证/验证，但不是完整官方公式，标 DATA_VERIFIED 而非 OFFICIAL_FORMULA。
- Merchant's Tab 买方 Gold 的精确函数目前未知。Wiki 引述开发者问答称其与物品商店价格层级/等级有关；在拿到完整函数前禁止给出伪精确公式。

## 当前结论
POE2 的 Gold 应正式纳入经济模型。对任何倒货、批量做装、入口素材“跑还是卖”问题，后续默认计算 **市场价 + Gold 机会成本 + 滑点 + 时间 + 失败风险**。Merchant's Tab 与 Currency Exchange 必须分开建模。

## 下一次应继续验证
按轮换回到底层战斗规则：优先研究 **Pinnacle Boss 的 Freeze / Heavy Stun / Electrocute Threshold 与重复控制抗性**，重点区分通用 ailment 公式、Boss 数据字段、实机 buildup 和阶段重置行为。

## Sources
- GGG, Asynchronous Trade FAQ, 2025-08-25: https://www.pathofexile.com/forum/view-thread/3828185
- GGG, Content Update 0.3.0 — The Third Edict: https://www.pathofexile.com/forum/view-thread/3826682
- PoE2 Wiki, Currency exchange market: https://www.poe2wiki.net/wiki/Currency_exchange_market
- PoE2 Wiki, Asynchronous trading: https://www.poe2wiki.net/wiki/Asynchronous_trading
- PoE2 Wiki, Gold: https://www.poe2wiki.net/wiki/Gold
- PoE2 Wiki, Expedition Artifact: https://www.poe2wiki.net/wiki/Expedition_Artifact
