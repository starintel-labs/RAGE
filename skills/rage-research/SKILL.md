---
name: "rage-research"
description: "Create or extend evidence-grounded RAGE research."
version: "1.0.0"
author: "StarIntel Labs"
category: "research"
tags: ["rage", "research", "evidence", "provenance"]
---

# RAGE Research

## Objective

Produce research that can safely drive a later execution gate.

## Preconditions

- Read applicable `AGENTS.md` files.
- Inspect the relevant index and existing canonical research before creating a new note.
- Load only the active research neighborhood, not the entire corpus.

## Procedure

1. Define the exact question or decision the research must support.
2. Gather current authoritative evidence appropriate to the task.
3. Separate **Verified Facts**, **Inference**, **Contradictions**, and **Unresolved Questions**.
4. Record source provenance and retrieval dates for changing external facts.
5. Update or create the canonical research note with `scripts/save-research.py` where applicable.
6. Identify affected design files and the next bounded action.
7. Run repository validation after material document changes.

## Exit Criteria

- Claims are traceable to evidence.
- Inference is not presented as fact.
- Contradictions and unknowns remain visible.
- Duplicate canonical research was not created.
- The research supports a concrete gate or explains why no gate can yet be opened.