---
name: "rage-evaluate"
description: "Evaluate observed execution results against the active RAGE gate."
version: "1.0.0"
author: "StarIntel Labs"
category: "verification"
tags: ["rage", "evaluation", "verification", "tests"]
---

# RAGE Evaluate

## Objective

Determine what actually changed, whether the gate's success criteria were satisfied, and what evidence should survive into the next loop.

## Procedure

1. Inspect the resulting state, diff, outputs, logs, and relevant external effects.
2. Run the narrowest meaningful checks first, then the configured broader checks.
3. Compare results against the gate's declared invariants and success criteria.
4. Classify the result as **ACCEPTED**, **REPAIR**, **REJECTED**, or **BLOCKED**.
5. Record exact observed failures and preserve useful evidence.
6. Update implementation or rejection records when the repository workflow requires it.
7. Hand the resulting state to `rage-recurse`.

## Rules

- Never claim a check passed unless it was run and observed.
- A passing subset of checks does not imply the full gate passed.
- Distinguish implementation defects from infrastructure/transient failures.
- Do not erase contradictory evidence because the intended outcome looked plausible.

## Exit Criteria

- The result classification is justified by observed evidence.
- Failed invariants are named precisely.
- Successful transitions have reproducible validation evidence.
- The next loop does not need to rediscover what happened.