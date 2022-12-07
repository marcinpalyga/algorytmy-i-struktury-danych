from copy import copy

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
 

def permutations(n):
    stack = Stack()
    for i in range(n):
        stack.push(i+1)

    current = [[stack.pop()]]
    done = []

    while stack.__len__() !=0:
        next_pop = stack.pop()
        for element in current:
            for i in range(len(element)+1):
                next_per = copy(element)
                next_per.insert(i, next_pop)
                done.append(next_per)
        current = copy(done)
        done = []
    return current
print(permutations(4))