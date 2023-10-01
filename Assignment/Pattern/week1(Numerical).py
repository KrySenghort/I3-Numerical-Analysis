# # def solve_linewar_equation(b:float,c:float)->float:
# #   x:float = None
# #   if(b!=0):
# #     print("Has a unique solution")
# #     x=-c/b
# #   else:
# #     if(c==0):
# #       print("Infinitely Many solutions")
# #     else:
# #       print("Has no solutions")
# #   return x
# # x= solve_linewar_equation(b=6,c=3)
# # print(f'x={x}')

# # n=10
# # sa=0
# # for i in range(n+1):
# #     sa+=i
# # print(f"n={n} and sa ={sa}")
# # print("\n Using formula:")
# # print(f"n = {n} and sa={n*(n+1)/2}")
# # def sum3b(n: int):
# #     s:float = 0
# #     for i in range(n+1):
# #         s +=i**2
# #     return s
# # for n in [10,20,30]:
# #     print(sum3b(n))
# # str1 = 'cambodia'
# # print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
# print("Hello")
# a = int(input("Enter the number: "))
# print("Your number is: ",a)
# if a>3:
#     for a in range(1,2):
#         print("Hi my name is LCL")
# else:
#     print("nice to meet you! see you latter")
# for i in  "banana":
#     print(i)
 
# def mybook():
#     print("My favorite book is Mine Book!")

# mybook()

# def myfri(b):
#     print("My friend is: ",b)
# myfri("Muth")
# myfri("Nakhim")
# myfri("Ah Ktery")

import pandas as pd;
def bisection(f, x0,x1, e):
    step = 1
    condition= True
    df = pd.DataFrame(data = {'x': [x0], 'f(x)': [f(x0)]})
    while condition:
        x2 = (x0 + x1)/2
        print(f'Step: {step}, x2 = {x2:0.16f} and f(x2) = {f(x2): 0.16f}')
        if f(x0) * f(x2) <0:
            x1= x2
        else:
            x0 = x2
        df.loc[step] = {'x':x0, 'f(x)': f(x0)}
        step = step +1
        condition = abs(f(x2))>e
    print(f'\nRequired Root is : {x2:0.16f}' )
    return df

if __name__=="__main__":
    import math
    def f(x): return math.cos(x) -x
    df = bisection(f=f, x0=0, x1= math.pi/4, e=1.0e-16)
    print(df.style.format({'x':'{:.16f}','f(x)':'{:.16f}'}).to_latex())
