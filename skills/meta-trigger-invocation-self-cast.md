---
id: KB-009
module: skills
status: DATA_VERIFIED
confidence: high
applies_to: "0.5.4f"
last_verified: 2026-08-22
tags: [trigger, meta, invocation, self-cast, energy, support-gems]
sources:
  - ggg-0.1.1-meta-energy
  - ggg-0.1.0d-coc
  - ggg-0.3.0-third-edict
  - poe2db-coc
  - poe2db-elemental-invocation
  - poe2db-barrier-invocation
  - poe2db-invocation
---

# Trigger / Meta Skill / Invocation / “你亲自施放”语义矩阵

## 适用版本
0.5.4f。0.5.5 已公布预告但尚未发布，因此本卡不预先套用未公开改动。

## 核心结论
1. **Triggered Skill 不是 self-cast。** 只要求普通 Spell/Hit/Area 等标签的辅助通常仍可作用于被触发技能；明确要求 `you cast yourself` / `you use yourself` 的辅助，不应作用于纯触发实例。
2. **Meta Skill 是容器与触发器，不等于被触发技能本体。** Meta 的 Energy、Reservation、Trigger 条件与插槽内技能的伤害/标签需要分层判断。
3. **Cast-on-X 与 Invocation 都是 Trigger，但触发时序不同。** Cast-on-X 达到最大 Energy 后自动触发并清空 Energy；Invocation 储存 Energy，玩家主动使用 Invocation 后消耗 Energy 触发插槽技能，并可在 Energy 足够时一次触发多次。
4. **0.1.1 后，放在 Meta Gem 内的技能不能再为 Meta 产生 Energy。** 这堵住了“触发技能反过来给自身/同类 Meta 充能”的自循环路线。
5. **被触发技能仍会支付其自身资源成本，不能因此视为 self-cast。** “资源由玩家支付”和“技能由玩家亲自施放”是两种不同技术语义。

## 判定流程
### A. 判断辅助是否作用于被触发技能
1. 确认辅助允许的技能标签（Spell/Attack/Hit/Area 等）。
2. 检查是否出现 `you cast yourself`、`you use yourself`、`cast yourself` 等限制。
3. 若有 self-use 限制，则纯 Trigger/Invocation 触发实例默认排除。
4. 若没有 self-use 限制，再检查 Triggered/InbuiltTrigger/Cooldown 等明确排除条件。
5. 最后才看 UI 是否允许插入；“能插”不等于所有子效果都满足条件。

### B. Meta Energy 与触发频率
- Cast on Critical 当前基础规则：每 0.1 秒插槽法术基础施法时间需要 10 最大 Energy；达到最大值时触发全部插槽法术并失去全部 Energy；插槽技能有 20% less Damage。
- CoC Energy 来自符合条件的 Critical Hit，并按敌人 Power 与该 Hit 相对敌人 Ailment Threshold 的比例修正。
- Elemental Invocation 最大 Energy 500；Freeze/Shock/Ignite 按各自规则产能，主动按 Invocation 后，插槽法术按每 0.1 秒基础施法时间消耗 10 Energy，可一次触发多次。
- Barrier Invocation 最大 Energy 500；敌人 Hit 造成 Energy Shield 损失时，每 10 ES 损失获得 1 Energy；主动 Invocation 后再触发。

## 计算例
若一个插槽 Spell 基础施法时间为 1.0 秒：
- Cast-on-X / Invocation 体系的基准 Energy 成本 = 10 × (1.0 / 0.1) = 100 Energy。
若 Invocation 当前储存 340 Energy，且只有这一枚 1.0 秒 Spell：
- 理论可连续触发 3 次并剩余约 40 Energy（忽略其它修正/特殊消耗）。

## 关键语义例子
### Considered Casting
文本要求 Spell `you cast yourself`。因此正常自施法可用；纯 Cast-on-X / Invocation 触发实例不应获得它的效果。历史上 UI/tooltip 曾出现误导或 bug 报告，不能以 tooltip 单独证明生效。

### Unleash
当前文本要求 Repeatable Spell `you cast yourself`，通过 Seals 在亲自施放时 Repeat。纯 Trigger 不满足 self-cast 条件，因此不能把“自施法版本可 Unleash”直接套到 Trigger 容器里的同名 Spell。

### Inhibitor
其文本是 `Skills you use or Trigger yourself`，这是非常重要的反例：GGG 会在文本中明确把“use yourself”和“Trigger yourself”并列。说明 Trigger-yourself 与 use/cast-yourself 是可区分的技术语义。

## 常见误区
- “由我的角色触发” = “我亲自施放” —— 错。
- “触发时扣我的 Mana” = “self-cast” —— 错。
- “Meta Gem 有 Spell 标签” = “插槽内所有 Spell 都继承 Meta 的所有辅助” —— 错。
- “辅助可以塞进技能组” = “一定对被触发技能有效” —— 错，必须读文本限制。
- “Invocation 是手动按键，所以插槽 Spell 算 self-cast” —— 错。你主动使用的是 Invocation；插槽 Spell 仍是被 Invocation Trigger。
- “被触发 Spell 可以继续给同一个 Meta 充能” —— 0.1.1 后错误。

