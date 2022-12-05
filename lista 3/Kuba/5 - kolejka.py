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
    
    def first(self):
        if self.is_empty():
            raise queue.Empty('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise queue.Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        return value
    
    def enqueue(self,e):
        self.cleaning()
        if self._size == len(self._data):
            self._resize(1+len(self._data))

        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1
        print(self._data)
        
    def _resize(self,cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0  
    
    def cleaning(self):
        initial_length = len(self._data)
        self._data = [self._data[k] for k in range(initial_length) if self._data[k] is not None]
        self._front = 0
        

Q = Queue()

for i in range(15):
    Q.enqueue(5)