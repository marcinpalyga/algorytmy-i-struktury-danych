import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def value_nsquared(given_x):

    n = random.randint(1, 10)                          #losowanie rozmiaru tablicy ze wspolczynnikami
    a = [random.randint(1,50) for i in range(0, n)]    #losowanie wartości wspolczynnikow
    result = 0

    for i in range(0, n):
        a_i = a[i]
        x_i = 1

        for j in range(0, i):
            x_i = x_i * given_x
        
        result += x_i * a_i
    
    return a, result

def value_nlogn(given_x):

    n = random.randint(1, 10)                          #losowanie rozmiaru tablicy ze wspolczynnikami
    a = [random.randint(1,50) for i in range(0, n)]    #losowanie wartości wspolczynnikow
    result = 0

    for i in range(0, n):
        a_i = a[i]
        result += a_i * (given_x**i)
    
    return a, result

def horner(given_x, n):

    a = [random.randint(1,50) for i in range(0, n)]    #losowanie wartości wspolczynnikow
    bracket_val = a[n-1]

    start = time.time()
    for i in range(n-1, 0, -1):
        bracket_val = (given_x * bracket_val) + a[i-1]
    end = time.time()
    
    return end-start


###################################

times = [[horner(5, i) for i in (10, 20, 30, 40, 50, 100, 200, 500, 1000)] for j in range(50)]
x_label = [10, 20, 30, 40, 50, 100, 200, 500, 1000]

mean = []
for i in range(9):
    summation = 0
    for j in range(50):
        summation += times[j][i]
    mean.append(summation/len(times))


#hipoteza
def func(x,a,b):
    return a*x + b

popt, pcov = curve_fit(func, x_label, mean)
a, b = popt[0], popt[1]

print("a = {}, b = {}".format(a, b))

x2_label = np.arange(1, 2000)

plt.scatter(x_label, mean, c='r', label='Dane')
plt.plot(x2_label, func(x2_label, a, b), label = 'Model')
plt.xlabel('Rozmiar tablicy ze współczynnikami')
plt.ylabel('Czas obliczenia')
plt.legend()
plt.show()

comparing_model, comparing_func = func(1500, a, b), horner(5, 1500)

print("Oczekiwany czas działania funkcji dla rozmiaru tablicy n = 1500:", comparing_model)
print("Faktyczny czas działania funkcji:", comparing_func)
print("Roznica w czasie:", abs(comparing_model - comparing_func))

#z powyzszych wynikow otrzymujemy potwierdzenie hipotezy, zakladajacej, ze zlozonosc algorytmu Hornera to O(n)