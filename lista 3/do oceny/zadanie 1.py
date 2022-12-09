import ctypes #tablice niskopoziomowe

class DynamicArray:
    
    def __init__(self):
        self._n = 0 #liczba elementów
        self._capacity = 1 #rozmiar tablicy
        self._A = self._make_array(self._capacity) #właściwa tablica
        
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

    def insert(self, k , value):
        B = self._A[:k] + [value] + self._A[k:]
        self._A = B
        self._n += 1
    
    def remove(self, value):
        for i in range(self._n-1):
            if self._A[i] == value:
                self._A = self._A[:i] + self._A[i+1:] 
                self._n -= 1
    
    def expand(self, seq):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        if type(seq) != list:
            raise TypeError('Sequence input is not a list')
        B = self._A + seq
        self._A = B
        self._n += len(seq)

    def __str__(self):
        values = [self._A[i] for i in range(self._n)]
        return f'{values}'

array = DynamicArray()
array._make_array(10)
array.append(1)
print(array)
array.append(2)
print(array)
array.insert(1, 7)
print(len(array))
print(array)
array.insert(3, 8)
print(array)
array.remove(2)
print(array)
print(len(array))
array.expand([9,8,7])
print(array)
print(len(array))