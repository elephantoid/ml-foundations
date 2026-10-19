# Week 1 — Calculus tools (10/14–10/20)

**Shelf:** MML 5.1–5.3 (printed p.141–154). 5.5 (p.158) as reference only. Skip 5.4, 5.7, 5.8.

## Gate
1. **Derivation** (book closed) → photo into `derivations/week01/`
   - f₁(x) = sin(x²)
   - f₂(x) = exp(−(x−μ)²)
   - f₃(x) = log(1 + eˣ)   ← simplify: what familiar function is f₃′?
   - f₄(x) = ‖Ax − b‖²  (x ∈ ℝⁿ, A ∈ ℝ^{m×n})  → ∇ₓf₄
2. **NumPy**: implement `gradcheck.py`, then the analytic gradients in `grads.py`. Run `uv run pytest tests weeks/week01 -q` — all green.
3. **Tutor**: `/tutor` → 3 consecutive correct.
