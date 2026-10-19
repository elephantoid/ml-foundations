import numpy as np
import pytest

from gradcheck import numerical_grad, rel_error
from weeks.week01 import grads as G

XS = [-1.3, -0.2, 0.0, 0.4, 1.7]


@pytest.mark.parametrize("f,df", [(G.f1, G.df1), (G.f2, G.df2), (G.f3, G.df3)])
@pytest.mark.parametrize("x0", XS)
def test_scalar(f, df, x0):
    num = numerical_grad(lambda v: f(v[0]), np.array([x0]))
    assert rel_error(np.array([df(x0)]), num) < 1e-6


def test_vector_f4():
    rng = np.random.default_rng(0)
    A, b, x = rng.normal(size=(5, 3)), rng.normal(size=5), rng.normal(size=3)
    num = numerical_grad(lambda v: G.f4(v, A, b), x)
    assert rel_error(G.grad_f4(x, A, b), num) < 1e-6
