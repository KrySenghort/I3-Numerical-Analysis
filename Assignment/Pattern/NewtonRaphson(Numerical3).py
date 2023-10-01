import pandas as pd
def NewtonRaphson(f: callable, fp: callable, x0: float, e: float = 1.0e-16, N: int = 100):
    step = 1 
    flag = 1 
    condition = True
    df = pd.DataFrame(data = {'x': [x0],'f(x)': [f(x0)]})
    while condition:
        if fp(x0) == 0.0:
            print('Divide by zero error!')
            break
        x1 = x0 - f(x0) / fp(x0)
        print(f'step: {step}, x1 = {x1:0.16f} and f(x1) = {f(x1):0.16f}')
        x0 = x1
        df.loc[step] = {'x': x0, 'f(x)':f(x0)}
        step = step + 1
        if step > N:
            flag = 0 
            break
        condition = abs(f(x1)) > e
    if flag == 1 :
        print(f'\nRequired root is: {x1:0.16f}')
    else:
        print('\nNot Convergent.')
    return df
if __name__=="__main__":
    from math import sin, cos, pi
    def f(x): return cos(x) - x
    def fp(x): return - sin(x) -1 
    x0 = pi / 4
    e = 1.0e-16
    df = NewtonRaphson(f=f, fp= fp, x0 = x0 , e=e)
    df.style.format({'x': '{:.16f}', 'f(x)': '{:.16f}'}).to_latex('NewtonRaphson.tex')