# ONX Research Workbench Demo

![Status](https://img.shields.io/badge/status-sanitized_demo-0f766e)
![Mode](https://img.shields.io/badge/mode-read_only-2563EB)
![Frontend](https://img.shields.io/badge/frontend-vanilla_demo-f59e0b)
![License](https://img.shields.io/badge/license-MIT-blue)

[English README](README.md)

本仓库是私有可视化研究终端的公开脱敏低版本演示。它保留只读前端壳、
合成 API 样本和工作流说明，不包含私有运行数据、账户信息、真实交易日志或生产服务。

![工作台预览](docs/assets/workbench-preview.svg)

## 演示内容

- 只读候选表和风险摘要。
- 合成 K 线标注元数据。
- 离线 API 合约示例。
- 面向公开读者的中英文说明和安全边界。

## 本地预览

```powershell
python backend/app/main.py
```

然后访问 `http://127.0.0.1:8765/`。
