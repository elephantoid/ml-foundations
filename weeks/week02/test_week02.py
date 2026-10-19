import numpy as np
import pytest
from gradcheck import numerical_grad
from weeks.week02 import mle


def test_bernoulli_mle_formula():
    xs = np.array([1, 0, 1, 1, 0, 1])
    assert mle.bernoulli_mle(xs) == pytest.approx(4 / 6)


def test_bernoulli_convergence():
    rng = np.random.default_rng(42)
    p_true = 0.65
    xs = rng.binomial(1, p_true, size=20000)
    p_hat = mle.bernoulli_mle(xs)
    assert abs(p_hat - p_true) < 0.015


def test_bernoulli_gradient_is_zero_at_mle():
    xs = np.array([1, 1, 0, 1, 0, 1, 1, 0])
    p_hat = mle.bernoulli_mle(xs)

    # d/dp log L(p) should be 0 at p_hat
    grad = numerical_grad(lambda p: mle.bernoulli_log_likelihood(p[0], xs), np.array([p_hat]))
    assert abs(grad[0]) < 1e-3


def test_gaussian_mle_formula():
    xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    mu_hat, var_hat = mle.gaussian_mle(xs)
    assert mu_hat == pytest.approx(3.0)
    # MLE variance is biased (divided by n=5, not n-1=4): ((4 + 1 + 0 + 1 + 4)/5) = 2.0
    assert var_hat == pytest.approx(2.0)


def test_gaussian_convergence():
    rng = np.random.default_rng(42)
    mu_true, var_true = 3.5, 2.2
    xs = rng.normal(loc=mu_true, scale=np.sqrt(var_true), size=30000)
    mu_hat, var_hat = mle.gaussian_mle(xs)
    assert abs(mu_hat - mu_true) < 0.02
    assert abs(var_hat - var_true) < 0.05


def test_gaussian_gradient_is_zero_at_mle():
    xs = np.array([1.2, 2.4, 1.8, 3.1, 2.0])
    mu_hat, var_hat = mle.gaussian_mle(xs)

    # Gradient of log L(mu, var) with respect to [mu, var] should be 0 at (mu_hat, var_hat)
    def obj(params):
        return mle.gaussian_log_likelihood(params[0], params[1], xs)

    grad = numerical_grad(obj, np.array([mu_hat, var_hat]))
    assert np.all(np.abs(grad) < 1e-3)
