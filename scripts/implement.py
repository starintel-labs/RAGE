#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

from _roamlib import ensure_roam, implementation_slot_problems, project_root, validate_org_headers


def status(roam: Path, root: Path) -> int:
    active = sorted((roam / "implement").rglob("*.org"))
    if not active:
        print("no active implementations")
        return 0
    for path in active:
        print(path.relative_to(root))
    return 0


def resolve_research_inputs(
    values: list[str], *, root: Path, roam: Path, project: str
) -> list[Path]:
    if not values:
        raise SystemExit("implementation requires at least one --research Org file")

    research_root = (roam / "research").resolve()
    resolved: list[Path] = []
    for value in values:
        path = Path(value)
        if not path.is_absolute():
            path = (root / path).resolve()
        else:
            path = path.resolve()

        try:
            rel = path.relative_to(research_root)
        except ValueError as exc:
            raise SystemExit(f"research input must be under {research_root}: {path}") from exc
        if len(rel.parts) < 2:
            raise SystemExit("research input must be inside a project directory")
        if rel.parts[0] != project:
            raise SystemExit(
                f"research project mismatch: design={project} research={rel.parts[0]}"
            )
        if path.suffix.lower() != ".org":
            raise SystemExit(f"research input must be an Org file: {path}")
        if not path.is_file():
            raise SystemExit(f"missing research input: {path}")

        validate_org_headers(path)
        resolved.append(path)

    return resolved


def append_research_manifest(
    destination: Path, research_inputs: list[Path], *, root: Path
) -> None:
    lines = [
        "",
        "* RAGE Research Inputs",
        "",
        "Files-first contract: read these Org research artifacts before the design or repository code.",
        "",
    ]
    for path in research_inputs:
        relative_link = os.path.relpath(path, destination.parent)
        label = path.relative_to(root)
        lines.append(f"- [[file:{relative_link}][{label}]]")
    lines.append("")

    with destination.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("design", nargs="?")
    parser.add_argument(
        "--research",
        action="append",
        default=[],
        help="Required Org research input. Repeat when implementation depends on multiple research files.",
    )
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()

    root = project_root()
    roam = ensure_roam(root)

    if args.status:
        return status(roam, root)
    if not args.design:
        parser.error("design is required unless --status is used")

    source = Path(args.design)
    if not source.is_absolute():
        source = (root / source).resolve()
    design_root = (roam / "design").resolve()
    try:
        rel = source.relative_to(design_root)
    except ValueError as exc:
        raise SystemExit(f"design must be under {design_root}") from exc
    if not source.is_file():
        raise SystemExit(f"missing design: {source}")

    validate_org_headers(source)
    if len(rel.parts) < 2:
        raise SystemExit("design must be inside a project directory")

    project = rel.parts[0]
    research_inputs = resolve_research_inputs(
        args.research, root=root, roam=roam, project=project
    )

    active_dir = roam / "implement" / project
    active_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(active_dir.rglob("*.org"))
    if existing:
        rendered = ", ".join(str(path.relative_to(root)) for path in existing)
        raise SystemExit(f"implementation slot for {project} is occupied: {rendered}")

    destination = roam / "implement" / rel
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    append_research_manifest(destination, research_inputs, root=root)

    problems = implementation_slot_problems(roam)
    if problems:
        destination.unlink(missing_ok=True)
        raise SystemExit("\n".join(problems))

    print(destination.relative_to(root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
