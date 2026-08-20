---
name: "rage-gate"
description: "Define and evaluate an explicit execution gate before changing state."
version: "1.0.0"
author: "StarIntel Labs"
category: "workflow"
tags: ["rage", "gate", "approval", "invariants"]
---

# RAGE Gate

## Objective

Turn analysis into a bounded, auditable decision about whether execution may proceed.

## Gate Contract

Before execution, state:

- the intended state transition;
- required evidence;
- required authority or approval, if any;
- invariants that must remain true;
- validation that will prove the transition succeeded;
- terminal conditions that force reject, repair, or defer.

## Procedure

1. Read the relevant research and canonical design.
2. Resolve contradictions that materially affect the action or leave the gate closed.
3. Check required approval evidence. Never infer approval from merge state, file existence, or green CI.
4. Confirm the action is bounded and reversible where practical.
5. Confirm the validation path exists before execution.
6. Record the gate as **OPEN**, **BLOCKED**, or **REJECTED** with evidence.

## Exit Criteria

- **OPEN** means every required precondition is satisfied and execution may begin.
- **BLOCKED** names missing evidence or authority without pretending the task failed.
- **REJECTED** records why the proposed transition should not execute.
- No ambiguous requirement is silently converted into permission.