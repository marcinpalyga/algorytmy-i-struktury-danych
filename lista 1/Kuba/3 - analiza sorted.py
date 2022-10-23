import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

sizes = [i for i in range(1,51)]
times = [[0]*50]*50

for i in range(50):
    for n, j in enumerate(sizes):
        random_array = [random.randint(-20,20) for m in range(j)]

        start = time.time()
        sorted(random_array)
        stop = time.time()

        times[i][n] = stop-start

print(times)
mean = []
for i in range(50):
    summation = 0
    for j in range(50):
        summation += times[i][j]
    mean.append(summation/50)


plt.scatter(sizes, mean, c='r', s=10)
plt.show()

'''
#hipoteza
def func(x, a, b):  return a*x + b
popt, pcov = curve_fit(func, sizes, times)

a, b = popt
x = np.arange(1, 2000)

plt.plot(x, func(x, a, b), label='model')
plt.scatter(sizes, times, c='r', s=10, label='dane')
plt.xlabel('Rozmiar tablicy')
plt.ylabel('Czas dzialania programu')
plt.legend()
plt.show()'''