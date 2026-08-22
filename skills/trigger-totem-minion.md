---
id: KB-002
module: skills
status: COMMUNITY_VERIFIED
confidence: medium-high
applies_to: "0.5.x"
last_verified: 2026-08-22
tags: [trigger, totem, minion, self-use, support-gems]
sources: []
---

# Trigger / Totem / Minion 与“你亲自使用”的语义边界

> 2026-08-22 更新：本卡中 Trigger / Meta / Invocation / self-cast 的技术语义已经由 **KB-009 `skills/meta-trigger-invocation-self-cast.md`** 以官方补丁与当前数据重新验证。后续 Trigger 相关判断优先引用 KB-009；本卡继续保留 Totem / Minion / Clone 的实体归属研究。

## 直接结论
判断辅助宝石是否生效，不能只看标签。必须同时确认：**技能实体、实际使用者、使用方式、辅助文本排除条件**。

玩家自用、Triggered Skill、Totem 使用技能、Minion/Clone 使用技能是不同来源。

## 四层判定
1. **技能类型**：Attack / Spell / Duration / Minion / Trigger 等。
2. **实际使用者**：Player / Totem / Minion / Clone / 其他实体。
3. **使用方式**：主动使用、触发、Persistent、Command。
4. **文本限制**：尤其是“你亲自使用”“不能支持 Trigger”“不能改变 Minion Skills”等。

## 已固化规则
- Triggered Spell 的 self-cast / Invocation 边界以 KB-009 为准。
- Totem 不是 Minion；召唤物增伤不能自动套给图腾。
- 一个技能可能包含玩家主击中、子爆炸、地面效果、生成实体、实体技能等多层，必须逐层判断辅助效果。

## 常见误区
- “能插进去” ≠ “所有部分都有效”。
- “使用我的武器” ≠ “继承我全部全局属性”。
- “Totem 是友方” ≠ “自动吃所有 Minion/Ally 效果”。

## 可复现实验
- Totem + Minion Damage 与同量通用伤害对照。
- 同一复合技能分别测玩家部分与生成实体部分。
- “你击中时” vs “你的技能击中时”只让 Totem 输出，观察差异。

## 待验证
- 图腾命中与击杀归属的逐词缀矩阵。
- Clone/Minion 对武器、箭袋与临时 Buff 的继承范围。
