import sys
import os
sys.path.append(os.getcwd())
from stack.list_stack import Stack

class Queue:
    def __init__(self):
        self._stk = Stack()
        self._rvstk = Stack()

    def isEmpty(self):
        return self._stk.isEmpty() and self._rvstk.isEmpty()

    def size(self):
        return self._stk.size()

    def enqueue(self, data):
        self._stk.push(data)

    def dequeue(self):
        return self._reverse_push(state=True)

    def top(self):
        if self._rvstk.isEmpty() and self._stk.isEmpty():
            return None
        return self._reverse_push()

    def _reverse_push(self, state=False):
        """
        Time complexity: O(n), space complexity: O(n)
        Amortized: O(1), space complexity: O(n)
        :param state:
        :return:
        """
        assert not self._stk.isEmpty() and not self._rvstk.isEmpty(), "queue underflow"
        if self._rvstk.isEmpty() and not self._stk.isEmpty():
            while not self._stk.isEmpty():
                self._rvstk.push(self._stk.pop())
        return self._rvstk.peek() if not state else self._rvstk.pop()



if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("top element", q.getTop())
    print("dequeue")
    while not q.isEmpty():
        print(q.dequeue())


