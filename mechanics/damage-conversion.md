---
id: KB-001
module: mechanics
status: DATA_VERIFIED
confidence: high
applies_to: "0.5.x"
last_verified: 2026-08-13
tags: [damage, conversion, gain-as-extra, ailments]
sources: [poe2db-damage-conversion]
---

# 伤害转换与 Gain as Extra 两阶段结算

## 直接结论

POE2 的 Damage Conversion 采用两阶段：**技能自身转换先结算，其他来源转换后结算**。转换后的伤害只按最终伤害类型缩放，不继续吃旧伤害类型的全局增伤。Damage over Time 不能被转换。

Damage Gained as Extra 与转换采用同类两阶段思路；新增部分保留原始伤害，但额外部分按新类型缩放。

## 判定流程

1. 确定基础伤害组成。
2. 执行技能自身 Conversion。
3. 执行技能自身 Gain as Extra。
4. 执行装备/被动/升华等非技能来源 Conversion。
5. 执行非技能来源 Gain as Extra，并检查是否存在明确特殊顺序。
6. 对最终各伤害类型应用对应增伤、抗性、穿透与异常状态规则。

## 关键误区

- 不得沿用 POE1 的“转换后同时吃来源类型和最终类型全局增伤”思路。
- 本地武器 `% increased Physical Damage` 与全局 `increased Physical Damage` 必须分开：前者可能先提高武器基础物理，再被转换。
- “Gain 20% as Extra”不等于固定 20% more，最终收益受敌人抗性、穿透、后续转换和可用缩放影响。

## 超额转换

同一阶段多个来源总转换超过 100% 时，需要进一步按当前规则验证比例缩放与内部取整。该边界目前保留 `NEEDS_RETEST` 子问题。

## 可复现实验

- 100% 火转冰后分别加入同数值 Fire Damage 与 Cold Damage，比较最终伤害。
- 技能自带额外闪电 + 装备 100% 闪转冰，观察感电/冻结与伤害组成。
- 对 DoT 单独测试 Gain as Extra 是否影响持续部分。

## 对构筑/做装的影响

转换 BD 的核心估值必须围绕**最终伤害类型**；穿透、Exposure、异常状态和全局增伤不能只看来源类型。复杂武器应先拆本地基础伤害，再评价全局词缀。

## 下一步验证

- 超过 100% Conversion 的所有比例与取整。
- 技能特殊文本在两阶段之间的优先级。
