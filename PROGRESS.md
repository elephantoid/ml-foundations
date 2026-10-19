# Progress Log — Cycle 1

Append-only, newest at bottom. Claude appends after every session, `/tutor`, `/gate`.

Format:
```
## [YYYY-MM-DD] Week N · <session | tutor | gate | retest>
- Time: <minutes> (week total: <h>/7.5)
- Done: ...
- Gaps found: ...        ← Tutor-diagnosed, specific
- Gate: [ ] derivation  [ ] numpy  [ ] tutor 3/3
- Next: ...
```

---

## [2026-10-14] Week 1 · setup
- Time: 0 (week total: 0/7.5)
- Done: Advisor interview completed in the vault session → Curriculum v1 (`PLAN.md`). Baseline diagnostic recorded (`diagnostics/baseline-2026-10-14.md`). Workspace created.
- Gaps found: see Baseline — derivation procedure, retrieval, parameter/prior confusion, backprop vs optimizer, answer discipline.
- Gate: [ ] derivation  [ ] numpy  [ ] tutor 3/3
- Next: First session — MML 5.1–5.2, derive the three week-1 functions, write `gradcheck.py`.

## [2026-10-14] Week 1 · setup
- Time: 0 (week total: 0/7.5)
- Done: Made workspace tool-agnostic — rules in `AGENTS.md` (CLAUDE.md imports it), commands as `.agents/skills/*` (Antigravity native; Claude Code via `.claude/skills` symlink). Added `notebooklm/` upload pack (MML cut to Cycle-1 sections + ML Bible excerpts + study context + GUIDE). PLAN page refs corrected to printed pages.
- Gate: [ ] derivation  [ ] numpy  [ ] tutor 3/3
- Next: Create NotebookLM notebook per `notebooklm/GUIDE.md`, then first session.

## [2026-10-15] Week 1 · tutor
- Time: 90 (week total: 1.5/7.5)
- Done: MML 5.1–5.2.1 reading. Blank-paper derivation attempt for 4 functions (sin(x²), exp(-(x-μ)²), log(1+eˣ), ‖Ax-b‖²). Implemented `gradcheck.py` and `weeks/week01/grads.py` (19 tests passed). Completed Tutor Q&A (3/3 consecutive correct).
  - Q1: d/dx exp(-2x²+3) → -4x exp(-2x²+3) [정답]
  - Q2: d/dx log(3+e^{2x}) → 2e^{2x}/(3+e^{2x}) [정답]
  - Q3: ∇x ‖Ax-b‖² dimension matching & why A^T [정답]
- Gaps found: Chain rule inner derivative multiplication vs cancellation; exp derivative in exponent confusion; log = ln in ML; matrix calculus row vs column dimension matching; rel_error denominator max vs addition.
- Gate: [ ] derivation  [x] numpy  [x] tutor 3/3
- Next: Clean blank-paper derivation sheet photo into `derivations/week01/`, then `/gate`.

## [2026-10-15] Week 1 · gate
- Time: 15 (week total: 1.75/7.5)
- Done: Weekly gate PASSED (all 3 checks green).
  - Derivation: `derivations/week01/To be Researcher-week1.jpg` verified (all 4 derivations clean, complete, correct notation).
  - NumPy: 19 pytest tests passed (`gradcheck.py` + `grads.py`).
  - Tutor: 3/3 consecutive correct verified.
  Scaffolded `weeks/week02/` (MLE: Bernoulli & Gaussian).
- Gaps found: None remaining for Week 1.
- Gate: [x] derivation  [x] numpy  [x] tutor 3/3
- Next: Week 2 first action — MML 8.3 (p.265) 열고 30분 타이머.

## [2026-10-19] Week 2 · setup
- Time: 0 (week total: 0/7.5)
- Done: Migrated workspace from `ml-interview-foundations` to `03-ml-foundations` (`M-00`). Preserved original `PLAN.md`, reconciled `AGENTS.md`, `CLAUDE.md`, `docs/PROJECT_SPEC.md`, `docs/ACCEPTANCE.md`, `tasks/BACKLOG.md`, `docs/STATUS.md`, `docs/MODULE_LOG.md`, and `docs/DESIGN_DECISIONS.md` (`ADR-001`). Re-synced `.venv` and verified Week 1 (`uv run pytest tests weeks/week01 -q` → 19 passed).
- Gaps found: —
- Gate: [ ] derivation  [ ] numpy  [ ] tutor 3/3
- Next: Week 2 (`M02-01` / `M02-02`) — MML 8.3 (p.265–271) 읽고 Bernoulli & Gaussian MLE 백지 유도.

