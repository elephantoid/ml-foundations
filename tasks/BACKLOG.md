# BACKLOG

## Inventory & Migration
- [x] **M-00** 기존 `PLAN.md`와 M01(Week 1) evidence 실제 확인 및 워크스페이스 통합 (2026-10-19 완료: `PLAN.md`, `PROGRESS.md`, `derivations/week01/To be Researcher-week1.jpg`, `gradcheck.py`, `weeks/week01/grads.py`, `uv run pytest tests weeks/week01 -q` 19 passed 확인)

## M01 — Week 1: Calculus Tools (`PLAN.md` Week 1)
- [x] **M01-01** 백지 유도 4종: $\sin(x^2), \exp(-(x-\mu)^2), \log(1+e^x), \nabla_x\|Ax-b\|^2$ (`derivations/week01/To be Researcher-week1.jpg`)
- [x] **M01-02** NumPy 구현 및 수치 미분 검증: `gradcheck.py`, `weeks/week01/grads.py` (`19 passed`)
- [x] **M01-03** Tutor 3/3 연속 정답 및 Week 1 Gate 통과 (`PROGRESS.md` 2026-10-15)

## M02 — Week 2: MLE — Bernoulli & Gaussian (`PLAN.md` Week 2, 현재 모듈)
- [ ] **M02-01** Bernoulli likelihood $L(p) \to \log L(p) \to \hat{p}_{\text{MLE}} = k/n$ 백지 유도(`derivations/week02/`), 경계 반례($k=0, k=n, \log 0$) 및 Diagnostic #1(파라미터 vs 추정량 vs 사전분포, Beta prior MAP 한 줄 차이) 재검증
- [ ] **M02-02** Gaussian 1D mean/variance MLE($\hat{\mu}_{\text{MLE}}, \hat{\sigma}^2_{\text{MLE}}$) 백지 유도(`derivations/week02/`)와 비편향 표본분산($n-1$) 비교
- [ ] **M02-03** NumPy 구현(`weeks/week02/mle.py`의 `TODO(JJ)` 4개) 및 `uv run pytest weeks/week02 -q` 통과·경계/수치 실험
- [ ] **M02-04** Tutor 변형질문 3연속 정답(`/tutor`), `/gate` 판정 & 48h+ 지연 회상 기록

## Subsequent Modules (`PLAN.md` Weeks 3–6, 이전 모듈 Gate 통과 전 자동 진입 금지)
- [ ] **M03-00** Week 3: Linear regression = Gaussian MLE + gradient descent (`MML 9.1–9.2`, Diagnostic #4 재검증)
- [ ] **M04-00** Week 4: Ridge = MAP with Gaussian prior (`MML 8.3, 9.2`, Diagnostic #2 재검증)
- [ ] **M05-00** Week 5: Logistic regression, sigmoid $\sigma'=\sigma(1-\sigma)$, cross-entropy (`shelf/ml-bible-ch0-classical-ml.md`, Diagnostic #3b 재검증)
- [ ] **M06-00** Week 6: 2-layer MLP backprop from scratch + Cycle 1 전체 4개 Diagnostic `/retest` (`MML 5.6`, `shelf/ml-bible-ch1~2`)

