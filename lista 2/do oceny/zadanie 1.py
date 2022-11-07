import random
import tracemalloc

def findbiggest(s):
    if len(s) == 1:
        return s[0]
    while len(s) > 1:
        if s[0] >= s[1]:
            s.pop(1)
            return findbiggest(s)
        else:
            s.pop(0)
            return findbiggest(s)

tracemalloc.start()

s = [random.randint(-50, 50) for i in range(15)]
print(f"{s}, Largest element is {findbiggest(s)}")

current, peak = tracemalloc.get_traced_memory()

print(f"Memory allocated is {peak/1024:.2f}kB")



import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

times = []
sizes = [i for i in range(1, 100, 2)]

for i in sizes:
    s = [random.randint(-50, 50) for i in range(i)]

    start = time.time()
    findbiggest(s)
    stop = time.time()

    times.append(stop-start)

def func(x,a,b):
    return a*x + b

popt, pcov = curve_fit(func, sizes, times)
a, b = popt[0], popt[1]
xs = np.arange(1, 100)

plt.scatter(sizes, times, c='r', label='Dane')
plt.plot(xs, func(xs, a, b), label='Model')
plt.xlabel('Rozmiary tablicy')
plt.ylabel('Czas oczekiwania')
plt.legend()
plt.show()

print('Nasza funkcja ma zlozonosc O(n)')