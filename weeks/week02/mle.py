"""Week 2: MLE (Bernoulli, Gaussian).

JJ implements the TODOs based on paper derivations.
"""
import numpy as np


def bernoulli_log_likelihood(p: float, xs: np.ndarray) -> float:
    """Compute log-likelihood log L(p; xs) for Bernoulli i.i.d. samples.

    p: scalar in (0, 1)
    xs: binary 1D ndarray, values in {0, 1}
    returns: scalar float log-likelihood
    """
    # TODO(JJ): write log-likelihood from scratch
    raise NotImplementedError


def bernoulli_mle(xs: np.ndarray) -> float:
    """Analytical MLE for Bernoulli parameter p.

    xs: binary 1D ndarray, values in {0, 1}
    returns: estimated float p_hat
    """
    # TODO(JJ): return the derived MLE formula
    raise NotImplementedError


def gaussian_log_likelihood(mu: float, var: float, xs: np.ndarray) -> float:
    """Compute log-likelihood log L(mu, var; xs) for 1D Gaussian samples.

    mu: mean (float)
    var: variance sigma^2 (float > 0)
    xs: 1D ndarray of observations
    returns: scalar float log-likelihood
    """
    # TODO(JJ): write log-likelihood from scratch
    raise NotImplementedError


def gaussian_mle(xs: np.ndarray) -> tuple[float, float]:
    """Analytical MLE for 1D Gaussian parameters (mu, sigma^2).

    xs: 1D ndarray of observations
    returns: (mu_hat, var_hat)
    """
    # TODO(JJ): return the derived MLE formulas (sample mean, biased sample variance)
    raise NotImplementedError
