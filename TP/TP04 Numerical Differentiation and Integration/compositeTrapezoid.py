from collections.abc import Callable

def compositeTrapezoid(f: Callable[[float],float], a: float, b: float, n: int)-> float:
    h = (b-a) / n
    f0 = f(a) +f(b)
    fi = 0
    x = a
    
    for _ in range(0,n,2):
        x = x+ h
        fi = fi +f(x)
    A = h * (0.5*f0+fi)
    
    return A