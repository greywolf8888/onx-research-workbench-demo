# Full-Stack Scope

I use this repository to map to the product and interface side of my full-stack work.
The companion trend-wave engine demo shows the research-core backend.

## What This Repository Shows

| Layer | My implementation focus |
| --- | --- |
| Product design | Dense, utility-first research screen instead of a marketing landing page. |
| Frontend engineering | Static shell, responsive layout, data rendering, and low dependency surface. |
| Backend engineering | Minimal Python HTTP service with explicit read-only routes. |
| API design | Synthetic JSON contracts that mirror the private workbench shape. |
| Data boundary | Fixture repository isolated from route handling and UI rendering. |
| Safety design | No mutation routes and a documented security boundary. |
| Testing | Contract-oriented unit tests and CI. |
| Documentation | Architecture, walkthrough, API contract, case study, release notes, and sanitization policy. |

## What I Deliberately Did Not Publish

- Private production frontend views.
- Account pages requiring real user context.
- Exchange credentials or account snapshots.
- Private cache locations and generated runtime files.
- Any route that could place orders or mutate account state.

## How It Pairs With The Research-Core Demo

The research-core demo answers: "How do I score and review candidates?"

I use this workbench demo to answer: "How do I present those outputs through a safe,
read-only product surface?"

Together they show my full-stack range while keeping private strategy and account
material out of public GitHub.

## 中文摘要

我用这个仓库展示我的产品化和界面工程能力；配套研究内核仓库展示后端评分和风控流程。
两个仓库合在一起覆盖研究逻辑、API、数据契约、前端界面、测试和文档。
