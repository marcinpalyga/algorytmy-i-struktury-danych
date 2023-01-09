import math

class Empty(Exception):
    pass

class ArrayBinaryTree:
    def __init__(self):
        self._size = 0
        self._tree = [None]

    def root(self, val):
        if self._tree[0] == None:
            self._tree[0] = val
            self._size += 1
            for i in range(2**(self._size)):
                self._tree.append(None)
        else:
            raise Empty("Tree already has a root")

    def _is_root(self, p):
        return self._tree[p] == self._tree[0]

    def _parent(self, p):
        if self._tree[p] == None:
            raise Empty('Node does not exist')
        else:
            if self._tree[p] == self._tree[0]:
                return None
            else:
                return self._tree[math.floor((p-1)/2)]

    def _children(self, p):
        list_child = []
        if self._tree[2*p+1] != None:
            list_child.append(self._tree[2*p+1])
        if self._tree[2*p+2] != None:
            list_child.append(self._tree[2*p+2])
        return list_child

    def _num_children(self, p):
        return len(self._children(p))

    def _is_leaf(self, p):
        return self._num_children(p) == 0

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self.__len__() == 0
    
    def _element(self, p):
        return self._tree[p]

    def _left(self, p):
        return self._tree[2*p+1]

    def _right(self, p):
        return self._tree[2*p+2]

    def _sibling(self, p):
        if p%2 == 1:
            return self._tree[p+1]
        else:
            return self._tree[p-1]

    def _add_left(self, p, val):
        if self._tree[p] == None:
            raise Empty('Node does not exist')
        else:
            self._tree[2*p+1] = val
            self._size += 1
        for i in range(2**(self._size)+1):
            self._tree.append(None)

    def _add_right(self, p, val):
        if self._tree[p] == None:
            raise Empty('Node does not exist')
        else:
            self._tree[2*p+2] = val
            self._size += 1
        for i in range(2**(self._size)+1):
            self._tree.append(None)

    def __str__(self):
        return f'{self._tree}'


t = ArrayBinaryTree()
t.root(1)
print(t)
t._add_left(0,2)
t._add_right(0,3)
print(t)
print(t._num_children(0))
t._add_right(1,4)
t._add_left(1,5)
print(t._is_leaf(1))  
print(t.__len__())
print(t._is_empty())
print(t._children(1))
    

    