## 例外条件
- 某些技能/辅助明确写 `Trigger yourself`，这种文本可以作用于玩家触发的技能，即使不是 self-cast。
- 某些技能是 Inbuilt Trigger 或内部子技能，需按其自身 Type/Excluded Type 判断。
- Invocation 本身是玩家主动使用的 Skill，但其触发的 socketed Skills 仍是 Triggered Skills。
- Ritual Cadence 会改变 Invocations 的触发节奏：改为每 2 秒触发技能，并降低被触发技能的 Energy 消耗；这属于 Invocation 的特殊规则，不能套到普通 Cast-on-X。

## 可复现实验
1. 同一 Spell 自施法 vs Cast on Critical 触发，分别插 Considered Casting，固定装备和敌人，比较单次 Hit 数值；预期仅自施法版本受益。
2. 同一 Spell 自施法 vs Elemental Invocation 触发，插 Unleash；观察是否积累/消耗 Seal；预期 Invocation 触发版本不形成 self-cast Unleash 行为。
3. 两个不同 Meta 同时启用，用外部自施法生成事件；记录二者 Energy。再让其中一个 Meta 触发高频 Spell，观察该触发 Spell 是否给任一 Meta 产能；依据 0.1.1 规则，Meta 插槽内技能不应产能。
4. Elemental Invocation 储存 300+ Energy，插入单一 1.0 秒 base cast time Spell，主动使用 Invocation，记录实际触发次数，验证 100 Energy/次基准。
5. Barrier Invocation 固定 ES、防御与敌人单次 Hit，记录损失 100/200/300 ES 时 Energy 增量，验证约 1 Energy/10 ES lost 的线性规则。

## 对 BD 的实际影响
- Trigger 构筑不能把自施法专属 Support 当成可用乘区；PoB/tooltip 如有异常必须实测。
- Invocation 构筑的关键不是单纯 Energy gain，而是 **Energy generation × storage × socketed base cast time × manual release timing**。
- Cast-on-X 更偏自动化频率；Invocation 更偏可控爆发与储能，尤其适合把 Energy 蓄到 Boss 可伤害窗口后一次释放。
- 触发技能不能给 Meta 自我充能，使无限 trigger loop 的基础假设失效；任何新 loop 必须来自 Meta 之外的事件源。

## 对做装 / Farm 的影响
- `increased Energy gained`、Spirit Reservation、技能等级、事件频率与基础施法时间共同决定 Trigger 吞吐量；不能只看触发 Spell 面板 DPS。
- 清图环境与 Boss 环境的 Energy 来源差异很大：Monster Power、ailment/crit事件频率不同，因此同一 Trigger 配置必须分别测 mapping trigger rate 与 boss trigger rate。
- Invocation 的手动释放允许避免把高价值触发浪费在普通怪或 Boss 无敌阶段，实际 Farm/ Boss Effective DPS 可能高于同面板自动 Cast-on-X。

## 资料冲突
- 2024-2025 早期论坛存在 Considered Casting 对 Trigger tooltip/伤害是否生效的矛盾报告；随后又有玩家报告补丁后不再生效。当前应以辅助文本 `you cast yourself` 与现行数据定义为准，旧 tooltip 行为视作历史 bug/误导，不作为规则。
- 社区曾观察多个 Meta 同时获得外部事件 Energy；这不与 0.1.1 冲突。0.1.1 禁止的是 **socketed skills in a Meta Gem** 产能，不是禁止同一外部事件被多个符合条件的 Meta 分别读取。该多 Meta 并行产能仍需 0.5.4f 实机复核后再升高置信度。

## 当前结论
Trigger 技术语义必须拆成三层：**谁产生事件 → 哪个 Meta 获得 Energy → 谁实际使用/触发插槽技能**。`self-cast/use yourself` 与 `Trigger yourself` 不是同义词；Invocation 的主动按键也不会把插槽 Spell 变成 self-cast。0.1.1 以后，Meta 插槽技能不能为 Meta 产能，因此任何循环都必须拥有容器外事件源。

## 下一次应验证
- 0.5.4f 下两个不同 Meta 是否仍能同时读取同一个外部 Crit/Ailment 事件并各自产能。
- `Trigger yourself` 对 kill attribution、on-cast、on-use、mana-spent 条件的逐词缀矩阵。
- Ritual Cadence 的逐技能 Energy consumption rounding 与多 Spell socket 顺序。
- 触发 Spell 的资源支付、Life/Mana cost 与 `when you spend Mana` 类效果是否计为玩家 spend，需逐条分离于 self-cast 语义。