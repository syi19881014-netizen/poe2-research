# Current Research Baseline

- Game: Path of Exile 2
- Research baseline: **0.5.4f**
- League/era: **Runes of Aldur / Return of the Ancients**
- Latest verified version date: **2026-08-12**
- Baseline checked: **2026-08-19**
- Repository schema: **v1**

## Version rule

`research baseline` 只表示知识库当前优先核验的版本，不意味着所有知识卡都已在该版本重新实测。每张卡必须单独查看 `last_verified` 与 `status`。

## Current verified chain

- 0.5.4 — 2026-06-25
- 0.5.4 Hotfix 1–4 — 2026-06-25 至 2026-06-29
- 0.5.4b / c / d — 2026-07
- 0.5.4e Maintenance — 2026-07-31
- **0.5.4f Patch Notes — 2026-08-12**
- **0.5.4f Hotfix — 2026-08-12**

## 0.5.4f verified changes

GGG 官方论坛 `0.5.4f Patch Notes`（Stacey_GGG，2026-08-12）确认：
1. 修复锁定目标发生在技能启动极短窗口时，技能可能朝错误方向释放；
2. 修复变身状态被部分 Boss 抓取技能命中后可能无限锁动画；
3. 修复冲刺后松开输入有时会额外 Dodge Roll；
4. 修复变身后切回 Quarterstaff 时 Charged Staff 的 energy waves 无法继续触发；
5. 修复部分 MTX、PlayStation 客户端及 instance crash。

同日 `0.5.4f Hotfix` 修复非英语语言下 Trade Market UI 未翻译。

## Correction note

2026-08-13 因当时未找到 GGG 原始线程，仓库曾将 `0.5.4f` 标记为未证实并把基线回退到 0.5.4e。2026-08-19 重新通过 Reddit 帖子的官方链接直接打开并核验 GGG 原始论坛线程：
- https://www.pathofexile.com/forum/view-thread/3996513
- https://www.pathofexile.com/forum/view-thread/3996590/page/1

因此此前“0.5.4f 未证实”的结论正式失效，当前基线更新为 **0.5.4f**。
