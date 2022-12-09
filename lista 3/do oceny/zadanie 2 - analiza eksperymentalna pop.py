import random
import time

indexes = [i for i in range(0, 100000, 1000)]
A = [i for i in range(1, 100000)]
times = [[0 for i in range(len(indexes))] for j in range(len(indexes))]

for j in range(len(indexes)):
    for i in range(len(indexes)):
        start = time.perf_counter()
        A.pop(indexes[i])
        stop = time.perf_counter()

        A.insert(indexes[i], random.randint(-50,50))
        times[i][j] = stop-start

avg = [sum(times[i])/len(indexes) for i in range(len(indexes))]
    

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

plt.plot(indexes, avg, label='pop')
plt.xlabel('Index of popped element')
plt.ylabel('Time')
plt.legend()
plt.show()

def f(x, a, b):     return x*a + b

popt, pcov = curve_fit(f, indexes, avg)


x = np.linspace(1, 100000)

plt.clf()
plt.plot(x, f(x, *popt), label='Pop - model', color='orange')
plt.scatter(indexes, avg, label='Pop', s=20)

plt.xlabel('Index of popped element')
plt.ylabel('Time')
plt.legend()
plt.show()

#Metoda pop ma złożoność O(1) gdy popujemy ostatni element i srednio O(n) kiedy popujemy n-ty element(nieostatni)