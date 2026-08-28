#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SelectorTest(unittest.TestCase):
    def test_debugging_task_selects_debugging_skill(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "select_harness.py"),
             "systematically debug a reproducible runtime failure", "--limit", "5"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        ids = [item["skill_id"] for item in json.loads(result.stdout)["candidates"]]
        self.assertIn("hermes-skill-systematic-debugging", ids)


if __name__ == "__main__":
    unittest.main()
