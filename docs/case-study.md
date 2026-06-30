# Case Study

## Context

I built the private workbench behind this demo because research outputs were too
fragmented when they lived only in scripts, files, screenshots, and terminal
logs. I wanted a read-only surface where I could review candidates, risk notes,
and chart context without turning the interface into an execution console.

## Problem I Solved

The product question was not "how do I make a trading button?" It was:

- How do I make candidate review faster?
- How do I keep evidence visible next to each symbol?
- How do I prevent a research UI from becoming an unsafe mutation surface?
- How do I make the same data contracts useful to frontend and backend code?

## My Technical Approach

I split the public demo into three simple layers:

1. A static frontend shell for the research view.
2. A minimal Python JSON service for read-only contracts.
3. Synthetic fixtures that replace private data sources.

My private workbench extends this with richer charts and more adapters. The
public repository keeps the shape of the product and the API without exposing
private assets.

## Tradeoffs

I chose a dependency-light public demo because I wanted reviewers to inspect the
full stack quickly. My private branch can use richer tooling; I use this demo to
focus on interface structure, contract clarity, and safety boundaries.

I also kept the UI work-focused. For this kind of tool, dense but organized
information is more valuable than a decorative landing page.

## Outcome

I use the demo to show a full-stack research workbench that is:

- readable as a product artifact,
- safe by default,
- backed by explicit API contracts,
- testable without credentials,
- and clear about what was sanitized.

## 中文摘要

我解决的问题是把分散在脚本、文件、截图和日志里的研究输出整理成只读工作台。
公开版本保留前端结构、API 合约和安全边界，用合成数据替代私有数据源。
