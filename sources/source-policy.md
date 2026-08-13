# Source Policy / 来源政策

## 优先级

1. Grinding Gear Games 官方公告、补丁、FAQ、开发者说明
2. 当前客户端/可验证游戏数据
3. PoE2 Wiki
4. PoE2DB
5. 官方交易站与游戏内市场数据
6. 可复现社区实验、顶级玩家实测
7. 攻略、视频、论坛、Reddit/Discord 讨论作为线索

## 重要限制

- PoE2DB 的 Modifier Weight 并非全部来自可直接读取的客户端权重；权重结论必须记录来源与可信度。
- 社区帖子只能证明“有人报告”，不能自动证明“机制如此”。
- 官方补丁说明可能存在后续文本修订；版本卡应记录修订日期。
- 价格与经济数据超过短周期后必须视为过期，不写成永久知识。

## 引用规范

知识卡的 `sources` 至少记录：

- `type`: official | data | wiki | community | trade
- `title`
- `url`
- `checked`
- `note`

如 URL 尚待重新核对，必须标记 `needs_url_verification: true`，不得伪造链接。
