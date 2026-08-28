#!/usr/bin/env python3
"""Rank public Hermes harnesses for a task using a transparent lexical baseline."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "harness" / "catalog.json"
STOP = {"a", "an", "and", "for", "in", "of", "on", "or", "the", "to", "with"}
ALIASES = {
    "debugger": "debug", "debugging": "debug", "systematically": "systematic",
    "failures": "failure", "reproduced": "reproduce", "reproducible": "reproduce",
    "reproduction": "reproduce", "tests": "test", "testing": "test",
}


def terms(value: str) -> set[str]:
    tokens = {token for token in re.findall(r"[a-z0-9]+", value.lower()) if token not in STOP}
    return {ALIASES.get(token, token) for token in tokens}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    query = terms(args.task)
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    ranked = []
    for item in catalog["skills"]:
        title_terms = terms(item["display_name"])
        detail_terms = terms(" ".join([
            item["description"], item["category"], *item["components"], *item["stages"],
        ]))
        title_overlap = query & title_terms
        detail_overlap = query & detail_terms
        overlap = sorted(title_overlap | detail_overlap)
        score = 3 * len(title_overlap) + len(detail_overlap)
        if score:
            ranked.append({"skill_id": item["id"], "score": score, "matched_terms": overlap})
    ranked.sort(key=lambda row: (-row["score"], row["skill_id"]))
    print(json.dumps({"task": args.task, "candidates": ranked[: max(args.limit, 1)]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
