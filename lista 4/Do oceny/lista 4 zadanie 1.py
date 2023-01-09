import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

class Empty(Exception):
 pass
class LinkedStack:
 #--- -Node class- ---
    class _Node:
        __slots__ = '_element', '_next' #faster memory access

        def __init__(self,element,next):
            self._element = element
            self._next = next

    #--- -Stack methods- ---
    def __init__(self): #empty stack
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


ls = LinkedStack()
czas_push_ls = []
czas_pop_ls = []
for i in range(1, 100000, 1000):
    lista_indeks = []
    for j in range(1, 100000, 1000):
        start = time.perf_counter()
        ls.push(i)
        end = time.perf_counter()
        lista_indeks.append(end-start)
    czas_push_ls.append(sum(lista_indeks)/len(lista_indeks))
for i in range(1, 100000, 1000):
    start = time.perf_counter()
    ls.pop()
    end = time.perf_counter()
    czas_pop_ls.append(end-start)

###analiza push
rozmiar_tab = [i for i in range(1, 100000, 1000)]
plt.scatter(rozmiar_tab, czas_push_ls)
plt.title('Czas wykonania dla metody push')
plt.show()

def wykres(x, a, b):
    return a*x + b

popt_push_1, pcov = curve_fit(wykres, rozmiar_tab, czas_push_ls)

x = np.linspace(1, 100000)

plt.plot(x, wykres(x, *popt_push_1), label = 'Model')
plt.scatter(rozmiar_tab, czas_push_ls, c = 'r', label = 'Dane')
plt.legend()
plt.xlabel('Indeks elementu')
plt.ylabel('Czas oczekiwania')
plt.show()

###analiza pop
rozmiar_tab = [i for i in range(1, 100000, 1000)]
plt.scatter(rozmiar_tab, czas_pop_ls)
plt.title('Czas wykonania dla metody pop')
plt.show()


popt_pop_1, pcov = curve_fit(wykres, rozmiar_tab, czas_pop_ls)

plt.plot(x, wykres(x, *popt_pop_1), label = 'Model')
plt.scatter(rozmiar_tab, czas_pop_ls, c = 'r', label = 'Dane')
plt.legend()
plt.xlabel('Indeks elementu')
plt.ylabel('Czas oczekiwania')
plt.show()


##############################Stack

class Empty(Exception):
    pass
class Stack:
    def __init__(self):
        self._data = [] #nowy pusty stos

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)==0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop() 


s = Stack()
czas_push_s = []
czas_pop_s = []
for i in range(1, 100000, 1000):
    lista_indeks = []
    for j in range(1, 100000, 1000):
        start = time.perf_counter()
        s.push(i)
        end = time.perf_counter()
        lista_indeks.append(end-start)
    czas_push_s.append(sum(lista_indeks)/len(lista_indeks))
for i in range(1, 100000, 1000):
    lista_indeks = []
    for j in range(1, 100000, 1000):
        start = time.perf_counter()
        s.pop()
        end = time.perf_counter()
        lista_indeks.append(end-start)
    czas_pop_s.append(sum(lista_indeks)/len(lista_indeks))
rozmiar_tab = [i for i in range(1, 100000, 1000)]

popt_push_2, pcov = curve_fit(wykres, rozmiar_tab, czas_push_s)
popt_pop_2, pcov = curve_fit(wykres, rozmiar_tab, czas_pop_s)

fig, (ax1, ax2)= plt.subplots(1, 2)

ax1.plot(x, wykres(x, *popt_push_1),c = 'r', label = 'LinkedStack')
ax1.scatter(rozmiar_tab, czas_push_ls, c = 'r')
ax1.plot(x, wykres(x, *popt_push_2),c = 'g', label = "Stack")
ax1.scatter(rozmiar_tab, czas_push_s, c = 'g')
ax1.title.set_text('Metoda push')
ax2.plot(x, wykres(x, *popt_pop_1), c = 'r', label = 'LinkedStack')
ax2.scatter(rozmiar_tab, czas_pop_ls, c = 'r')
ax2.plot(x, wykres(x, *popt_pop_2), c = 'g', label = 'Stack')
ax2.scatter(rozmiar_tab, czas_pop_s, c = 'g')
ax2.title.set_text('Metoda pop')
plt.legend()
plt.show()