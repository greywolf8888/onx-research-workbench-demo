from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend" / "app"))

from demo_repository import candidates, kline


class WorkbenchDemoTest(unittest.TestCase):
    def test_candidates_are_synthetic(self) -> None:
        payload = candidates()
        self.assertEqual(payload["source"], "synthetic-demo")
        self.assertGreaterEqual(len(payload["candidates"]), 3)

    def test_kline_contract_is_readonly_fixture(self) -> None:
        payload = kline("BTCUSDT")
        self.assertEqual(payload["source"], "synthetic-demo")
        self.assertIn("overlays", payload)


if __name__ == "__main__":
    unittest.main()
