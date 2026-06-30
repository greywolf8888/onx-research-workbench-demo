# Security Boundary

I designed this workbench demo to stay read-only and to use synthetic data.

- I do not provide order placement, cancellation, leverage edit, or account mutation.
- I do not require exchange credentials.
- I do not include private cache paths or real account exports.
- I load API responses from `demo_data/` synthetic fixtures.
- I keep the public UI focused on research review, not execution control.

## Reporting Issues

If you review this repository and notice anything that looks like private data,
credential material, or an unintended mutation route, please open an issue with
the file path and line number.

## 中文说明

我让这个工作台演示只读运行，不包含下单、撤单、杠杆修改或账户变更入口。
API 响应来自 `demo_data/` 合成样本。
