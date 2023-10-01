import pandas as pd
def NaturalCubicSpline(x: list[float], a: list[float]) -> pd.DataFrame:
    N = len(x)
    n = N - 1
    h = [0] * N
    al = [0] * N
    l = [0] * N
    mu = [0] * N
    z = [0] * N
    c = [0] * N
    b = [0] * N
    d = [0] * N
    for i in range(0, n, 1):
        h[i] = x[i+1] - x[i]
    for i in range(1, n, 1):
        al[i] = 3 * (a[i+1] - a[i]) / h[i] - 3 * (a[i] - a[i-1]) / h[i - 1]
        l[0] = 1
        mu[0] = 0
        z[0] = 0
    for i in range(1, n, 1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (al[i] - h[i-1] * z[i-1]) / l[i]
    l[n] = 1
    z[n] = 0
    c[n] = 0
    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1]+2*c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3*h[j])
    data = [a[:-1], b[:-1], c[:-1], d[:-1]]
    index = list('abcd')
    columns = [pd.Interval(left = x[i], right = x[i+1], closed = 'both') for i in range(len(x)-1)]
    df = pd.DataFrame(data=data, index=index, columns=columns).transpose()
    return df
if __name__ == "__main__":
    h = NaturalCubicSpline(x=[1,2,3,4],a=[5,6,7,8])
    print(h)