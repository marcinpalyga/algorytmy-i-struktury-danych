import queue

class Queue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def top(self):
        if self.is_empty():
            raise queue.Empty('Queue is empty')
        return self._data[self._size - 1]                         
    
    def pop(self):
        if self.is_empty():
            raise queue.Empty('Queue is empty')
        value = self._data[self._size - 1] 
        self._data[self._size - 1] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        return value
    
    def push(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def _resize(self,cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0 

import time
import random

size = [i for i in range(30)]
push_times = [[None for i in size] for j in size]
pop_times = [[None for i in size] for j in size]
top_times = [[None for i in size] for j in size]
D = Queue()

for m in size:
    for n in size:
        push_start = time.process_time()
        D.push(n)
        push_stop = time.process_time()
    
        top_start = time.process_time()
        D.top()
        top_stop = time.process_time()

        push_times[n][m] = push_stop - push_start
        top_times[n][m] = top_stop - top_start

for m in size:
    for n in size:
        pop_start = time.process_time()
        D.pop()
        pop_stop = time.process_time()

        pop_times[n][m] = pop_stop - pop_start

push_avg = [sum(push_times[i])/len(size) for i in size]
pop_avg = [sum(pop_times[i])/len(size) for i in size]
top_avg = [sum(top_times[i])/len(size) for i in size]
    


import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

plt.plot(size, push_avg, label='push')
plt.plot(size, pop_avg, label='pop')
plt.plot(size, top_avg, label='top')

plt.xlabel('Size of stack')
plt.ylabel('Time')

plt.legend()
plt.show()

##wszystkie sa zlozonosci O(1)
##wychylenia dla funkcji push sa spowodowane rozszerzaniem wielkosci tablicy

def f(x, a, b):    return x*a + b

push_popt, push_pcov = curve_fit(f, size, push_avg)
push_a, push_b = push_popt[0], push_popt[1]
pop_popt, pop_pcov = curve_fit(f, size, pop_avg)
pop_a, pop_b = pop_popt[0], pop_popt[1]
top_popt, top_pcov = curve_fit(f, size, top_avg)
top_a, top_b = top_popt[0], top_popt[1]


x = np.linspace(1, 50)

plt.clf()
plt.plot(x, f(x, push_a, push_b), label='Push - model')
plt.plot(x, f(x, pop_a, pop_b), label='Pop - model')
plt.plot(x, f(x, top_a, top_b), label='Top - model')

plt.scatter(size, push_avg, label='Push', s=20)
plt.scatter(size, pop_avg, label='Pop', s=20)
plt.scatter(size, top_avg, label='Top', s=20)
plt.xlabel('Size of stack')
plt.ylabel('Time')
plt.legend()
plt.show()