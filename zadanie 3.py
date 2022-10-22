import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x = []
y = []
for n in range(100000, 1000000, 50000):
    numbers = [random.randint(-25,25) for i in range(n)]
    start = time.process_time()
    sorted(numbers)
    end = time.process_time()
    t = end - start
    x.append(n)
    y.append(t)
    print("%d   %f"%(n,t))

def func(x,a,b):
    return a*x+b

x2 = np.arange(100000, 1000000)
popt, pcov = curve_fit(func,x,y)
plt.scatter(x, y, c="r", label="Dane")
plt.plot(x2, func(x2, *popt), 'b-', label="Model")
plt.xlabel("Rozmiar Tablicy")
plt.ylabel("Czas oczekiwania")
plt.show()