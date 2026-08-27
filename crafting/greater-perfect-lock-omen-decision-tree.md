# KB-011 — Greater/Perfect Currency + Hinekora's Lock + Omen 做装决策树

- baseline: 0.5.4f
- researched: 2026-08-27
- status: DATA_VERIFIED
- confidence: high（Catalysing Exaltation 的具体权重倍率为 community-tested）

## 核心结论

1. 0.3.0 新增 Greater/Perfect Transmutation、Augmentation、Chaos、Regal、Exalted。Greater/Perfect 只对**本次新加入的 modifier**施加 Minimum Modifier Level，不会升级旧词缀，也不保证目标词缀/T1。
2. Greater Regal/Exalted/Chaos 的 Minimum Modifier Level 为 35；Perfect Regal/Exalted/Chaos 为 50。
3. Minimum Modifier Level 有重要例外：如果某 modifier type 的所有 tier 都会因门槛被排除，则至少保留该 type 可合法出现的最高 tier。因此 Perfect 并不会把低等级家族彻底从池中删除。
4. 目标词缀概率必须在“item level允许 + modifier family约束 + minimum modifier level过滤 + omen方向/标签约束”之后重新计算权重。
5. Omen of Sinistral/Dextral Exaltation 将下一次 Exalted 限定为 prefix/suffix；与 Omen of Greater Exaltation 联用时，两条新词缀都受方向限制。Greater Exaltation 也可和 Greater/Perfect Exalted Orb 同时作用。
6. Omen of Whittling 令下一次 Chaos 移除最低 modifier-level-requirement 的词缀（不是最低显示Tier），然后 Chaos/Greater Chaos/Perfect Chaos 再按各自新词缀池补一条。
7. Omen of Catalysing Exaltation 消耗全部 Catalyst Quality，提高对应 tag 的权重。当前 Wiki 引用 Prohibited Library 实测：20% quality ≈ 5x 对应权重，40% ≈ 7.5x；该倍率不是 GGG 官方公开公式，保持 COMMUNITY_TESTED。
8. Hinekora's Lock 在 PoE2 0.3.0 加入，可预览下一次 currency 对物品的结果；任何实际修改都会移除 foresight。它只适合“失败损失/成功增值”远高于 Lock 成本的终局步骤，不能因为能预览就当作廉价常规保险。

## 概率模型

设当前一次新增词缀的合法候选集合为 E，目标集合为 T，权重为 w_i：

P(target)=sum(w_i, i∈T∩E) / sum(w_j, j∈E)

其中 E 的生成顺序：

Base/Item Class → Item Level → Prefix/Suffix空位 → Family互斥 → Greater/Perfect Minimum Modifier Level → Omen方向限制 → Catalyst/tag等权重修正。

如果使用 Greater Exaltation 一次加入两条，需按**连续两次有条件的加权抽取**计算；第一条加入后会改变第二条的合法池（占用prefix/suffix、family互斥等），不能简单使用 `1-(1-p)^2`，除非验证两次抽取的池完全不变。

## Minimum Modifier Level 的关键例外

Perfect Exalted Orb（Min Mod Level 50）并不等价于“所有可能词缀都至少需要 ilvl50”。若某个 modifier type 的最高 tier 本身只要求例如 lvl30，而过滤后该 type 将完全没有候选，则最高合法 tier仍会保留。因此：

- Perfect 会显著减少许多低级 tier；
- 但不会保证消灭所有“低等级家族/低价值结果”；
- 更不会保证 T1；
- item level 仍决定高等级 tier是否本来就可出现。

## Chaos + Omen 判定

Omen of Whittling 判断的是 modifier 的**level requirement**，不是游戏界面显示的 Tier。若有并列最低 level 的多个 modifier，需要进一步实测/数据确认其选择规则；不要假设按 Tier 或词缀位置决定。

对近成品稀有物：

1. 先确认哪一条会被 Whittling 确定移除；
2. 再用 Perfect/Greater Chaos 决定新词缀的最低 modifier level；
3. 计算新合法池与目标概率；
4. 比较失败后的物品残值，不要只算成功概率。

