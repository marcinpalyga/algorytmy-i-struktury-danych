import random
import time

list_lengths = [i for i in range(30)]
extend_times = [[0 for i in list_lengths] for i in list_lengths]
append_times = [[0 for i in list_lengths] for i in list_lengths]
A = [1, 1, 1]

for j in list_lengths:
    for i in list_lengths:
        B, C = A, A

        appended_list = [random.randint(-20, 20) for j in range(i)]

        start_e = time.process_time()
        B.extend(appended_list)
        stop_e = time.process_time()

        start_a = time.process_time()
        for element in appended_list:
            C.append(element)
        stop_a = time.process_time()

        extend_times[i][j] = stop_e-start_e
        append_times[i][j] = stop_a-start_a

avg_extend = [sum(extend_times[i])/len(list_lengths) for i in list_lengths]
avg_append = [sum(append_times[i])/len(list_lengths) for i in list_lengths]

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

plt.plot(list_lengths, avg_extend, label='Extend')
plt.plot(list_lengths, avg_append, label='Append')
plt.xlabel('Size of appended array')
plt.ylabel('Time')
plt.legend()
plt.show()

####

def a_func(x, a, b):    return (x**2)*a + b
def e_func(x, a, b):    return x*a + b

a_popt, a_pcov = curve_fit(a_func, list_lengths, avg_append)
a_a, a_b = a_popt[0], a_popt[1]
e_popt, e_pcov = curve_fit(a_func, list_lengths, avg_extend)
e_a, e_b = e_popt[0], e_popt[1]

x = np.linspace(1, 50)

plt.clf()
plt.plot(x, a_func(x, a_a, a_b), label='Append - model')
plt.plot(x, e_func(x, e_a, e_b), label='Extend - model')

plt.scatter(list_lengths, avg_append, label='Append', s=20)
plt.scatter(list_lengths, avg_extend, label='Extend', s=20)
plt.xlabel('Size of appended array')
plt.ylabel('Time')
plt.legend()
plt.show()