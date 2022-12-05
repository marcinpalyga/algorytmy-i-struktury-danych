import ctypes                                           #tablice niskopoziomowe

class DynamicArray:
    
    def __init__(self):
        self._n = 0                                     #liczba elementów
        self._capacity = 1                              #rozmiar tablicy
        self._A = self._make_array(self._capacity)      #właściwa tablica
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
        
    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        
    def _make_array(self,c):
        return (c*ctypes.py_object)()

###zadanie
    def insert(self, k, value):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        else:
            if self._n == self._capacity:       self._resize(2 * self._capacity)
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i-1]
            self._A[k] = value
            self._n += 1
    
    def remove(self, value):
        value_presence = False
        for i in range(self._n-1):
            if (self._A[i] == value) and (value_presence == False):
                value_presence = True
                self._n -= 1
                self._A[i] = self._A[i+1]
            elif value_presence:
                self._A[i] = self._A[i+1]
        if not value_presence:
            if self._A[self._n-1] == value: 
                self._A[self._n-1] = None
                self._n -= 1
            else:
                raise ValueError('value not in array')

    def expand(self, seq):
        if type(seq) != list:
            raise TypeError('given value is not a sequence (try using "append()" method)')
        else:
            self._capacity += len(seq)

            for element in seq:
                self._n += 1
                self._A[self._n-1] = element
                

    def __str__(self):
        copy_A = [self._A[i] for i in range(self._n)]
        return f'{copy_A}'

        

X = DynamicArray()
X._resize(10)
for i in range(10):     X.append(i)

print(X)
X.insert(0, 100)

print(X)
X.remove(100)

print(X)
X.expand([2,3,4,5])

print(X)