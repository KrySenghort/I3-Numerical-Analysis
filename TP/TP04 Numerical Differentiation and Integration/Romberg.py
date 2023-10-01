from typing import Callable, Tuple
import numpy as np
import pandas as pd
from math import pi

def Romberg(f: Callable[[float], float], a: float, b: float, rtol: float = 1.e-6, n: int = 10) -> Tuple[float, pd.DataFrame]:
    N = n + 1
    R = np.full(shape=(N, N), fill_value=np.nan, dtype=np.float64)
    ni = 1
    R[0, 0] = CompositeTrapezoid(f=f, a=a, b=b, n=ni)
    for i in range(1, N):
        ni = 2 * ni
        R[i, 0] = CompositeTrapezoid(f=f, a=a, b=b, n=ni)
        I = i + 1
        p = 1
        for j in range(1, I):
            p = 4 * p
            R[i, j] = R[i, j - 1] * (R[i, j - 1] - R[i - 1, j - 1]) / (p - 1)
        if abs(R[i, i] - R[i - 1, i - 1]) < rtol:
            break
    A = R[i, i]
    I = i + 1
    columns = [f'0(h^{2*(k+1)})' for k in range(0, I)]
    R = pd.DataFrame(data=R[0:I, 0:I], columns=columns)
    return A, R

if __name__ == "__main__":
    from math import cos

    pd.options.display.float_format = "{:.8f}".format

    def f(x: float):
        return cos(x)

    a, b = 0, pi / 2
    A, R = Romberg(f=f, a=a, b=b, n=4)
    print(f"A = {A:.8f}")
    print(R)