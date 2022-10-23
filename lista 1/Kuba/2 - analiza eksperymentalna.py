def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
       total += S[j]
    return total


def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):
       total += S[j]
    return total


def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
       for k in range(1+j):
           total += S[k]
    return total


def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex sums in A."""
    n = len(A)
    1
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count


#analysis

import random
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

example1_time, example2_time, example3_time, example4_time = [], [], [], []
sizes = [10, 20, 30, 40, 50, 100, 200, 500, 1000]


for i in tqdm(sizes):
    example_list = [random.randint(-20, 20) for j in range(i)]
    example_additional_list = [random.randint(-20, 20) for j in range(i)]

    start = time.time()
    example1(example_list)
    stop = time.time()
    example1_time.append(stop-start)

    start = time.time()
    example2(example_list)
    stop = time.time()
    example2_time.append(stop-start)

    start = time.time()
    example3(example_list)
    stop = time.time()
    example3_time.append(stop-start)

    start = time.time()
    example4(example_list, example_additional_list)
    stop = time.time()
    example4_time.append(stop-start)


fig, ax = plt.subplots(2, 2, figsize=(8,6))

ax[0, 0].scatter(sizes, example1_time, s=10, c='r')
ax[0, 1].scatter(sizes, example2_time, s=10, c='r')
ax[1, 0].scatter(sizes, example3_time, s=10, c='r')
ax[1, 1].scatter(sizes, example4_time, s=10, c='r')

ax[0,0].set_title("example 1")
ax[0,1].set_title("example 2")
ax[1,0].set_title("example 3")
ax[1,1].set_title("example 4")
plt.show()

#hipotheses
from scipy.optimize import curve_fit

def func_1_2(x, a, b):  return a*x + b
def func_3(x, a, b):  return a*(x**2) + b
def func_4(x, a, b):  return a*(x**3) + b

popt_1, pcov_1 = curve_fit(func_1_2, sizes, example1_time)
popt_2, pcov_2 = curve_fit(func_1_2, sizes, example2_time)
popt_3, pcov_3 = curve_fit(func_3, sizes, example3_time)
popt_4, pcov_4 = curve_fit(func_4, sizes, example4_time)

xs = np.arange(1,2000)

plt.clf()
fig, ax = plt.subplots(2, 2, figsize=(8,6))

ax[0,0].scatter(sizes, example1_time, s=10, c='r')
ax[0,0].plot(xs, func_1_2(xs, popt_1[0], popt_1[1]))
ax[0,1].scatter(sizes, example2_time, s=10, c='r')
ax[0,1].plot(xs, func_1_2(xs, popt_2[0], popt_2[1]))
ax[1,0].scatter(sizes, example3_time, s=10, c='r')
ax[1,0].plot(xs, func_3(xs, popt_3[0], popt_3[1]))
ax[1,1].scatter(sizes, example4_time, s=10, c='r')
ax[1,1].plot(xs, func_4(xs, popt_4[0], popt_4[1]))

ax[0,0].set_title("example 1")
ax[0,1].set_title("example 2")
ax[1,0].set_title("example 3")
ax[1,1].set_title("example 4")
plt.show()


#Analiza pokazala, ze
#example1 i example2 sa zlozonosci O(n)
#example3 jest zlozonosci O(n^2)
#example4 jest zlozonosci O(n^3)