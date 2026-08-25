# How Hermes Agent Works

The visuals on this page are static SVGs, so they render directly on GitHub on phones and desktop browsers. Each one is generated from a model specific to this skill.

## System architecture

![Detailed system map for Hermes Agent](../assets/system-map.svg)

### Components

- **1. Hermes configuration:** participates in identify the requested hermes extension.
- **2. Agent runtime:** participates in inspect configuration and runtime version.
- **3. Tools and models:** participates in add the smallest compatible change.
- **4. Skills and memory:** participates in connect tools skills or model settings.
- **5. Verified behavior:** participates in run a disposable behavior check.

## Actor and data sequence

![Actor and data sequence for Hermes Agent](../assets/operation-sequence.svg)

### 1. Identify the requested Hermes extension

**Primary surface:** `Hermes configuration`

Record the concrete input, the operation performed, and the evidence produced at this stage. Continue only when the output is sufficient for the next stage; otherwise preserve the blocker and stop.
### 2. Inspect configuration and runtime version

**Primary surface:** `Agent runtime`

Record the concrete input, the operation performed, and the evidence produced at this stage. Continue only when the output is sufficient for the next stage; otherwise preserve the blocker and stop.
### 3. Add the smallest compatible change

**Primary surface:** `Tools and models`

Record the concrete input, the operation performed, and the evidence produced at this stage. Continue only when the output is sufficient for the next stage; otherwise preserve the blocker and stop.
### 4. Connect tools skills or model settings

**Primary surface:** `Skills and memory`

Record the concrete input, the operation performed, and the evidence produced at this stage. Continue only when the output is sufficient for the next stage; otherwise preserve the blocker and stop.
### 5. Run a disposable behavior check

**Primary surface:** `Verified behavior`

Record the concrete input, the operation performed, and the evidence produced at this stage. Continue only when the output is sufficient for the next stage; otherwise preserve the blocker and stop.
### 6. Document rollback and environment assumptions

**Primary surface:** `Hermes configuration`

Record the concrete input, the operation performed, and the evidence produced at this stage. Continue only when the output is sufficient for the next stage; otherwise preserve the blocker and stop.

## Example output shape

![Illustrative output for Hermes Agent](../assets/example-output.svg)

The example is a visual contract: a real run may look different, but it should expose comparable state, provenance, and verification information. It is not presented as evidence of a live external action.

## Decision and stop conditions

![Decision guide for Hermes Agent](../assets/decision-guide.svg)

The workflow stops when the target is ambiguous, the relevant surface is unavailable or unauthorized, or the final artifact cannot be checked. A logged-in session or successful tool call is not by itself proof that the requested outcome is complete.

## Verification checklist

- Confirm every component shown in the system map exists in the target environment.
- Trace the actor sequence using actual tool output or artifact state.
- Compare the result with the example-output information contract.
- Re-read or reopen the final artifact instead of trusting an attempt message.
- Report omitted stages, unsupported capabilities, and remaining human decisions.
