import numpy as np
import pytest

from gradcheck import numerical_grad, rel_error


def test_quadratic():
    x = np.array([1.0, -2.0, 3.0])
    g = numerical_grad(lambda v: np.sum(v**2), x)
    assert rel_error(g, 2 * x) < 1e-6


def test_does_not_mutate_input():
    x = np.array([0.5, 1.5])
    x0 = x.copy()
    numerical_grad(lambda v: np.sum(np.sin(v)), x)
    assert np.array_equal(x, x0)


def test_rel_error_basic():
    assert rel_error(np.array([1.0]), np.array([1.0])) == 0
    assert rel_error(np.array([1.0]), np.array([1.1])) == pytest.approx(0.1 / 1.1)
