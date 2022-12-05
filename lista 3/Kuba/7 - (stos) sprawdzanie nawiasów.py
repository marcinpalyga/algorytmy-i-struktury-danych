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

def is_matched(text):
    opening_brackets = ['[','(', '<', '{']
    closing_brackets = [']', ')', '>', '}']

    a_brackets = Stack()

    for symbol in text:
        if symbol in opening_brackets:
            a_brackets.push(symbol)
        elif symbol in closing_brackets:
            if opening_brackets.index(a_brackets.top()) != closing_brackets.index(symbol):
                return False
            else:
                a_brackets.pop()
    if len(a_brackets) != 0:
        return False
    return True

if __name__ == "__main__":
    import sys
    text = sys.argv[1]

    print( is_matched(text) )
