"""Numerical gradient checker — used every week of Cycle 1.

JJ writes this himself (Week 1 task). Do not let Claude fill in the TODOs.
"""
import numpy as np


def numerical_grad(f, x, h=1e-5):
    """Central-difference gradient of a scalar function.

    f: callable, R^n -> R (takes a float ndarray of shape (n,), returns a float)
    x: ndarray, shape (n,)
    returns: ndarray, shape (n,)

    Hints to think about (not code):
    - central difference (f(x+h e_i) - f(x-h e_i)) / 2h has O(h^2) error; forward has O(h)
    - why is h ~ 1e-5, not 1e-12?
    - don't mutate the caller's x
    """
    # TODO(JJ): 5-8 lines
    n = len(x)
    grad = np.zeros(n)

    for i in range(n):
        x_plus_h = x.copy()
        x_minus_h = x.copy()

        x_plus_h[i] += h
        x_minus_h[i] -= h

        grad[i] = (f(x_plus_h) - f(x_minus_h)) / (2 * h)
    return grad


def rel_error(a, b):
    """Max relative error between two arrays: |a-b| / max(|a|, |b|, 1e-12)."""
    # TODO(JJ): 1-3 lines
    return np.max(np.abs(a - b)) / max(np.max(np.abs(a)), np.max(np.abs(b)), 1e-12)
