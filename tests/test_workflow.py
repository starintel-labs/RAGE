from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from _roamlib import implementation_slot_problems, slugify  # noqa: E402
from implement import append_research_manifest, resolve_research_inputs  # noqa: E402


VALID_ORG = """:PROPERTIES:
:ID: test-id
:END:
#+title: Research
#+description: Research input
#+status: REVIEW
#+filetags: :rage:research:
"""


class RoamLibTests(unittest.TestCase):
    def test_slugify(self) -> None:
        self.assertEqual(slugify("Hello, RAGE World"), "hello-rage-world")

    def test_rejects_empty_slug(self) -> None:
        with self.assertRaises(SystemExit):
            slugify("---")

    def test_implementation_slot_allows_one_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            roam = Path(tmp) / "roam"
            project = roam / "implement" / "demo"
            project.mkdir(parents=True)
            (project / "one.org").write_text("one", encoding="utf-8")
            self.assertEqual(implementation_slot_problems(roam), [])

    def test_implementation_slot_rejects_two_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            roam = Path(tmp) / "roam"
            project = roam / "implement" / "demo"
            project.mkdir(parents=True)
            (project / "one.org").write_text("one", encoding="utf-8")
            (project / "two.org").write_text("two", encoding="utf-8")
            problems = implementation_slot_problems(roam)
            self.assertEqual(len(problems), 1)
            self.assertIn("contains 2 Org files", problems[0])

    def test_implementation_requires_research_org_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            roam = root / "roam"
            (roam / "research" / "demo").mkdir(parents=True)
            research = roam / "research" / "demo" / "finding.org"
            research.write_text(VALID_ORG, encoding="utf-8")

            resolved = resolve_research_inputs(
                [str(research.relative_to(root))],
                root=root,
                roam=roam,
                project="demo",
            )
            self.assertEqual(resolved, [research.resolve()])

            with self.assertRaises(SystemExit):
                resolve_research_inputs([], root=root, roam=roam, project="demo")
            with self.assertRaises(SystemExit):
                resolve_research_inputs(
                    [str(research.relative_to(root))],
                    root=root,
                    roam=roam,
                    project="other",
                )

    def test_active_implementation_records_files_first_research_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "roam" / "research" / "demo" / "finding.org"
            destination = root / "roam" / "implement" / "demo" / "design.org"
            research.parent.mkdir(parents=True)
            destination.parent.mkdir(parents=True)
            research.write_text(VALID_ORG, encoding="utf-8")
            destination.write_text(VALID_ORG, encoding="utf-8")

            append_research_manifest(destination, [research], root=root)
            text = destination.read_text(encoding="utf-8")
            self.assertIn("* RAGE Research Inputs", text)
            self.assertIn("Files-first contract", text)
            self.assertIn("roam/research/demo/finding.org", text)


if __name__ == "__main__":
    unittest.main()
