# KB-010 — 0.5.4f Meta Energy / Invocation 被动、Invoker 与 Breakpoint

- **适用版本**：0.5.4f
- **核验日期**：2026-08-25
- **状态**：DATA_VERIFIED
- **置信度**：high（Ritual Cadence 的若干实战行为仍单列 NEEDS_RETEST）
- **模块**：职业、升华与被动树

## 核心结论

Meta/Invocation 构筑不能把“increased Energy”“more Energy”“Maximum Energy”“Energy refund”“consume half Energy”视为同一种属性。它们分别改变充能速度、离散触发 breakpoint、储能上限和单位 Energy 的触发次数。

### 1. Energy gain 计算

设某事件基础获得 `E0` Energy，所有 increased Energy 合计为 `I`，more Energy 乘区为 `M`：

`E_event = E0 × (1 + I) × M`

Invoker 升华 `The Soul Springs Eternal` 当前给予：

- Meta Skills gain 35% more Energy
- Meta Skills have 50% increased Reservation Efficiency

因此 Invoker 的 Energy 乘区为 `1.35`，不是与普通 increased Energy 相加。

例：基础每事件 10 Energy，树上/其它来源共 40% increased Energy：

`10 × 1.40 × 1.35 = 18.9 Energy/event`

若本次触发需要 100 Energy，则实际事件数为：

`ceil(100 / 18.9) = 6`

而无任何 Energy 增益时需要 10 次事件。因此 Energy 节点的实际 DPS 价值应按“是否跨过整数事件 breakpoint”评价，而不是只看面板百分比。

### 2. Reservation Efficiency 不是 less Reservation

Reservation Efficiency 使用除数：

`Final Reservation = Base Reservation / (1 + total increased Reservation Efficiency)`

所以 The Soul Springs Eternal 的 50% increased Reservation Efficiency 单独作用时：

- 30 Spirit → 20
- 60 Spirit → 40
- 100 Spirit → 约67

它不是“预留减半”；需要 100% increased Reservation Efficiency 才会把基础预留减为 50%。

## 当前关键被动/节点

### The Soul Springs Eternal — Invoker

- 35% more Meta Energy：强独立乘区，尤其容易跨 Energy/event breakpoint。
- 50% increased Reservation Efficiency：0.4.0 新增；同时运行多个 Meta Skill 时可能等同于释放一个额外 Persistent/Meta 槽位。

**判断**：对真正依赖 Meta Energy 的构筑是核心升华，而不是单纯“35% more DPS”。收益要用触发间隔和 Spirit 预算分别计算。

### Dynamism

- 40% increased Damage if you've Triggered a Skill Recently
- Meta Skills gain 15% increased Energy

其 15% 属于普通 increased Energy；与其它 increased 相加，再与 Invoker 35% more 相乘。

### Evocational Practitioner

- 25% increased Critical Hit Chance if you've Triggered a Skill Recently
- Meta Skills gain 25% increased Energy if you've dealt a Critical Hit Recently

Energy 部分是条件增益。若 generator 本身稳定暴击，则可以近似视为常驻；若 Boss 开场、低暴击或机制期断档，则不能直接按常驻计算。

### Energise

- 25% chance for Trigger skills to refund half of Energy Spent

若每次原始支出为 `C`，且退款事件独立，长期期望净 Energy 支出：

`0.75C + 0.25×0.5C = 0.875C`

即仅从期望值看，相当于每单位 Energy 可支持约：

`1 / 0.875 = 1.1429`

约 14.3% 更多触发次数。

但短 Boss 战中波动明显，应同时报告平均值与低roll风险。

### Invocated Echoes

- Invocated Spells have 40% chance to consume half as much Energy

长期期望 Energy 支出：

`0.60C + 0.40×0.5C = 0.80C`

理论上等价于单位 Energy 触发次数上限约提高：

`1 / 0.8 = 1.25`

即约 25%。这是“单位 Energy 效率”节点，不直接增加 Energy gain。

### Invocated Limit

- Invocated Skills have 30% increased Maximum Energy

它提高 burst storage，不提高 Energy/sec。若角色通常在达到较低 Energy 后立刻释放，则价值可能接近零；若 Boss 有长时间不可伤害阶段、需要屯能后一次爆发，则价值显著。

推荐新增指标：

`StoredBursts = floor(MaxEnergy / EnergyCostPerInvocation)`

并比较加点前后是否多出完整一次触发。

### Ritual Cadence — Keystone

官方 0.3.0 添加。当前文本：

- Invocation Skills instead Trigger Spells every 2 seconds
- Invocation Skills cannot gain Energy while Triggering Spells
- Invoked Spells consume 50% less Energy

它不是简单“Invocation 伤害翻倍”。应拆成：

1. 单次 invoked spell 的 Energy 消耗乘 0.5，因此同一储能理论上可支持约 2 倍触发次数；
2. 触发被时间化为每 2 秒一次，释放吞吐存在 cadence 上限；
3. Invocation 正在触发 Spells 时无法继续获得 Energy，因此放电阶段存在 generation downtime；
4. 因此它偏向“长时间平滑释放”，而普通 Invocation 偏向“手动屯能后瞬时爆发”。

对短 Boss vulnerability window，Ritual Cadence 可能反而降低爆发价值；对持续站桩、长战斗或希望降低操作频率的构筑，它可能提高 Energy 利用率。

## Breakpoint 判定流程

