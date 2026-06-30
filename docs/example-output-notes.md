# Example Output Notes

I moved these two images from my private `codex` branch into the public demo as
sanitized example outputs. They show the kind of visual evidence my workbench is
designed to collect, explain, and keep read-only.

These images are not trading advice and they are not live execution signals.
They do not include account data, credentials, balances, fills, order history, or
private runtime paths.

## BTCUSDT Multi-Timeframe Structure

![BTCUSDT multi-timeframe structure](assets/example-outputs/btc-multi-timeframe-structure.png)

I use this output to show how the workbench can summarize the same symbol across
several timeframes instead of forcing me to jump between isolated charts.

What the image demonstrates:

- Weekly, daily, 12H, 4H, and 1H chart panels are placed in one review surface.
- Each timeframe has a compact text judgment covering trend state, support,
  resistance, distance to key levels, and structural notes.
- The right-side cards create an evidence trail: I can see which timeframe is
  supportive, which timeframe is uncertain, and where the short-term trigger
  conflicts with higher-timeframe context.
- The workbench output is read-only. It explains the state; it does not provide a
  button to trade.

Engineering value:

- I can turn chart analysis into a repeatable data product.
- I can keep visual output and textual reasoning aligned.
- I can expose complex research output in a way that is scannable for review.

## WLDUSDT Shortline FIB Channel Plan

![WLDUSDT shortline FIB channel plan](assets/example-outputs/wld-shortline-fib-channel-plan.png)

I use this output to show how the workbench can present a fast-moving candidate
without hiding the risk context.

What the image demonstrates:

- The left panel shows 1H candles with support, resistance, main-force dense
  zones, and a FIB channel overlay.
- The right panel converts the chart into a structured summary: symbol,
  short-term change, turnover, threshold rule, main-force/dense-zone state, FIB
  channel direction, and a read-only plan.
- The plan section distinguishes "no chase", pullback logic, breakout logic,
  targets, soft invalidation, and hard invalidation.
- The output is framed as review material, not as an automatic execution command.

Engineering value:

- I can connect market-screening results to chart-level evidence.
- I can represent a trade idea as structured read-only data.
- I can make invalidation and risk context visible before any action.

## Public Boundary

I keep these images in the demo because they are visual outputs, not private
runtime state. Before publishing them I checked that they do not expose:

- exchange credentials,
- account identifiers,
- balances or positions,
- order IDs or fills,
- private file paths,
- or mutation routes.

## 中文说明

我把这两张图作为公开 demo 的脱敏示例输出，用来展示工作台如何组织图表证据和文字解释。
它们不是投资建议，不是实盘信号，也不包含账户、密钥、余额、订单、成交或私有路径。

第一张 BTCUSDT 图展示多周期结构判读：周线、日线、12H、4H、1H 放在同一页，
右侧卡片把趋势、支撑、压力、距离关键位和周期冲突整理成可复核摘要。

第二张 WLDUSDT 图展示短线候选的 FIB 通道和主力支撑/压力解释：左侧是 1H K 线和通道，
右侧是候选信息、阈值规则、主力密集区、FIB 通道方向、只读计划、失效条件和风险边界。
