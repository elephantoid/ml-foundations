# PROJECT SPEC — ML Foundations

## 출처 보존 및 모듈 매핑 (`PLAN.md` = Source of Truth)
원본 [`PLAN.md`](../PLAN.md) (ALTER Curriculum v1, Cycle 1)를 학습 범위·순서·교재 참조의 **Single Source of Truth**로 보존한다. 원본 계획의 모듈 경계·문제를 덮어쓰지 않으며, 본 프로젝트의 모듈 ID(`M01`–`M06`)는 `PLAN.md`의 주차(`Week 1`–`Week 6`)와 1:1 대응한다:

| Module | `PLAN.md` 대응 | 주제 | 핵심 유도 (Whiteboard) | NumPy 구현 | 교재 (`shelf/`, 인쇄본 페이지) | 상태 |
|---|---|---|---|---|---|---|
| **M01** | Week 1 | Calculus tools: partials, gradients, chain rule | $\sin(x^2), \exp(-(x-\mu)^2), \log(1+e^x), \nabla_x\|Ax-b\|^2$ | `gradcheck.py`, `weeks/week01/grads.py` | MML 5.1–5.3 (p.141–154), 5.5 (p.158) | **PASSED** (실물 증빙·19 테스트 검증 완료) |
| **M02** | Week 2 | MLE (Bernoulli, Gaussian) | $\log L \to \partial = 0$ ($\hat{p}$, $\hat{\mu}, \hat{\sigma}^2$) + Diagnostic #1 재검증 | `weeks/week02/mle.py`, `test_week02.py` | MML 8.3 (p.265–271) | **IN PROGRESS** (스캐폴딩 완료, TODO 미구현) |
| **M03** | Week 3 | Linear regression = Gaussian MLE + GD | MSE $\equiv$ Gaussian MLE; $\nabla_w$ | Linear regression GD (Diagnostic #4) | MML 9.1–9.2 (p.291–302) | Planned |
| **M04** | Week 4 | Ridge = MAP with Gaussian prior | Closed form; why $w$ shrinks (Diagnostic #2) | $\|w\|$ vs $\lambda$ sweep | MML 8.3 (MAP), 9.2 (MAP/regularization) | Planned |
| **M05** | Week 5 | Logistic regression, sigmoid, cross-entropy | $\sigma' = \sigma(1-\sigma)$; CE $\equiv$ MLE; $\nabla$ CE (Diagnostic #3b) | Logistic regression GD | `shelf/ml-bible-ch0-classical-ml.md` | Planned |
| **M06** | Week 6 | 2-layer MLP backprop | Layer-wise gradients + All 4 diagnostics (`/retest`) | Backprop from scratch + `gradcheck` | MML 5.6 (p.159–164), `shelf/ml-bible-ch1~2` | Planned |

### M01 실물 증빙 확인 결과 (Inventory Verified 2026-10-19)
- 백지 유도 스캔본: [`derivations/week01/To be Researcher-week1.jpg`](../derivations/week01/To%20be%20Researcher-week1.jpg), [`derivations/week01/To be Researcher-day1.jpg`](../derivations/week01/To%20be%20Researcher-day1.jpg)
- NumPy 구현 및 테스트: [`gradcheck.py`](../gradcheck.py), [`weeks/week01/grads.py`](../weeks/week01/grads.py), [`tests/test_gradcheck.py`](../tests/test_gradcheck.py), [`weeks/week01/test_week01.py`](../weeks/week01/test_week01.py) (`uv run pytest tests weeks/week01 -q` → **19 passed**)
- Tutor 3/3 및 Gate 통과 로그: [`PROGRESS.md`](../PROGRESS.md) (2026-10-15 Week 1 · gate PASSED)


## 학습 루프 (ALTER + Evidence Gate)
1. **사전 진단 / 독서**: 교재(`shelf/` 내 지정 섹션만 사용) 읽기 후 Tutor가 최소 힌트로 사전 진단 (정답이나 전체 유도 과정을 먼저 제공하지 않음).
2. **백지 수식 유도**: 사용자가 책을 덮고 백지에서 처음부터 끝까지 수식 유도 후 `derivations/weekNN/`에 사진/스캔 저장.
3. **NumPy 구현 + 검증**: 사용자가 직접 `weeks/weekNN/*.py`의 `TODO(JJ)`를 구현(AI 대필 금지). `gradcheck.numerical_grad` 상대오차 `< 1e-6` 및 극한/예외/수렴 조건을 pytest로 검증.
4. **Tutor Gate & 지연 회상**: Tutor(`/tutor`)가 질문 변형 3연속 정답 및 답변 규율("모르면 모른다 + 아는 데서 유도 시도") 확인; 48h 이상 지난 학습일에 지연 회상 및 해당 모듈의 Baseline Diagnostic 재검증 수행.
5. **Binary Gate**: 한 Module 완결(`/gate` 통과 및 `PROGRESS.md`·`docs/STATUS.md` 기록) 전에 새 Module을 자동 시작하지 않음.

## M02 (Week 2) 핵심 점검 항목
- Bernoulli likelihood $L(p)$와 log-likelihood $\log L(p)$ 및 $\hat{p}_{\text{MLE}} = k/n$의 유도, 경계값($k=0, k=n, p \in \{0,1\}$).
- Gaussian 1D 평균($\hat{\mu}_{\text{MLE}}$)/분산($\hat{\sigma}^2_{\text{MLE}}$) MLE의 도출, 표본분산(unbiased variance, $n-1$ 분모)과의 차이.
- 관측 독립성(i.i.d. 가정에 의한 곱 $\to$ 로그 합 변환), likelihood 최적화와 모델 가정의 구분, 파라미터($p$)·추정량($\hat{p}$ )·사전분포(prior)의 구분(Diagnostic #1 보완).
- 수치적/해석적 주의점: $\log(0)$, 곱셈 underflow, degenerate sample($\hat{\sigma}^2 \to 0$), 2계 도함수(오목성/극대값) 확인.

## Cut List 및 일정 원칙
- **Cut List (`PLAN.md` §4 엄수)**: Book of Proof, PyTorch/JAX/autograd, ML Bible Ch3–6, SVM/트리/K-Means/PCA, 일반 행렬미분/볼록성 증명, 외부 신규 강의/자료 추가, 예쁜 요약 노트 작성 금지.
- **일정을 강요하지 않음**: 주 7.5h(일 90분 × 5일)는 기존 계획의 상한선(cap)이지 새로운 일일 강제 할당량이 아니다(컨디션 난조 시 최소 15분 Tutor 질문 1개). 날짜 대신 **Module Gate 판정**으로 전진하며, 금융자격 공부는 포함하지 않는다.

