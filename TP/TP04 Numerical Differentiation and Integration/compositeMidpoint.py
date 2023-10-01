from collections.abc import Callable

def compositeTrapezoid(f: Callable[[float],float], a: float, b: float, n: int)-> float:
    h = (b-a) / (n+2)
    h2 = 2 *h
    f2 = 0
    x = a
    N = n +1
    
    for _ in range(0,N,2):
        x = x+h2
        f2 = f2 +f(x)
    A = h2 * f2
    
    return A