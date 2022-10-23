import time
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex
    sums in A."""
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count
x = []
y = []
for n in range (100,400,25):
    A = [random.randint(-50, 50) for i in range(n)]
    B = [random.randint(-50,50) for i in range(n)]
    start = time.process_time()
    example4(A, B)
    end = time.process_time()
    t = end - start
    x.append(n)
    y.append(t)
    print("%d   %f"%(n,t))
def func(x,a,b):
    return a*x**3 + b
popt, pcov = curve_fit(func,x,y)
x2=np.arange(100, 400)
plt.scatter(x, y, c='r', label = 'Dane')
plt.plot(x2, func(x2, *popt), 'b-', label = "Model")
plt.xlabel("Rozmiar Tablicy")
plt.ylabel("Czas oczekiwania")
plt.legend()
plt.show()