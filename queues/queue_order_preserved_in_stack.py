import os
import sys
sys.path.append(os.getcwd())
from stack.list_stack import Stack
from queues.queue_list import Queue

def QueueOrder(q):
    s = Stack()
    while not q.isEmpty():
        s.push(q.dequeue())
    while not s.isEmpty():
        q.enqueue(s.pop())
    while not q.isEmpty():
        s.push(q.dequeue())
    print(s.peek())
    return s

if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(2)
    q.enqueue(0)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(5)
    s = QueueOrder(q)
    while not s.isEmpty():
        print(s.pop())


