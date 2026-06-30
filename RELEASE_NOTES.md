# Release Notes

## v0.1.2-demo

I published this patch release to add the two chart-output examples from my
private `codex` branch into the public workbench demo with safer, clearer
explanations.

### Highlights

- Added the BTCUSDT multi-timeframe structure output image.
- Added the WLDUSDT shortline FIB-channel plan output image.
- Added `docs/example-output-notes.md` with visual interpretation, engineering
  value, and public-boundary notes.
- Added an example-output gallery to the English and Chinese README files.

### Public Boundary

I use these images as sanitized visual examples only. They do not include account
data, credentials, balances, fills, order history, private runtime paths, or live
execution controls.

### 中文摘要

`v0.1.2-demo` 增加了两张来自私有 `codex` 分支的脱敏示例输出图，并补充说明：
BTCUSDT 多周期结构判读、WLDUSDT 短线 FIB 通道计划、工程价值和公开边界。

## v0.1.1-demo

I published this patch release to turn the workbench demo from a simple public
export into a stronger full-stack portfolio artifact for the private `codex`
branch.

### Highlights

- Rewrote the README in my first-person project voice.
- Added architecture, walkthrough, full-stack scope, case study, and sanitization docs.
- Added a GitHub presentation checklist covering README, topics, release, security, CI, and social preview.
- Added 1280x640 PNG/SVG social preview assets for repository presentation.
- Tightened read-only security documentation and API boundary language.
- Normalized generated contract notes toward first-person wording.

### 中文摘要

`v0.1.1-demo` 是展示层增强版本。我把 README、架构、案例复盘、脱敏策略、
GitHub 展示清单、社交预览素材和只读安全边界补到更适合作品集展示的状态。

## v0.1.0-demo

I published this release as the public, sanitized demo for the private visual
research workbench behind my `codex` branch.

### Highlights

- Added a dependency-light read-only frontend shell.
- Added a minimal Python JSON service for local review.
- Added synthetic candidate and K-line API fixtures.
- Added explicit API contract documentation.
- Added security and sanitization documentation for public review.
- Added English and Chinese README files written from my first-person project view.
- Added tests and CI for the public data contract.

### Public Boundary

I did not include credentials, private cache paths, account
snapshots, real order history, production frontend views, or any route that can
mutate account state.

### 中文摘要

`v0.1.0-demo` 是我为私有可视化研究台准备的公开脱敏版本。它包含只读前端壳、
最小 Python JSON 服务、合成 API 样本、合约文档、脱敏说明、测试和 CI；
不包含密钥、账户、私有缓存、真实订单、生产页面或任何写入路径。
