from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "demo_data"


def load_json(name: str) -> dict:
    with (DATA / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def candidates() -> dict:
    return load_json("candidates.json")


def kline(symbol: str) -> dict:
    if symbol.upper() != "BTCUSDT":
        return {"symbol": symbol.upper(), "source": "synthetic-demo", "overlays": [], "candles": []}
    return load_json("kline_btcusdt.json")