1. 确定 socketed Skill 的单次 Energy 成本 `C`。
2. 确定 generator 每个有效事件的基础 Energy `E0`。
3. 汇总普通 increased Energy：`I = Σ increased`。
4. 再应用所有 more/less Energy 乘区。
5. 计算 `E_event`。
6. 计算事件数：`N = ceil(C / E_event)`。
7. 加/减一个节点后重新计算 `N`。如果 `N` 没变化，该节点对当前触发频率可能只有溢出/稳定性价值；如果从 6 次事件降到 5 次，则实际触发速度提升约 20%，明显高于节点面板数字。
8. Invocation 还需分别计算 Maximum Energy、Energy refund/half-consumption 与释放时间窗口。

## 常见误区

- “35% more Energy = 35% more DPS”：错误。只有在 Energy 是唯一瓶颈且没有整数 breakpoint、CD、目标事件频率等限制时才接近。
- “50% increased Reservation Efficiency = 50% less reservation”：错误。100 Spirit 约变67，而不是50。
- “Maximum Energy = Energy gain”：错误。前者只提高储能池。
- “Ritual Cadence 的 50% less Energy = 2倍瞬发”：错误。它把释放拆成每2秒一次，并且触发期间停止充能。
- “所有 increased Energy 节点独立乘算”：错误。普通 increased 先相加；Invoker 的 35% more 再独立相乘。
- “条件 Energy 节点在 Boss 开场必定常驻”：错误。需要先满足 Recently/Crit 等条件。

## 例外与边界

- Energy gain 与消费若基于 Skill use time，Total use time 修正会以特殊方式参与 Energy 计算；不能直接拿面板 cast time 做线性换算。
- Triggered Skill 的直接效果不能反向为 Meta 产生 Energy（0.1.1 后规则）。
- 多个 Meta Skill 各自拥有独立 Energy 池；同一外部事件是否会同时喂多个 Meta，在当前版本应继续实测确认具体事件类型。
- Ritual Cadence 对带 Cooldown 的 socketed Spell、换武器、远距离移动/重新瞄准曾有历史 bug 报告。0.5.4f 下这些行为尚未得到足够的新实测，不作为稳定规则。

## 可复现实验

### A. Energy breakpoint
固定同一 generator 与同一 Boss，分别测试：
- 无 Energy 节点
- +15% increased
- +40% increased
- Invoker 35% more
- increased + Invoker more

记录每次事件增加的 Energy 和达到一次触发所需事件数。

### B. Reservation Efficiency
用基础 30/60/100 Spirit 的 Meta Skill，记录 0%、50%、100% total increased Reservation Efficiency 下的实际预留，验证除数公式。

### C. Ritual Cadence 吞吐
固定 500 Energy 和 100 Energy/次 Spell，对比普通 Invocation 与 Ritual Cadence：
- 总触发次数
- 首次触发延迟
- 完成全部释放所需时间
- 释放阶段能否继续获得 Energy

### D. Invocated Echoes / Energise
至少 200 次触发记录实际 half-cost/refund 命中率与总 Energy 消耗，比较理论期望 0.8C / 0.875C，并记录短战斗方差。

## 对 BD 的影响

Meta 构筑的节点排序应从“百分比大小”改成 breakpoint 优先：

`真实价值 ≈ 触发频率变化 × 单次触发伤害 × 有效目标时间`

当 +15% Energy 足以把 7-event breakpoint 降到 6-event 时，它可能比 40% increased spell damage 更强；反之若触发事件数不变，伤害节点可能更好。

Invoker 的 The Soul Springs Eternal 同时解决 Energy throughput 与 Spirit budget，因而对多 Meta 构筑价值通常高于单纯伤害节点，但必须确认构筑确实受这两个资源限制。

## 对做装的影响

装备上的 Spirit、Reservation Efficiency、Meta Energy 等词缀应按“能否多开一个关键 Persistent Skill / 能否跨一个 Energy breakpoint”定价，不能使用统一的 DPS-per-mod 模型。

## 对 Farm 的影响

清图环境中事件密度高，Energy gain 往往容易过量，节点价值可能转向 Reservation 或伤害；Pinnacle 单体环境事件源稀疏，Energy more/increased 的价值通常更高。因此同一 Trigger/Invocation 构筑可能需要 mapping 与 boss 两套树/装备取舍。

## 资料冲突

- 社区曾误解 50% increased Reservation Efficiency 应把 60 Spirit 降到30；当前机制公式明确实际为40，因此该类“bug”报告属于公式误解。
- Ritual Cadence 历史版本存在移动后中断、换武器中断、固定旧目标、带 Cooldown Spell 行为异常等报告。官方文本能确认设计规则，但不能证明这些历史实现问题在0.5.4f全部消失。

## 当前结论

1. Meta Energy 节点必须按离散 breakpoint 评价。
2. Invoker `The Soul Springs Eternal` 的 35% more Energy 是独立乘区；50% increased Reservation Efficiency 使用除数公式。
3. `Dynamism` / `Evocational Practitioner` 提供 increased Energy；与 Invoker 的 more 乘算。
4. `Energise` / `Invocated Echoes` 主要提高单位 Energy 的长期触发效率；`Invocated Limit` 主要提高 burst storage。
5. `Ritual Cadence` 是“释放模型转换”Keystone，不是简单的2倍伤害节点。

## 下一次继续验证

按轮换进入“装备、词缀与做装”。优先专题：**0.5.4f Greater / Perfect Currency + Hinekora's Lock + Omen 的目标词缀做装决策树**，重点验证最低/最高 modifier level 约束、合法词缀池变化、成本模型与失败品残值。
