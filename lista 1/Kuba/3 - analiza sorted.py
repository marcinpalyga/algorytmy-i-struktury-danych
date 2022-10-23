import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

sizes = [i for i in range(1,21)]
times = [[0]*20]*20

for i in range(20):
    for j in sizes:
        random_array = [random.randint(-20,20) for n in range(j)]

        start = time.time()
        sorted(random_array)
        stop = time.time()

        times[i][j] = stop-start

mean = []
for i in range(20):
    summation = 0
    for j in range(20):
        summation += times[i][j]
    
    mean.append(summation/20)

print(len(mean), len(sizes))


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