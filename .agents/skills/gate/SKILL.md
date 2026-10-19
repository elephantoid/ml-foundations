---
name: gate
description: >-
  Use when JJ asks to check whether the week is done or types /gate. Runs the weekly gate (derivation photo + NumPy tests + Tutor log) and advances the week only if all pass.
---
Current week = earliest week with an unpassed gate in PROGRESS.md. Check all three, Editor role (attack, don't flatter):

1. **Derivation** — look in `derivations/weekNN/` for images/PDFs. Read them. Check every step of the week's required derivation (PLAN.md § Milestones). Flag skipped steps, notation errors, hand-waving. Missing file = fail.
2. **NumPy** — run `uv run pytest weeks/weekNN -q`. All tests must pass (they include the rel-error < 1e-6 gradcheck). Also skim JJ's code for anything that only passes by accident.
3. **Tutor** — PROGRESS.md must show a `tutor` entry this week with 3/3 consecutive. If missing, run `/tutor` now.

Result:
- All pass → append `gate` entry to PROGRESS.md with "PASSED", create `weeks/week{N+1}/` scaffolding (README with tasks from PLAN.md + test file + stub with TODO — **never** the solution), and state next week's first action.
- Any fail → list exactly what's missing, append `gate` entry "NOT PASSED", no advancing.
