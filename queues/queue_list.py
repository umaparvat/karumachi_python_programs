
class Queue:
    def __init__(self):
        self._lst = list()

    def enqueue(self, data):
        self._lst.append(data)

    def dequeue(self):
        assert len(self._lst) > 0, "queue underflow"
        return self._lst.pop(0)

    def isEmpty(self):
        return len(self._lst) <= 0

    def size(self):
        return len(self._lst)

    def peek(self):
        if len(self._lst) > 0:
            return self._lst[0]
        else:
            return None