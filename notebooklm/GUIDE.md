# NotebookLM Setup — ALTER Cycle 1

NotebookLM plays **Librarian** (grounded reading, audio) and a **mobile Tutor**. It cannot run code, read your gradcheck results, or keep `PROGRESS.md` — the gate stays in the agent workspace (Antigravity / Claude Code).

## 1. Create the notebook (once, ~5 min)
1. notebooklm.google.com → **New notebook** → name: `ALTER C1 — ML Interview Foundations`.
2. Upload **everything in `notebooklm/sources/`** (7 files):
   - `00-study-context.md` — who/what/out-of-scope (not math)
   - `01-mml-ch5-vector-calculus.pdf` — MML 5.1–5.3, 5.5, 5.6 (printed p.141–154, 158–164)
   - `02-mml-8.3-parameter-estimation.pdf` — MML 8.3 (p.265–271)
   - `03-mml-ch9-linear-regression.pdf` — MML 9.1–9.2 (p.291–302)
   - `04-ml-bible-ch0-regression.md`, `05-ml-bible-ch1-loss-gd-backprop.md`, `06-ml-bible-ch2-math-of-nn.md`
   - If `.md` upload is rejected, rename to `.txt`.
3. **Do not add anything else.** The cut list is enforced here by what is *not* uploaded. A full MML PDF would let answers drift into out-of-scope chapters.

## 2. Configure chat → custom instructions (paste once)
```
You are JJ's tutor for ALTER Cycle 1. Respond in Korean.
Default mode = TUTOR: ask ONE question at a time. Do not lecture. Find the exact gap in my answer and probe it with a narrower follow-up.
If my answer does not address the question asked, say so explicitly before anything else.
Only when I say "막힘" after trying, give the smallest possible hint, then re-ask.
Prefer "derive", "why", "what changes if" over definitions. Ask me to write equations step by step.
Ground every hint in the uploaded sources and cite them. Never go outside the scope in 00-study-context.md.
Count consecutive correct answers. After 3 in a row, say "통과 (3/3)" and print the 3 Q&As as a short block I can paste into my log.
When I type "teach me <topic>", switch to a short explanation (max 8 lines) then immediately "test me" with one question.
```

## 3. Weekly Audio Overview (Studio → Audio Overview → Customize)
Generate one per week, **select only that week's sources** before generating. Use as commute review, not as a substitute for the derivation.

| Week | Sources to select | Customize prompt |
|---|---|---|
| 1 | 00, 01 | Focus only on partial derivatives, gradients and the chain rule (MML 5.1–5.3). Work through 3 concrete examples step by step. Skip matrix gradients and Taylor series. |
| 2 | 00, 02 | Explain maximum likelihood by deriving the Bernoulli and Gaussian MLE step by step: likelihood, log, derivative, set to zero. Stress the difference between parameter, estimate, and prior. |
| 3 | 00, 03, 04 | Show why minimizing squared error equals Gaussian maximum likelihood, then derive the gradient of the squared error for gradient descent. |
| 4 | 00, 02, 03 | Explain MAP with a Gaussian prior and show that it yields Ridge regression. Derive the closed form and explain why the weights shrink. |
| 5 | 00, 04, 05 | Derive the sigmoid derivative σ(1−σ) and show cross-entropy is the negative log-likelihood of logistic regression; derive its gradient. |
| 6 | 00, 01, 05, 06 | Walk through backpropagation for a 2-layer network: forward pass, the error term delta, and the four backprop equations. Separate computing gradients from updating weights. |

During playback use **Interactive mode (Join)** to interrupt with questions.

## 4. How a NotebookLM session counts toward the gate
- Tutor 3/3 in NotebookLM **counts only if** you paste the printed Q&A block into the agent session (`/tutor` → "NotebookLM 결과 붙여넣기"). The agent verifies and logs it to `PROGRESS.md`.
- Audio Overviews and Flashcards/Quizzes **never** count toward the gate — they are review.

## 5. Week rollover
No action needed — all six weeks' sources are in the notebook from day 1. Just change which sources are selected for each Audio Overview.
