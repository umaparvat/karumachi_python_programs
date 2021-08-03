from ctypes import py_object

class Array:
    def __init__(self, size):
        py_array = py_object * size
        self._slot = py_array()
        self._size = size
        self.clear(None)


    def clear(self, value):
        for i in range(self._size):
            self._slot[i] = value

    def __setitem__(self, key, value):
        assert key >= 0 and key < self._size, "Index out of range"
        self._slot[key] = value

    def __getitem__(self, key):
        assert key >= 0 and key < self._size, "Index out of range"
        return self._slot[key]

class Stack:
    def __init__(self, limit=10):
        self._arr = Array(limit)
        self._size = limit
        self._tail = -1

    def push(self, data):
        assert self._tail < self._size, "Stack overflow"
        self._tail += 1
        self._arr[self._tail] = data


    def pop(self):
        assert self._tail is not None and self._tail >= 0, "stack underflow"
        data = self._arr[self._tail]
        self._tail -= 1
        return data

    def size(self):
        return self._tail+1

    def peek(self):
        if self._tail is not None and self._tail > 0:
            return self._arr[self._tail]
        else:
            return None

if __name__ == "__main__":
    arStack = Stack()
    #arStack.pop()
    arStack.peek()
    arStack.push(1)
    arStack.push(2)
    arStack.push(3)
    arStack.push(4)
    arStack.push(5)
    arStack.push(6)
    arStack.push(7)
    arStack.push(8)
    arStack.push(9)
    arStack.push(10)
    print("popping")
    for i in range(arStack.size()):
        print(arStack.pop())


