import time
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def example2(S):
    """Return the sum of the elements with even index in sequence S.
    """
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total
x = []
y = []
for n in range(100000, 2000000, 100000):
    S = [random.randint(-50,50) for i in range(n)]
    start = time.process_time()
    example2(S)
    end = time.process_time()
    t = end-start
    x.append(n)
    y.append(t)
    print("%d   %f"%(n,t))
def func(x,a,b):
    return a*x + b
popt, pcov = curve_fit(func,x,y)
x2=np.arange(100000, 2000000)
plt.scatter(x, y, c='r', label = 'Dane')
plt.plot(x2,func(x2, *popt), 'b-', label = "Model")
plt.xlabel("Rozmiar Tablicy")
plt.ylabel("Czas oczekiwania")
plt.show()