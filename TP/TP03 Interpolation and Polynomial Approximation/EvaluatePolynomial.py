def EvaluatePolynomial(a: list[complex], x: complex) -> complex:
    N = len(a)
    n = N - 1
    p = a[n]
    for i in range(1, N, 1):
        p = a[n - i] + x * p
    return p
