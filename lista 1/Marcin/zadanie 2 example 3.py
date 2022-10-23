import time
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total
x = []
y = []
for n in range(1000, 5000, 100):
    S = [random.randint(-50,50) for i in range(n)]
    start = time.process_time()
    example3(S)
    end = time.process_time()
    t = end-start
    x.append(n)
    y.append(t)
    print("%d   %f"%(n,t))
def func(x,a,b):
    return a*x**2 + b
popt, pcov = curve_fit(func,x,y)
x2=np.arange(1000, 5000)
plt.scatter(x, y, c='r', label = 'Dane')
plt.plot(x2, func(x2, *popt), "b-", label = "Model")
plt.xlabel("Rozmiar Tablicy")
plt.ylabel("Czas oczekiwania")
plt.legend()
plt.show()