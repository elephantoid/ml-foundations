# ACCEPTANCE (Module Gate Criteria)

모든 모듈(`M01`–`M06` / `Week 1`–`Week 6`)은 아래 증거 Gate가 **모두(Binary)** 통과되어야 완료 처리된다 (`PLAN.md` §5 & 공동 운영 프로토콜 통합):

1. **백지 수식 유도 (`derivations/weekNN/`)**:
   - 교재를 덮고 사용자가 처음부터 끝까지 백지에 수식을 유도(AI 해답 복사·대필 금지).
   - 사진/스캔본을 `derivations/weekNN/`에 저장하고, Editor 역할 검증에서 논리 비약·기호 오류가 없어야 함.
2. **NumPy 구현과 테스트 실제 실행 로그 (`weeks/weekNN/`)**:
   - 사용자가 직접 `TODO(JJ)`를 구현(`gradcheck.py`, `weeks/weekNN/*.py`).
   - 해석적 기울기/추정량이 `gradcheck.numerical_grad` 대비 상대오차 `< 1e-6` (`|a-b| / max(|a|,|b|,1e-12)`) 및 수렴/경계 조건을 만족하며, `uv run pytest weeks/weekNN -q` 실제 실행 로그가 녹색(PASS)이어야 함.
3. **Tutor 질문 3연속 정답과 반례 설명 (`/tutor`)**:
   - Tutor 세션에서 변형 질문 **3연속 정답** 달성 및 실패 반례(경계값, 수치 불안정 등) 1개 이상 설명.
   - 답변 규율 준수: 모르면 "모른다"고 답한 뒤 아는 정의에서 유도 시도(질문 바꿔치기 시 오답 처리). NotebookLM 세션은 전체 Q&A 원문을 붙여넣어 검증을 통과한 경우에만 인정.
4. **지연 회상 기록 및 로그 동기화 (`PROGRESS.md` & `docs/STATUS.md`)**:
   - 해당 모듈에 배정된 Baseline Diagnostic 재시도 및 48h+ 지연 회상 기록.
   - `PROGRESS.md`(append-only)와 `docs/STATUS.md`, `tasks/BACKLOG.md`에 실제 검증 증거 링크 기록. 미통과 항목은 미통과(`blocked` / `[ ]`)로 표시하며 **Module auto-skip 금지**.

