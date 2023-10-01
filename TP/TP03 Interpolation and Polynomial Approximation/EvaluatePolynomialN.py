def EvaluatePolynomialN(a: list[complex], x: complex, d: int = 0) -> list:
    """
    TODO
    ----------
    Evaluate a polynomial and its first, second and `d`-th derivatives at a given value of `x`.

    Parameters
    ----------
    1) `a` : `list[complex]`
        list of coefficients `[a_0,...,a_n]` of the polynomial `p(x)=a_0+a_1 x+...+a_n x^n`
    2) `x` : `complex`
        complex value at which the polynomial to be evaluated

    Return
    ----------
    1) `p` : `complex`
        list of complex value of the polynomial and its consecutive derivatives evaluated at `x`

    Example
    ----------
    >>> import NumericalAnalysis as na
    >>> p = na.EvaluatePolynomialN(a=[1, 2, 3, 4, 5], x=1, d=8)
    >>> for pi in p:
    >>>     print(pi)
    """
    n = len(a) - 1
    p = [0] * (d + 1)
    p[0] = a[n]
    stop = n + 1
    for k in range(1, stop, 1):
        for i in range(d, 0, -1):
            p[i] = i * p[i - 1] + p[i] * x
        p[0] = a[n - k] + p[0] * x
    return p
