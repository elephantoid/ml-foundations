"""Week 1: analytic derivatives you derived on paper. JJ fills these in."""
import numpy as np

MU = 0.7


def f1(x): return np.sin(x**2)
def f2(x): return np.exp(-(x - MU) ** 2)
def f3(x): return np.log1p(np.exp(x))
def f4(x, A, b): r = A @ x - b; return float(r @ r)


def df1(x):
    # TODO(JJ): your derivation of d/dx sin(x^2)
    return 2 * x * np.cos(x**2)


def df2(x):
    # TODO(JJ)
    return 2 * (MU - x) * np.exp(-(x - MU) ** 2)


def df3(x):
    # TODO(JJ)
    return  1 / (1 + np.exp(-x))


def grad_f4(x, A, b):
    # TODO(JJ): gradient w.r.t. x, shape (n,)
    return 2 * A.T @ (A @ x - b)
