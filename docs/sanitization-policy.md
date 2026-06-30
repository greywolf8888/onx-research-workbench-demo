# Sanitization Policy

I publish this repository as a product and full-stack engineering demo. It is not
a copy of my private workbench.

## Kept

- Read-only product shell.
- Minimal Python JSON service.
- Synthetic candidate and K-line fixtures.
- Two sanitized chart-output images from the private `codex` branch.
- API contract documentation.
- Tests, CI, release notes, and public workflow history.

## Removed Or Replaced

- Private frontend screens that depend on account context.
- Exchange credentials and local environment files.
- Account snapshots, balances, fills, order logs, and position history.
- Private cache paths and generated reports.
- Runtime files that expose account context or local machine paths.
- Any route that could place orders, cancel orders, edit leverage, or mutate state.
- Internal assets that are not intended for public review.

## UI Principle

I keep the public UI close enough to demonstrate the workbench concept, but I
remove every dependency on private data and every action that would imply live
trading control.

## Commit History Principle

I curated and deduplicated the public history. I use it to tell the development story
of the demo repository without exposing private runtime commits.

## 中文摘要

这个仓库是产品和全栈工程演示，不是私有工作台的完整复制。我保留只读界面、最小 API、
合成样本、测试和文档；移除账户、密钥、真实日志、私有缓存、生产页面和任何写入动作。
