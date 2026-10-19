# Week 2 — MLE: Bernoulli & Gaussian

**Shelf:** MML 8.3 (printed p.265–271).

## Gate
1. **Derivation** (book closed) → photo into `derivations/week02/`
   - Bernoulli: Likelihood $L(p) \to$ Log-likelihood $\log L(p) \to \frac{d}{dp} \log L(p) = 0 \implies \hat{p}_{\text{MLE}} = \frac{k}{n}$
   - Gaussian (1D): Likelihood $L(\mu, \sigma^2) \to$ Log-likelihood $\log L(\mu, \sigma^2) \to$
     $\frac{\partial}{\partial \mu} \log L = 0 \implies \hat{\mu}_{\text{MLE}} = \frac{1}{n}\sum x_i$,
     $\frac{\partial}{\partial \sigma^2} \log L = 0 \implies \hat{\sigma}^2_{\text{MLE}} = \frac{1}{n}\sum (x_i - \hat{\mu})^2$
   - Diagnostic #1 retried
2. **NumPy**: Implement TODOs in `mle.py`. Run `uv run pytest weeks/week02 -q` — all green.
3. **Tutor**: `/tutor` → 3 consecutive correct.
