# Demo Walkthrough

This walkthrough explains how I expect a reviewer to inspect the workbench demo.

## 1. Read The Product Intent

The README explains the relationship to my private `codex` branch. I use this
repository to show how I productized research outputs into a read-only interface.

## 2. Inspect The Frontend Shell

Start with:

```text
frontend/index.html
frontend/styles.css
frontend/app.js
```

I kept the frontend dependency-free in this public slice so the layout, data
loading, and product boundary are easy to inspect.

## 3. Inspect The API Contract

The service exposes only:

```text
/health
/api/candidates
/api/kline/BTCUSDT
```

There are no order routes, account mutation routes, or credential-dependent
routes.

## 4. Preview Locally

```powershell
python backend/app/main.py
```

Then open `http://127.0.0.1:8765/`.

## 5. Validate The Contract

```powershell
python -m unittest discover -s tests
```

The tests confirm that candidate and K-line responses are synthetic and match the
expected read-only shape.

## 中文摘要

我建议按 README、前端壳、API 合约、本地预览、测试的顺序阅读。我设定这个 demo 的目标不是展示完整私有系统，
而是展示我如何把研究数据做成可阅读、可验证、只读优先的全栈产品切片。
