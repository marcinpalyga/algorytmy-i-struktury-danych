import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def polynomialn2(n, x):
    start = time.time()
    result = 0
    coefficients = [random.randint(-10, 10) for i in range(n)]
    start = time.process_time()
    for i in range(n):
        ai = coefficients[i]
        xi = 1
        for j in range(0, i):
            xi *= x
        result += ai*xi
    end = time.time()
    t = end - start
    return result, t

def polynomialnlogn(n, x):
    result = 0
    coefficients = [random.randint(-10, 10) for i in range(n)]
    start = time.process_time()
    for i in range(n):
        ai = coefficients[i]
        result += ai*(x**i)
    end = time.process_time()
    t = end - start
    return result, t

print(polynomialn2(1000, 2))
print(polynomialnlogn(1000, 2))

def horner(n, x):
    coefficients = [random.randint(-10,10) for i in range(n+1)]
    result = 0
    start = time.process_time()
    for i in range(n, 0, -1):
        bracket = coefficients[n-1] + x*coefficients[n]
        result += bracket
    end = time.process_time()
    t = end - start
    return result, t  
print(horner(1000, 2))

#################################
def func(x,a, b):
    return a*x + b
x = []
y = []
for n in range (100000,500000,25000):
    start = time.process_time()
    horner(n, 2)
    end = time.process_time()
    t = end - start
    x.append(n)
    y.append(t)
    print("%d   %f"%(n,t))
x2 = np.arange(100000, 500000)
popt, pcov = curve_fit(func,x,y)

plt.scatter(x, y, c='r', label = 'Dane')
plt.plot(x2, func(x2, *popt), "b-", label="Model")
plt.xlabel("Rozmiar Tablicy")
plt.ylabel("Czas oczekiwania")
plt.legend()
plt.show()

#schemat hornera jest notacji O(n)