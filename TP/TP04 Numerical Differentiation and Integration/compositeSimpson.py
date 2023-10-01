from collections.abc import Callable


def CompositeSimopson(f: Callable[[float],float],a: float, b: float, n: int) -> float:
    h = (b-a)/n
    f0=f(a)+f(b)
    f1 = 0
    f2 = 0
    x=a
    for i in range (1,n,1):
        x=x+h
        if(i % 2 == 0):
            f2 = f2 +f(x)
        else:
            f1 = f1 +f(x)
    A = h*(f0+2 * f2 +4 * f1)/3
    return A

if __name__ == "__main__":
    def f(x): 
        return x**2
    I = CompositeSimopson(f=f,a=0,b=1,n=10)
    print(I)