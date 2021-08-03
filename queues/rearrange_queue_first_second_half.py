import os, sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def rearrange(q):
    half = q.size() //2
    q1 = Queue()
    for i in range(half):
        q1.enqueue(q.dequeue())
    for i in range(half):
        second = q.dequeue()
        first = q1.dequeue()
        q.enqueue(first)
        q.enqueue(second)
    return q


if __name__ == "__main__":
    q = Queue()
    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(14)
    q.enqueue(15)
    q.enqueue(16)
    q.enqueue(17)
    q.enqueue(18)
    q.enqueue(19)
    q.enqueue(20)
    print(q._lst)
    rearrange(q)
    print(q._lst)
