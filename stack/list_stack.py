class Stack:
    def __init__(self):
        self._lst = list()
        self._tail = -1

    def size(self):
        return self._tail+1

    def push(self, data):
        self._tail += 1
        self._lst.append(data)

    def pop(self):
        assert self._tail >= 0, "stack underflow"
        data = self._lst.pop()
        self._tail -= 1
        return data
    
    def peek(self):
        if self._tail >= 0:
            return self._lst[self._tail]
        else:
            return None
    def isEmpty(self):
        return self._tail == -1

if __name__ == "__main__":
    lsStack = Stack()
    #lsStack.pop()
    lsStack.peek()
    lsStack.push(1)
    lsStack.push(2)
    lsStack.push(3)
    lsStack.push(4)
    lsStack.push(5)
    lsStack.push(6)
    lsStack.push(7)
    lsStack.push(8)
    lsStack.push(9)
    lsStack.push(10)
    print("popping")
    for i in range(lsStack.size()):
        print(lsStack.pop())