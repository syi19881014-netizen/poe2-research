# Knowledge Changelog

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
- 撤回仓库初始化时缺乏可核验官方来源的 `0.5.4f` 基线；后续核验确认当前知识基线可推进至 `0.5.4e Maintenance`，但 0.5.4 核心机制仍以主补丁及 Hotfix 1–4 为证据基线。

## 2026-08-13 — Repository bootstrap

- 建立 POE2 专家知识库目录、证据等级与版本规范。
- 迁移知识卡 01：伤害转换与 Gain as Extra。
- 迁移知识卡 02：Trigger / Totem / Minion / 自施法语义。
- 迁移知识卡 03：Weapon Set Passive、Spirit 与快照边界。
- 迁移知识卡 04：Modifier pool、iLvl、Weight、Family 与做装概率。
- 建立实验模板、待验证队列、来源政策与自动校验脚本。
