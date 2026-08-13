---
id: EXP-001
status: planned
version: "0.5.4f"
created: 2026-08-13
last_run: null
related_cards: [KB-003]
---

# Weapon Set 快照矩阵

## 目标

将“快照/动态读取”从模糊描述拆成逐属性矩阵。

## 测试对象

- Totem
- Temporary Minion
- Reviving/Persistent Minion
- Direct DoT
- Ignite
- Poison
- Ground effect

## 变量

- +Skill Level
- increased/more Damage
- Penetration
- Ailment Buildup
- Duration
- Player Buff
- Enemy Debuff
- Spirit availability

## 输出

每个格子只允许：`snapshot` / `dynamic` / `mixed` / `unknown`，并附视频/日志或重复次数。
