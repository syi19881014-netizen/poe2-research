# Contribution Rules

## 新增知识前

- 先确认当前版本。
- 优先查 GGG 官方；再查数据站/社区实测。
- 不把攻略作者结论直接升级为 `OFFICIAL`。

## 修改知识卡

- 保留旧结论的版本历史。
- 改 `last_verified`。
- 证据变强/变弱时同步改 `status` 与 `confidence`。
- 如果补丁可能影响但尚未重测，先改为 `NEEDS_RETEST`。

## Commit 建议

- `kb: add <topic>`
- `kb: verify <topic> for <version>`
- `kb: mark <topic> obsolete in <version>`
- `version: ingest <version>`
- `research: add experiment <topic>`
