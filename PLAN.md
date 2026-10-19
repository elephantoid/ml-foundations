# Cycle 1 Plan — ML Interview Foundations (ALTER Curriculum v1)

- **Cycle:** 1 of ~3 · **Dates:** 2026-10-14 → 2026-11-24 (6 weeks)
- **Designed:** 2026-10-14 via Advisor interview (5 decisions below)

## 1. Destination
At the end of Cycle 1, JJ can **derive on a whiteboard** and **implement in NumPy** the core math behind ML-interview questions asked of both **Big-tech Research Engineers** and **Big-tech/unicorn Data / Applied Scientists**.

Cycle 1 covers only the **intersection** of the two roles, along one chain:
**objective function → derivative → implementation.**

Long-term route (direction only — each cycle is re-planned by the Advisor at its end):

| Cycle | Content | Serves |
|---|---|---|
| **1 (now)** | Calculus tools → MLE → linear regression → Ridge/MAP → logistic regression → backprop | Both (prerequisite for everything) |
| 2 | Probability basics, statistical inference (hypothesis tests, p-values, CIs, A/B sizing), ML general (bias-variance, L1/L2, trees/ensembles, metrics) | DS/AS |
| 3 | Linear algebra (eigen, SVD, PCA), DL depth (optimizers, BN/LN, dropout, attention) | RE |

Estimate: Cycle 1 alone covers ~25–30% of fundamentals questions directly (independent estimate, not a measured figure) but is the prerequisite for the rest. ~18 weeks total → mid-Feb 2027. Algorithm coding and system design are separate tracks.

## 2. Baseline (measured 2026-10-14)
**Time budget:** 5 days × 1.5 h = **7.5 h/week cap** (~45 h per cycle). Over the cap → publishing track wins. **Floor:** on a bad day, 1 Tutor question (15 min) — never zero.

Diagnostic results (full answers in `diagnostics/baseline-2026-10-14.md`):

| # | Area | Result |
|---|---|---|
| 1 | Bernoulli MLE + Beta-prior MAP | Got k/n by intuition. **No likelihood → log → derivative procedure.** Called parameter p a "prior probability" (parameter vs estimate vs prior confusion). |
| 2 | Ridge: effect on w, why it reduces overfitting | Could not recall. |
| 3 | Backprop in one sentence / σ′(x) | Chain-rule-backwards ✅. **Conflated gradient computation (backprop) with update (optimizer).** Sigmoid range wrong (said −1..1; it's (0,1)). **Answered "what sigmoid looks like" when asked for its derivative.** |
| 4 | NumPy linear regression with GD | Did not know. |

**Diagnosis:** names and rough pictures exist; **derivation procedure and retrieval do not.** One shared bottleneck — *"write the objective, differentiate it"* — solves all four. Plus an **answer-discipline** issue (swapping the question).

## 3. Sequence
> Page numbers = **printed book pages** (PDF page = printed + 6).

| Week | Dates | Topic | Whiteboard derivation | NumPy | Shelf |
|---|---|---|---|---|---|
| 1 | 10/14–10/20 | Calculus tools: partials, gradients, chain rule | 3 composite functions + 1 vector function | `gradcheck.py` + verify analytic grads | MML 5.1–5.3 (p.141–154); 5.5 (p.158) as reference |
| 2 | 10/21–10/27 | MLE (Bernoulli, Gaussian) | log-likelihood → derivative → 0 | Simulate data, show MLE → true value | MML 8.3 (p.265–271) |
| 3 | 10/28–11/03 | Linear regression = Gaussian MLE + gradient descent | MSE ≡ Gaussian MLE; ∇w | Linear regression GD (= diagnostic #4) | MML 9.1–9.2 (p.291–302) |
| 4 | 11/04–11/10 | Ridge = MAP with Gaussian prior | Closed form; why w shrinks | ‖w‖ vs λ sweep | MML 8.3 (MAP part), 9.2 (MAP/regularization) |
| 5 | 11/11–11/17 | Logistic regression, sigmoid, cross-entropy | σ′ = σ(1−σ); CE ≡ MLE; ∇ of CE | Logistic regression GD | `shelf/ml-bible-ch0-classical-ml.md` (logistic regression section) |
| 6 | 11/18–11/24 | 2-layer MLP backprop | Layer-wise gradients | Backprop from scratch + gradcheck | MML 5.6 (p.159–164), `shelf/ml-bible-ch2-math-of-nn.md`, ch1 backprop part |

- **Finished early?** Move to the next week. **Never add content.**
- **Behind?** The week extends. The cycle end date moves; scope does not grow.

## 4. Cut list (ignore during Cycle 1)
| Item | Decision |
|---|---|
| **Book of Proof** | **Removed from the learning track entirely** (whiteboard interviews test derivation, not proof writing). Revisit only for a paper-implementation/research track. |
| ML Bible Ch3 (hardware), Ch4 (Transformers), Ch5 (vision), Ch6 (agentic) | Cut. Ch4 re-judged in Cycle 3. |
| ML Bible Ch0 | Keep regression only (weeks 3–5). Cut SVM, trees, K-Means, PCA. |
| ML Bible Ch1–2 | Keep backprop / loss / gradient descent only (weeks 5–6). Optimizer comparison & regularization techniques → Cycle 3. |
| PyTorch / JAX / any autograd | Cut — NumPy only (autograd removes the differentiation practice). |
| General matrix calculus, convexity proofs | Cut — derive only what each week needs. MML 5.4, 5.7, 5.8 skipped. |
| New sources / videos / courses / ingesting study material | Cut. |
| Writing polished study notes (wiki pages etc.) | Cut — accepted artifacts are **handwritten derivations + code** only. |
| Roommate role | After Cycle 1, once. |

## 5. Milestones — Weekly gate
A week passes only when **all three** pass:

1. **Blank-paper derivation** — book closed, derive the week's core result start to finish. Save photo/scan to `derivations/weekNN/`.
2. **NumPy verification** — implemented gradient matches `gradcheck.numerical_grad` with **relative error < 1e-6**: `|a−b| / max(|a|,|b|,1e-12)`. Tests in `weeks/weekNN/` must pass.
3. **Tutor: 3 consecutive correct answers** (`/tutor`). Answer discipline counts: unknown → say "모른다", then try to derive from what you know.

| Week | Derivation artifact | Diagnostic retried |
|---|---|---|
| 1 | Derivatives of sin(x²), exp(−(x−μ)²), log(1+eˣ); gradient of ‖Ax−b‖² | — |
| 2 | Bernoulli MLE; Gaussian MLE (μ, σ²) | #1 |
| 3 | MSE ≡ Gaussian MLE; ∇w of MSE | #4 (code) |
| 4 | Ridge closed form + MAP interpretation | #2 |
| 5 | σ′ = σ(1−σ); CE gradient | #3b |
| 6 | Full 2-layer MLP backprop | **All 4 diagnostics, verbatim** (`/retest`) |

**Cycle end (11/24):** compare retest vs Baseline table → Advisor re-run → design Cycle 2.

## Daily session template (90 min)
| Min | Block |
|---|---|
| 0–30 | Read the week's shelf section (Librarian) |
| 30–60 | Blank-paper derivation attempt |
| 60–80 | NumPy work + tests |
| 80–90 | `/tutor` (3 questions) |
