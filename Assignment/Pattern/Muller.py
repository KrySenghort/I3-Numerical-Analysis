import pandas as pd
# from EvaluatePolynomial import EvaluatePolynomial
from  PolyEval import PolyEval
def Muller(a, p0,p1, p2, ftol =1.0e-10, maxiter = 100):
    fp0 = PolyEval(a=a, x=p0, d=0)[0]
    fp1 = PolyEval(a=a, x=p1, d=0)[0]
    fp2 = PolyEval(a=a, x=p2, d=0)[0]
    h1 = p1 - p0
    h2 = p2 - p1
    d1 = (fp1-fp0)/h1
    d2 = (fp2 - fp1)/h2
    d = (d2 - d1)/(h2 + h1)
    df = pd.DataFrame(data= {'p':[p0, p1, p2], 'f(p)': [fp0, fp1, fp2]})
    i = 3
    condition = True
    while condition:
        b = d2 + h2 * d
        fp2 =PolyEval(a=a, x=p2,d = 0)[0]
        D = (b**2 - 4*fp2*d)**(1/2)
        if abs(b - D)<abs(b+D):
            E=b+D
        else:
            E = b-D
        h= -2 * fp2/E
        p = p2 +h
        fp =PolyEval(a=a , x=p, d=0)[0]
        df.loc[i, :] = {'p': p,'f(p)': fp}
        # print(f'i= {i:.0f},p ={p:.10f}, f(p)={f(p):.10f}')
        condition = abs(h)>ftol
        if condition:
            p0 = p1
            p1= p2
            p2 = p
            h1=p1-p0
            h2 = p2 - p1
            fp0=PolyEval(a=a, x=p0, d=0)[0]
            fp1=PolyEval(a=a, x=p1, d=0)[0]
            fp2=PolyEval(a=a, x=p2, d=0)[0]
            h1 = p1 - p0
            h2 = p2 - p1
            d1 = (fp1-fp0)/h1
            d2 = (fp2 - fp1)/h2
            d = (d2 - d1)/(h2 + h1)
            i = i+1
        if i>= maxiter:
            print(f'Method failed after{maxiter} iterations')
        else:
            print(f'\nRoot={p:.2f}')
        return(p, df)
if __name__=="__main__":
    a =[1,1,1,-3,1]
    p, df = Muller(a=a, p0=-0.5, p1=0, p2 = 0.5)
    print(f'p={p:.10f}')
    print(df)