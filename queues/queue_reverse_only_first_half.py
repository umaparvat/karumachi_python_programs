import os, sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue


def rearrange(q, k):
    s = []
    for i in range(k):
        s.append(q.dequeue())
    while s:
        q.enqueue(s.pop())
    for i in range(q.size()-k):
        q.enqueue(q.dequeue())
    return q


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)
    q.enqueue(90)
    print(q._lst)
    rearrange(q, 4)
    print(q._lst)
