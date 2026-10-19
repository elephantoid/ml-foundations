# STATUS

Project: ML Foundations — Module & Evidence (`ml-interview-foundations`, ALTER Cycle 1)
Date: 2026-10-19
Mode: **READY FOR M02 (Week 2)** — Workspace migration & document reconciliation completed (`M-00` done).
Current task: `M02-01` / `M02-02` (Week 2 Reading `MML 8.3 p.265–271` & Blank-paper derivation of Bernoulli/Gaussian MLE).
Approved task: `M-00` (completed 2026-10-19). Next learning task awaits JJ's study session (`/today` or `M02-01`).
Blockers: None.

## Evidence-Backed Status Matrix (`implemented / partial / missing / unknown`)

| Component / Module | Status | Evidence (File & Test References) |
|---|---|---|
| **Curriculum & Logs** (`PLAN.md`, `PROGRESS.md`, `diagnostics/`) | **implemented** | [`PLAN.md`](../PLAN.md), [`PROGRESS.md`](../PROGRESS.md), `diagnostics/baseline-2026-10-14.md` (local-only via `.gitignore`) |
| **Shelf & NotebookLM Pack** (`shelf/`, `notebooklm/`) | **implemented** | `shelf/` (local-only via `.gitignore`), [`notebooklm/GUIDE.md`](../notebooklm/GUIDE.md) |
| **Agent Configs & Skills** (`AGENTS.md`, `CLAUDE.md`, `.agents/skills/`) | **implemented** | [`AGENTS.md`](../AGENTS.md), [`CLAUDE.md`](../CLAUDE.md), `.agents/skills/{today,tutor,gate,retest}/SKILL.md` (symlinked to `.agent/skills` & `.claude/skills`) |
| **M01 / Week 1** (Calculus tools & `gradcheck.py`) | **implemented** | Derivation: [`derivations/week01/To be Researcher-week1.jpg`](../derivations/week01/To%20be%20Researcher-week1.jpg)<br>Code: [`gradcheck.py`](../gradcheck.py), [`weeks/week01/grads.py`](../weeks/week01/grads.py)<br>Tests: [`tests/test_gradcheck.py`](../tests/test_gradcheck.py), [`weeks/week01/test_week01.py`](../weeks/week01/test_week01.py) (**19/19 passed**)<br>Gate: `PROGRESS.md` [2026-10-15] Week 1 · gate PASSED |
| **M02 / Week 2** (MLE: Bernoulli & Gaussian) | **partial** | Scaffolding & tests exist: [`weeks/week02/README.md`](../weeks/week02/README.md), [`weeks/week02/mle.py`](../weeks/week02/mle.py) (4 `TODO(JJ)` raise `NotImplementedError`), [`weeks/week02/test_week02.py`](../weeks/week02/test_week02.py) (0/6 passed as expected before implementation). `derivations/week02/` is empty; Tutor 3/3 not started. |
| **M03–M06 / Weeks 3–6** | **missing** | Planned in `PLAN.md`; scaffolding is created only upon passing the preceding week's `/gate`. |
| **Git Repository (`.git`)** | **implemented** | Initialized git repository with `.gitignore` excluding sensitive/copyrighted files (`shelf/`, `diagnostics/`, `.venv/`, etc.) and published to GitHub. |


## Last Tests (Executed 2026-10-19)
- **M01 & Core Gradcheck:**
  - Command: `uv run pytest tests weeks/week01 -q`
  - Result: `19 passed in 0.89s`
- **M02 Scaffolding Check:**
  - Command: `uv run pytest weeks/week02 -q`
  - Result: `6 failed in 0.07s` (`NotImplementedError` on all 4 `TODO(JJ)` stubs in `weeks/week02/mle.py`, as expected).

