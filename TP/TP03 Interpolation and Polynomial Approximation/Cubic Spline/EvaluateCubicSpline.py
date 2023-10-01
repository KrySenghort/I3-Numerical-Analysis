import pandas as pd
from EvaluatePolynomial import EvaluatePolynomial


def EvaluateCubicSpline(df: pd.DataFrame, x: float) -> float:
    n = len(df)
    index = df.index.values
    for k in range(0, n, 1):
        inter = index[k]
        if (x in inter):
            i = k
            break
    p = EvaluatePolynomial(a=df.iloc[i, :].to_list(), x=x - inter.left)
    return p


if __name__ == "__main__":
    from NaturalCubicSpline import NaturalCubicSpline
    df = NaturalCubicSpline(x=[1, 2, 3], a=[2, 3, 5])
    print(df)
    p = EvaluateCubicSpline(df=df, x=2.5)
    print(p)
