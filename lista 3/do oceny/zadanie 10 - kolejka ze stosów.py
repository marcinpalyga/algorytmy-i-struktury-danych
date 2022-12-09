import queue

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
            raise queue.Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise queue.Empty('Stack is empty')
        return self._data.pop()

class Queue:
    def __init__(self):
        self.Stack_enqueue = Stack()
        self.Stack_dequeue = Stack()

    def dequeue(self):
        value = self.Stack_dequeue.pop()
        self.Stack_enqueue._data = self.Stack_dequeue._data.copy()
        self.Stack_enqueue._data.reverse()

        return value

    def enqueue(self, e):
        self.Stack_enqueue.push(e)
        self.Stack_dequeue._data = self.Stack_enqueue._data.copy()
        self.Stack_dequeue._data.reverse()



queue = Queue()
for i in range(10):
    queue.enqueue(i)
    print(queue.Stack_enqueue._data)

for i in range(10):
    queue.dequeue()
    print(queue.Stack_enqueue._data)