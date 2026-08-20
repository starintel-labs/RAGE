---
name: "rage-execute"
description: "Execute one bounded action admitted by an open RAGE gate."
version: "1.0.0"
author: "StarIntel Labs"
category: "execution"
tags: ["rage", "execution", "bounded-change", "agents"]
---

# RAGE Execute

## Objective

Perform the smallest state transition admitted by the active gate while preserving declared invariants.

## Preconditions

- The active gate is explicitly **OPEN**.
- The intended change and validation path are known.
- Applicable repository instructions have been read.
- Current state has been observed immediately before mutation.

## Procedure

1. Re-check the specific state that the action depends on.
2. Perform only the bounded action admitted by the gate.
3. Preserve unrelated work and avoid opportunistic refactors.
4. Capture failures and partial effects rather than hiding them.
5. Stop when the admitted action is complete. Do not silently chain into another state transition.
6. Hand the observed result to `rage-evaluate`.

## Rules

- Do not widen scope because another improvement is convenient.
- Do not bypass wrappers, validation, permissions, or safety checks to force success.
- Retries must be bounded and justified by observed failure mode.
- Idempotent operations are preferred when the same action may be replayed.

## Exit Criteria

- The admitted action ran or produced an explicit failure state.
- Side effects are known well enough to evaluate.
- No claim of success is made until evaluation completes.