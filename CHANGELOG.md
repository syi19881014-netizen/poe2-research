# Knowledge Changelog

## 2026-10-25 — Baseline catch-up and KB-013

- 发现仓库 VERSION.md 仍停留在 0.5.4f，现以 GGG 官方 0.5.5e Patch Notes 校正版本参考至 0.5.5e；不代表全部旧知识卡已完成新版实测。
- 新增 KB-013：Mark_GGG 解释武器基础攻击伤害；Concussive Runes / Repulsion Wave 非武器基础伤害特例仍需 A/B 实验，不能用通用解释覆盖特例。
- 记录 2026-10-23 交易站 stat min/max 过滤器异常报告及 GGG 正在调查；未证实修复。
- 记录 2026-10-19–25 周报；新版本无平衡数值调整的已确认依据。
- 将旧卡 0.5.4f 数值视为历史作用域，后续逐卡执行 0.5.5e Diff。

## 2026-08-19 — 0.5.4f officially verified

- 直接核验 GGG 官方论坛 `0.5.4f Patch Notes` 与同日 Hotfix，当前知识基线由 0.5.4e 更新为 **0.5.4f**。
- 推翻 2026-08-13 的临时结论“0.5.4f 未证实”。
- 技能：Charged Staff 在 Shapeshift 后切回 Quarterstaff 时 energy waves 失效的问题已修复；pre-0.5.4f 样本需重测。
- 操控：修复锁定目标发生在技能启动极短窗口时，技能可能朝错误方向释放；pre-0.5.4f 的瞄准可靠性结论需要版本标记。
- Boss：修复 Shapeshift 状态被部分 Boss grab 后可能无限锁动画；该风险不再属于当前正常构筑评估。
- Trade：0.5.4f Hotfix 只修复非英语 Trade Market UI 翻译，没有 Gold、手续费或交易规则变化。
- 尚待验证：其它 weapon-swap/shapeshift buff 是否共享同类 bug；Archon of Chayula + Talismans 社区报告仍未获官方修复确认。

## 2026-08-15 — Grand Expedition reward-scaling model

- 新增 KB-006：0.5.4 Grand Expedition 的 Remnant、Runic Modifier、Logbook 与 rarity/quantity 放大模型。
- 固化 0.5.3 后 T15+ 达到 Grand Expedition Remnant 上限、炸药从 20 降为 15、箱子奖励结构重做。
- 固化 0.5.4 Expedition Atlas Tree：Gaining Traction、Sown Seeds、Calculated Investment、The Quest Continues、Double or Nothing、Cultivate the Sea 等关键节点。
- 标记 0.5.4 Hotfix 3 为重要数据分界：移除隐藏的每 Remnant +50% Monster Rarity，并将该收益正式放到 Gaining Traction；Hotfix 前后收益样本禁止混用。
- 建立路径依赖 Farm 模型：传播源应按对后续 Runic Monsters 的覆盖价值排序，高 Rune 数量/Boss/密集怪区作为后段收割目标。
- 社区关于 Pack Size 对 rune loot 价值很低的说法保持待验证，不升级为稳定机制。

## 2026-08-13 — Pinnacle Boss architecture + baseline correction

- 新增 KB-005：0.5 终局 Pinnacle Boss 的 Quest / Infinite Farm 双层架构。
- 固化 0.5 以后不再沿用旧 Difficulty 0–4 / Calamity Fragment 终局模型。
- 记录 Arbiter of Ash 的强制转阶段与转阶段回满生命对真实 TTK 的影响。
- 记录 Arbiter of Divinity 的 Quest / repeatable 两版定位，以及重复击杀可用于 Fortress 区域自动完成与 Atlas 点获取。
- 撤回仓库初始化时缺乏可核验官方来源的 `0.5.4f` 基线；后续核验确认当前知识基线可推进至 `0.5.4e Maintenance`，但该临时结论已在 2026-08-19 被官方 0.5.4f 原帖推翻。

## 2026-08-13 — Repository bootstrap

- 建立 POE2 专家知识库目录、证据等级与版本规范。
- 迁移知识卡 01：伤害转换与 Gain as Extra。
- 迁移知识卡 02：Trigger / Totem / Minion / 自施法语义。
- 迁移知识卡 03：Weapon Set Passive、Spirit 与快照边界。
- 迁移知识卡 04：Modifier pool、iLvl、Weight、Family 与做装概率。
- 建立实验模板、待验证队列、来源政策与自动校验脚本。
