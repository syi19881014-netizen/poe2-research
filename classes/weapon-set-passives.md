---
id: KB-003
module: classes
status: COMMUNITY_VERIFIED
confidence: medium
applies_to: "0.5.x"
last_verified: 2026-08-08
tags: [weapon-set, passive-tree, spirit, snapshot]
sources: []
---

# Weapon Set Passive、Spirit 与快照边界

## 直接结论

Weapon Set Passive Skill Points 不是额外白送两套点数，而是允许部分普通被动点在 Weapon Set I/II 上采用不同分配。技能可绑定武器组并在使用时动态切换对应装备、专属被动与 Reservation/Spirit 配置。

## 重要规则

- 同一枚可双专精的被动点在两组可走不同路线，但任一时刻只按当前武器组生效。
- 技能绑定或武器需求可导致自动切换。
- Reservation / Persistent Skills 可随 Weapon Set 动态切换。
- 工具武器价值显著高于传统“备用武器”：可承担 +技能等级、Curse、Exposure、Spirit 等角色。

## 快照模型

当前不使用“全快照/全动态”二分法，而采用**按属性拆分的混合模型**：

- 创建实体时固有参数可能快照，例如技能等级驱动的基础参数。
- 玩家当前全局属性可能动态读取。
- 敌人身上的 Debuff 常可能动态影响已存在效果。

这只是框架，不可从一种技能推广到全部 Minion/Totem/DoT。

## 常见误区

- Weapon Set Points ≠ 额外点。
- 切换武器 ≠ 只换装备；被动与 Reservation 也可能变化。
- 已生成实体 ≠ 必然锁定创建时全部属性。
- 高 Spirit 武器召满后切走 ≠ 保证永久维持所有召唤物。

## 对 BD / 做装影响

- 可以设计“准备树 / 输出树”“清图树 / Boss树”。
- 副手工具武器应纳入市场估值与做装体系。
- Witchhunter/高双专精能力构筑需单独建立极端双树模型。

## 待验证

- Temporary / Reviving / Persistent Minion 的属性读取矩阵。
- Ignite / Poison / Bleed / Ground DoT 的快照边界。
- 武器切换后已存在实体对 +Skill、全局增伤、穿透、异常积累的读取方式。
