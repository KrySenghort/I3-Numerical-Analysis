def PolyEval(a,x,d):
    N = len(a)
    n = N-1
    v = [0]* (d+1)
    v[0] = a[n]
#     dp = 0
#     ddp = 0
#     p = a[n]
    #v = [a[n],0,0]
    for k in range(1, N,1):
        for l in range(d,0,-1):
            v[l] = l*v[l-1]+ x * v[l]
        v[0] = a[n -k] + x * v[0]
    return  v
    #  v[2] = 2*v[1]+x*v[2]
#         dp = p+x*dp:
#         v[1] = v[0] +x *v[1]
# #         ddp = 2 * dp + x*ddp
#         v[0] =a[n-k]+x*v[0]
# #         p = a[n - k] + x * p
#         v[0 ] = a[n-k]+x *v[0]
#     #return (p, dp,ddp)
if __name__=="__main__":
    a = [1,2,3,4]
    x = 2
    v= PolyEval(a=a, x=x,d=4)
    print(a)
    print(x)
    print(v)