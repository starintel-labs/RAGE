---
name: "rage-loop"
description: "Run a complete Recursive Analysis with Gated Execution loop."
version: "1.0.0"
author: "StarIntel Labs"
category: "workflow"
tags: ["rage", "workflow", "agents", "verification"]
---

# RAGE Loop

## Objective

Drive a task through Recursive Analysis with Gated Execution without skipping evidence, approval, or verification boundaries.

## Procedure

1. **Analyze** observed repository and task state. Separate facts, assumptions, contradictions, and unknowns.
2. **Gate** the next bounded action. State the evidence, authorization, invariants, and tests required to proceed.
3. **Execute** only the admitted action. Do not silently expand scope.
4. **Evaluate** observed outputs, tests, diffs, failures, and side effects.
5. **Recurse** from the new observed state. Preserve useful evidence and revise assumptions that failed.

## Rules

- Never treat a plan as evidence.
- Never treat a generated patch as successful execution.
- Never treat a green test as approval unless the gate explicitly defines it that way.
- Prefer small loops with observable exits over long open-loop agent runs.
- On failure, diagnose before retrying. Do not repeat the same action unchanged unless the failure was demonstrably transient.

## Exit Criteria

- The requested outcome is observable.
- Required gates were satisfied or explicitly reported blocked.
- Verification results are recorded exactly as observed.
- The next state is clear enough for another RAGE loop.