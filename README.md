# Hermes Agent

> Configure, extend, or contribute to Hermes Agent with explicit local/runtime safety boundaries.

This repository packages one focused Hermes skill as a public, documentation-first capability. The blueprint below explains the actual operating surfaces, control points, failure paths, and evidence expected from a trustworthy run.

![Detailed systems blueprint for Hermes Agent](assets/system-blueprint.png)

## The problem it solves

Tool integrations can create accidental side effects when authentication, scope, preview, execution, and verification are not separated.

## System components

- **Hermes configuration**
- **Agent runtime**
- **Tools and models**
- **Skills and memory**
- **Verified behavior**

## Execution walkthrough

1. **Identify the requested Hermes extension**
2. **Inspect configuration and runtime version**
3. **Add the smallest compatible change**
4. **Connect tools skills or model settings**
5. **Run a disposable behavior check**
6. **Document rollback and environment assumptions**

## Example request

> In a disposable test workspace, configure, extend, or contribute to Hermes Agent with explicit local/runtime safety boundaries. Return the result, the evidence used to verify it, and any limitations or actions that still require approval.

## Evidence contract

- `request.json` — captures request.
- `inspection.json` — captures inspection.
- `preview.json` — captures preview.
- `execution.json` — captures execution.
- `verification.json` — captures verification.
- `receipt.json` — captures receipt.

A run is complete only when the final artifact can be reopened or re-read and compared with the requested acceptance criteria. An attempted command or successful API response alone is not sufficient proof.

## Safety boundaries

- Confirm the exact target, owner, environment, and authority before acting.
- Preview consequential changes and pause at the approval gate.
- Keep credentials, personal data, and private endpoints out of logs and examples.
- Preserve user work and avoid unrelated changes.
- Report verification failures as incomplete work.

Read [SAFETY.md](SAFETY.md), [SECURITY.md](SECURITY.md), and the detailed [How it works](docs/HOW-IT-WORKS.md) guide before connecting this workflow to a real service or production environment.

## Repository contents

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Trigger conditions and concise agent workflow. |
| `assets/system-blueprint.png` | High-resolution technical architecture poster. |
| `docs/HOW-IT-WORKS.md` | Component and execution-stage details. |
| `docs/EXAMPLES.md` | Safe, review-only, and failure scenarios. |
| `docs/PRODUCT.md` | Audience, problem statement, and maturity. |
| `SAFETY.md` / `SECURITY.md` | Operational and disclosure boundaries. |
| `tests/README.md` | Contract and package validation guidance. |

## Maturity

This is a public reference workflow extracted from a larger private workbench. It does not include a hosted runtime, credentials, or private infrastructure. Adopters must connect compatible tools and validate behavior in their own environment.

## Contributing

Contributions should improve capability accuracy, safe defaults, reproducible examples, or verification evidence without broadening the skill beyond its stated purpose. See [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- JIT-HARNESS:START -->
## Executable harness contract

This repository now includes a typed, task-adaptive harness contract for **Hermes Agent**. The contract maps the skill to memory, planning, capability-orchestration, and action modules; defines bounded repair and stop behavior; and records skill-specific verification evidence.

```bash
python3 scripts/validate_harness.py
python3 scripts/run_harness.py examples/task.json
python3 -m unittest discover -s tests -p 'test_*.py'
```

The included runner performs validation and dry-run planning only. Live tool or service execution requires a separately reviewed adapter and measured evidence.

- [Task-adaptive harness guide](docs/JIT-HARNESS.md)
- [Typed harness manifest](harness/manifest.json)
- [JSON Schema](harness/harness.schema.json)
- [Example task](examples/task.json)
<!-- JIT-HARNESS:END -->
