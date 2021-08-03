import sys
import os
sys.path.append(os.getcwd())
from queues.queue_list import Queue

class Stack:
    def __init__(self):
        self._que = Queue()
        self._rvque = Queue()

    def size(self):
        return self._que.size()

    def push(self, data):
        self._que.enqueue(data)

    def isEmpty(self):
        return self._que.isEmpty() and self._rvque.isEmpty()

    def pop(self):
        if not self._que.isEmpty() and not self._rvque.isEmpty():
            return None
        elif not self._rvque.isEmpty():
            return self._rvque.dequeue()
        else:
            while not self._que.isEmpty():
                data = self._que.dequeue()
                self._rvque.enqueue(data)
            del_data = self._rvque.dequeue()
            return del_data

    def top(self):
        if self._rvque.isEmpty() and self._que.isEmpty():
            return None
        elif self._rvque.isEmpty() and not self._que.isEmpty():
            while not self._que.isEmpty():
                data = self._que.dequeue()
                self._rvque.enqueue(data)
            return self._rvque.peek()
        else:
            return self._rvque.peek()

if __name__ == "__main__":
    lsStack = Stack()
    #lsStack.pop()
    #lsStack.top()
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
    while not lsStack.isEmpty():
        print(lsStack.pop())


