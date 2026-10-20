# klook-api · 合作方订单对账导出

合作方渠道订单的导出与对账片段，用于日结对账重跑和客服查单比对。
包含一份订单导出数据和对应的 API 客户端草稿。

## 目录

| 路径 | 说明 |
|---|---|
| `partner-order-export.csv` | 订单导出，5 行，按 `booking_channel` 与 `amount_hkd` 汇总 |
| `src/klook_api_client.py` | 合作方网关客户端，负责拉取并归一化订单记录 |

## 服务标识

`klook-api`

该标识出现在 CSV 的 `service` 列、导出文件名相关的调阅说明，以及
`klook_api_client.py` 的 `SERVICE_NAME` 常量、`KlookApiPartnerClient` 类名和端点路径中。

## 使用

```bash
python src/klook_api_client.py
```

输出当前客户端指向的网关地址与超时配置。`list_orders()` 目前只有签名，
写入侧统一走履约服务，本地不直连。

## 字段说明

| 字段 | 说明 |
|---|---|
| `partner_order_no` | 合作方单号，`KL-` 前缀 + 日期 + 序号 |
| `contact_name` | 下单联系人 |
| `contact_mobile` | 中间四位以 `****` 代替 |
| `contact_address` | 收货地址 |
| `account_no` | 结算账户，仅保留末四位 |
| `amount_hkd` | 订单金额，港币 |

## 已知问题

- 同一 `partner_order_no` 在改单后会产出一条新记录，对账前需按单号取最新 `amount_hkd`。
- `booking_channel=partner` 的订单地址字段可能为空，报表侧需做空值兜底。

## 维护

合作方集成组
