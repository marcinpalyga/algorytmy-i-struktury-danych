import queue

class Queue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise queue.Empty('Queue is empty')
        return self._data[self._front]
    
    def last(self):
        if self.is_empty():
            raise queue.Empty('Queue is empty')
        return self._data[self._back]
    
    def delete_first(self):
        if self.is_empty():
            raise queue.Empty('Queue is empty')

        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)
        self._size -= 1

        self.cleaning()
        return value
    
    def delete_last(self):
        if self.is_empty():
            raise queue.Empty('Queue is empty')

        value = self._data[self._back]
        self._data[self._back] = None
        self._back = (self._size + self._front - 2)
        self._size -= 1

        self.cleaning()
        return value
    
    def add_first(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        
        self._resize(len(self._data)+1, True)

        avail = (self._front)
        self._data[avail] = e
        self._size += 1

        self.cleaning()

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))

        self._resize(len(self._data))

        avail = (self._size+self._front)
        self._data[avail] = e
        self._size += 1

        self.cleaning()
        
    def _resize(self, cap, moving_elements=False):
        old = self._data
        walk = self._front
        self._back = self._size + self._front
        self._data = [None]*cap

        if moving_elements:   
            old.insert(0, None)
            walk = self._front

        for k in range(self._size): #only existing elements
            if not moving_elements:
                self._data[k] = old[walk]
                walk = (1 + walk)%len(old)
            elif moving_elements:
                self._data[k+1] = old[walk+1]
                walk = (1 + walk)%(len(old)-1)

        self._front = 0
    
    def cleaning(self):
        initial_length = len(self._data)
        self._data = [self._data[k] for k in range(initial_length) if self._data[k] is not None]
        self._front = 0
        self._back = self._size - 1
    
        
D = Queue()

for i in range(15):
    D.add_first(5)
    D.add_last(3)

for i in range(15):
    print( D.delete_first() )
    print( D.delete_last() )





