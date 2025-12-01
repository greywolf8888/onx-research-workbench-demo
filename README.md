# ONX Research Workbench Demo

![Status](https://img.shields.io/badge/status-sanitized_demo-0f766e)
![Mode](https://img.shields.io/badge/mode-read_only-2563EB)
![Frontend](https://img.shields.io/badge/frontend-vanilla_demo-f59e0b)
![License](https://img.shields.io/badge/license-MIT-blue)

[中文说明](README.zh-CN.md)

ONX Research Workbench Demo is a sanitized, low-version public demo of a
private visual research terminal. It keeps a read-only frontend shell,
synthetic API fixtures, and documentation that explain the workflow without
exposing private runtime data.

![Workbench preview](docs/assets/workbench-preview.svg)

## What This Demo Shows

- Read-only candidate table and risk summary.
- Synthetic K-line overlay metadata.
- Offline API contract examples.
- Internationalized introduction and safety documentation.

## Repository Map

| Path | Purpose |
| --- | --- |
| `frontend/` | Static read-only demo shell |
| `backend/` | Minimal Python JSON service for local review |
| `demo_data/` | Synthetic candidates and K-line fixtures |
| `docs/` | Overview, API contract, safety boundary, and demo policy |

## Local Preview

```powershell
python backend/app/main.py
```

Then open `http://127.0.0.1:8765/`.

This repository is not connected to live trading, account management, or private
production services.
