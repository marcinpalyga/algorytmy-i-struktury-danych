from html.parser import HTMLParser

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

class MyHTMLParser(HTMLParser):
    startings = []
    endings = []
    def handle_starttag(self, tag, attrs):
        MyHTMLParser.startings.append(tag)
    def handle_endtag(self, tag):
        MyHTMLParser.endings.append(f'</{tag}>')

def checkHTML(text):
    parser = MyHTMLParser()
    stack = Stack()
    parser.feed(text)
    endings_check = [f'</{i}>' for i in parser.startings]
    startings_check = [f'<{i}>' for i in parser.startings]
    x = text.split()
    for element in x:
        if element in startings_check:
            stack.push(element)
        if element in parser.endings:
            if stack.is_empty():
                return False
            if endings_check.index(element) != startings_check.index(stack.pop()):
                return False
    return stack.is_empty()
            

print(checkHTML("""
<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>
"""))





    