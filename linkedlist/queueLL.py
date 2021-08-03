from linkedlist import LinkedList, Node

class QueueLL:
    def __init__(self):
        self.ll = LinkedList()
    def enqueue(self, data):
        self.ll.insert(data)
    def dequeue(self):
        if not self.ll.head:
            return "empty queue"
        return self.ll.remove(self.ll.head.data)
    def top(self):
        return self.ll.head.data
    def traverse(self):
        self.ll.traverse()
