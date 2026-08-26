# How Hermes Agent Works

Configure, extend, or contribute to Hermes Agent with explicit local/runtime safety boundaries.

![Detailed systems blueprint for Hermes Agent](../assets/system-blueprint.png)

## Stages

### 1. Identify the requested Hermes extension

**Primary surface:** `Hermes configuration`

Record the input, operation, observable output, and any decision that changes scope. Stop here if the output is missing, contradictory, or insufficient for the next stage.
### 2. Inspect configuration and runtime version

**Primary surface:** `Agent runtime`

Record the input, operation, observable output, and any decision that changes scope. Stop here if the output is missing, contradictory, or insufficient for the next stage.
### 3. Add the smallest compatible change

**Primary surface:** `Tools and models`

Record the input, operation, observable output, and any decision that changes scope. Stop here if the output is missing, contradictory, or insufficient for the next stage.
### 4. Connect tools skills or model settings

**Primary surface:** `Skills and memory`

Record the input, operation, observable output, and any decision that changes scope. Stop here if the output is missing, contradictory, or insufficient for the next stage.
### 5. Run a disposable behavior check

**Primary surface:** `Verified behavior`

Record the input, operation, observable output, and any decision that changes scope. Stop here if the output is missing, contradictory, or insufficient for the next stage.
### 6. Document rollback and environment assumptions

**Primary surface:** `Verified behavior`

Record the input, operation, observable output, and any decision that changes scope. Stop here if the output is missing, contradictory, or insufficient for the next stage.

## Failure handling

- **Authorization failure:** do not probe credentials or broaden access; report the missing authority.
- **Target ambiguity:** stop before mutation and request the minimum identifying information.
- **Tool or service failure:** retain error evidence, retry only safe transient failures, and cap retries.
- **Verification failure:** classify the run as incomplete even when the preceding operation returned success.

## Completion evidence

The handoff should contain the original request, inspection state, preview or plan, exact execution result, direct verification, and a final receipt naming limitations and withheld actions.
