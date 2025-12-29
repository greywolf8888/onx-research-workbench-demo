# API Contract

| Route | Purpose | Data |
| --- | --- | --- |
| `/health` | Demo service health | Static status |
| `/api/candidates` | Candidate table fixture | `demo_data/candidates.json` |
| `/api/kline/BTCUSDT` | K-line overlay fixture | `demo_data/kline_btcusdt.json` |

## 中文摘要

API 仅返回合成样本，不读取私有缓存，不访问账户，不提供交易动作。