## Hinekora's Lock 经济阈值

设 Lock 市价 C_L，成功结果相对当前物品的增值 ΔV_success，失败结果的损失 L_fail，普通直接 craft 成功率 p。

Lock 不是自动“划算”。最低要求是被保护步骤本身的风险价值与增值空间足以覆盖 C_L，并考虑拒绝预览结果后如何安全改变未来随机状态/物品状态的实际操作成本。

当前 US Realm PoE2DB 24h snapshot（2026-08-27附近）显示 Hinekora's Lock 约 1,400 Divine 量级，而 Perfect Exalted 约 2.1 Divine、Perfect Chaos 约 5.9–6.1 Divine。因此 Lock 目前属于 mirror-tier/超高端 craft 工具，不应纳入普通几十/几百 Divine 项目的常规步骤。市场数据必须按当天刷新。

## 常见误区

- “Perfect Orb = T1 Orb” → 错。
- “Minimum Modifier Level 50 会把所有 lvl<50 的 modifier family 全删掉” → 错，有保底家族例外。
- “Perfect Chaos 会保护现有好词缀” → 错，它仍随机移除，除非 Omen改变移除规则。
- “Whittling 会删最低Tier” → 错，删最低 modifier level requirement。
- “Greater Exaltation 两条命中率直接=1-(1-p)^2” → 通常不严谨，第一条会改变第二条池。
- “Catalyst 20% 就是20%更多目标权重” → 错；当前社区实测远高于线性，但倍率需版本复测。
- “Lock 能预览，所以所有终局 craft 都应该用” → 错，先做经济阈值。

## 可复现实验

1. **Minimum Modifier Level保底家族实验**：选择拥有最高tier仍低于50的 modifier type 的高ilvl base，用大量 Perfect Exalted/Regal 样本验证该家族最高tier仍能出现。
2. **Whittling并列实验**：制作两个词缀拥有相同最低 modifier level 的稀有物，反复用 Whittling + Chaos 记录删除选择，验证并列规则。
3. **Catalysing权重实验**：同base、同pool下做0/20/40% Catalyst三组至少500次新增词缀样本，估计 tag 权重倍率。
4. **双Exalt条件池实验**：Greater Exaltation + Sinistral/Dextral，记录第一/第二条词缀family，验证第二次抽取池如何因第一条改变。
5. **Lock预览边界实验**：逐类测试 Perfect Exalted/Chaos、Omen联用、Vaal/Fracturing等是否可预览，并记录拒绝结果后哪些轻量修改会消耗 foresight。

## 对 BD / 做装 / Farm 的影响

- BD：高端毕业装备的成本应从“买词缀”升级为“购买有效候选池 + 保护失败损失”。
- 做装：Perfect Currency 最强的价值通常不是提高单个目标 tier，而是**删除大量低tier权重**；必须先跑合法池再决定是否值价差。
- Farm：Perfect Currency、Hinekora's Lock 与高价值 Omens 的掉落/交易价值来自 endgame crafting demand；在 fresh economy 或0.5.5后其价格可能剧烈重估，不可把本卡市场snapshot长期固化。

## 资料冲突与证据等级

- OFFICIAL：0.3.0 新增 Greater/Perfect Currency；其作用是各自具有 Minimum Modifier Level。
- DATA_VERIFIED：Greater=35、Perfect=50（Regal/Exalted/Chaos）；Whittling、Sinistral/Dextral、Greater Exaltation具体文本；Hinekora's Lock存在且可预览下一Currency。
- COMMUNITY_TESTED：Catalysing Exaltation 20%≈5x、40%≈7.5x对应tag权重。
- NEEDS_RETEST：Whittling并列最低level选择；Lock与所有0.5.4f currency/Omen组合的精确预览边界；Catalyst倍率是否在0.5.4f完全不变。

## 下一次应验证

按轮换进入“剧情、终局与 Boss”：优先研究 0.5.4f Fortress → Arbiter of Divinity 的 Atlas 自动完成/Passive Point 奖励、Quest 与 repeatable 路径及版本化掉落池，并准备在0.5.5正式公告后优先Diff任何Boss改动。
