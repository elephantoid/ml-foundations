# DESIGN DECISIONS LOG

> Never silently rewrite accepted ADRs or retrofit a rationale. Log proposed and accepted changes separately.

## TEMPLATE (copy per decision)
- Date / decision ID:
- Problem and source evidence:
- Existing constraint / prior ADR:
- Option A / Option B:
- Expected advantage / cost / failure condition:
- Fastest distinguishing experiment:
- User decision: **PENDING | APPROVED | REJECTED**
- Code/test links:

---

## ADR-001 — Migrate `ml-interview-foundations` and Reconcile Configs/Plans
- **Date / decision ID:** 2026-10-19 / ADR-001
- **Problem and source evidence:**
  - 기존 학습 작업물(`PLAN.md`, `PROGRESS.md`, `gradcheck.py`, `weeks/week01~02`, `derivations/week01~02`, `diagnostics/`, `shelf/`, `notebooklm/`, `.agents/skills/*`, `pyproject.toml`, `uv.lock`)이 `ml-interview-foundations`에 있고, 신규 거버넌스 패키지(`docs/PROJECT_SPEC.md`, `docs/ACCEPTANCE.md`, `tasks/BACKLOG.md`, `docs/STATUS.md`, `AGENTS.md`, `CLAUDE.md`, `.agent/prompts/`, `.claude/prompts/`)는 `03-ml-foundations`에 분리되어 있음.
  - 두 경로에 동명 파일(`AGENTS.md`, `CLAUDE.md`, `.claude/`)이 존재하며, 기존은 `Week 1..6` 명명(`PLAN.md`)을 쓰고 신규 문서는 `M01..M06` 모듈 명명(`docs/PROJECT_SPEC.md`, `tasks/BACKLOG.md`)을 사용함.
- **Existing constraint / prior ADR:**
  - `docs/PROJECT_SPEC.md`: 기존 `PLAN.md`를 source of truth로 보존하고 원본 모듈 경계·문제를 덮어쓰지 말 것.
  - `AGENTS.md` Rule 7: 파괴적 덮어쓰기(`rm -rf`, 파일 유실) 금지.
- **Option A / Option B:**
  - **Option A (Unified Root + Non-destructive Merge — 채택):** `ml-interview-foundations`의 모든 학습 자산(`PLAN.md`, `PROGRESS.md`, `weeks/`, `derivations/`, `diagnostics/`, `shelf/`, `notebooklm/`, `tests/`, `gradcheck.py`, `pyproject.toml`, `uv.lock`, `.agents/skills/`)을 프로젝트 루트로 이동. 충돌하는 `AGENTS.md`/`CLAUDE.md`는 원본을 로컬 백업 보존한 뒤, 신규 공동 운영 프로토콜과 기존 ALTER 6-역할·Hard rules·슬래시 스킬(`.agents/skills` + `.claude/skills` 심볼릭 링크)을 통합. `Week N ↔ Module M0N` 매핑을 `docs/PROJECT_SPEC.md`, `tasks/BACKLOG.md`, `docs/STATUS.md`에 명시하여 `PLAN.md` 원본을 무결하게 유지.
  - **Option B (Subdirectory Isolation):** 기존 폴더 전체를 `legacy/` 하위 폴더로 이동하고 루트 문서에서만 링크 참조. (`pytest` 경로, `PLAN.md` 상대 경로, `.agents/skills` 탐색 경로가 깨지는 단점 존재)
- **Expected advantage / cost / failure condition:**
  - 장점: `pyproject.toml` 및 `uv run pytest` 경로(`weeks/week01`, `tests/test_gradcheck.py`), `.agents/skills` 및 `.claude/skills` 경로가 루트에서 그대로 작동하며, 원본 `PLAN.md`와 `PROGRESS.md`가 100% 보존됨.
  - 실패 조건: `.venv` 이동 시 절대경로(shebang) 불일치로 pytest 실행 실패 가능 → 이동 후 `uv sync` 또는 가상환경 재생성으로 해결. 동명 설정 파일 단순 덮어쓰기 시 기존 규칙 손실 가능 → 백업 파일 생성 후 병합으로 방지.
- **Fastest distinguishing experiment:**
  - 파일 이동 후 `ls -la`로 누락/충돌 확인 및 `uv run pytest tests weeks/week01 -q`로 기존 M01(Week 1) 19개 테스트 통과 확인.
- **User decision:** **APPROVED** (사용자 요청: `ml-interview-foundations` 이동 및 설정/plan 비교 업데이트, Git 초기화 및 민감 정보 `.gitignore` 후 Public 배포)
- **Code/test links:** [PLAN.md](../PLAN.md), [PROGRESS.md](../PROGRESS.md), [gradcheck.py](../gradcheck.py), [weeks/week01/grads.py](../weeks/week01/grads.py), [weeks/week02/mle.py](../weeks/week02/mle.py)


