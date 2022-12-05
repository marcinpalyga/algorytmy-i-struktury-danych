class Empty(Exception):
    pass

class Deque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = (self._front+self._size-1)%len(self._data)

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size == 0

    def first(self):
        if self._is_empty() == True:
            raise Empty('Deque is empty')
        return self._data[self._front]
    
    def last(self):
        if self._is_empty() == True:
            raise Empty('Deque is empty')
        return self._data[self._back]

    def delete_first(self):
        if self._is_empty() == True:
            raise Empty('Deque is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data) 
        return value
    
    def delete_last(self):
        if self._is_empty() == True:
            raise Empty('Deque is empty')
        value = self._data[self._back]
        self._data[self._back] = None
        self._back = (self._back-1)%len(self._data)
        return value
    
    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._size))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._size))
        avail = (self._back+1)%len(self._data)
        self._data[avail] = e
        self._size += 1
        self._back = (self._front+self._size-1)%len(self._data)
    
    def _resize(self, cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0 
        self._back = (self._front+self._size-1)%len(self._data)
        