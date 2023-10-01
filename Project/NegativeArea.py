import numpy as np

a = -(np.pi)/2
b = (np.pi)/2
m = 0
M = 2
N = np.array([500, 1000, 5000, 10000])

result = []

def f(x):
    return np.cos(x)

for k in range(len(N)):
    Counter = 0
    for i in range(N[k]):
        counter = 0
        x = np.zeros(N[k])
        y = np.zeros(N[k])
        for i in range(len(x)):
            x[i] = np.random.uniform(a,b)
            y[i] = np.random.uniform(m,M)
            
        for i in y:
            j = 0
            if (i <= f(x[j])) & (i >= m):
                counter += 1
            j += 1
        Counter += counter/N[k]
        
    area = (M-m)*(b-a)*Counter/N[k]

    print(f'The Value of this Integral with {N[k]} random is : {area}')