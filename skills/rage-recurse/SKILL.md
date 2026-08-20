---
name: "rage-recurse"
description: "Turn evaluated results into the next grounded RAGE loop."
version: "1.0.0"
author: "StarIntel Labs"
category: "workflow"
tags: ["rage", "recursion", "replanning", "recovery"]
---

# RAGE Recurse

## Objective

Start the next loop from observed evidence rather than blindly repeating the previous plan.

## Procedure

1. Preserve the accepted facts and evidence from the evaluation phase.
2. Remove or revise assumptions contradicted by execution.
3. Identify whether the current objective is complete, blocked, rejected, or still active.
4. If work remains, define the smallest next question or state transition.
5. Re-enter analysis with only the context needed for that next decision.
6. If the same failure repeats, stop naive retries and diagnose the loop itself.

## Loop Detection

Treat repeated action + repeated failure + no new evidence as a loop defect. Change the analysis, gather new evidence, reduce scope, or close the gate. Do not consume resources performing ceremonial retries.

## Exit Criteria

- Completed objectives terminate cleanly.
- Remaining work begins from updated evidence.
- Failed assumptions do not silently survive into the next plan.
- Repeated failures trigger diagnosis rather than unbounded retry.