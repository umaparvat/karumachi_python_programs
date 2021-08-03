from linkedlist import Node
import ctypes

class XORList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if not self.head:
            n = Node(data)
            n.next = id(n)
            self.head = n
            self.tail = self.head
            print("head is", self.head)
        else:
            n = Node(data)
            prev = self.tail.next^ id(n) if self.tail.next else id(n)
            self.tail.next = prev
            n.next = id(self.tail)
            self.tail = n
            print("value inserted:" ,data, self.tail)

    def traverse(self):
        prev = 0
        x = self.head
        print("traversing list:", x)
        next = 1
        while next:
            print(x.next)
            next = prev^x.next
            print(next)
            if next:
                prev = id(x)
                node = ctypes.cast(next, ctypes.py_object).value
                print(node)
                print("value is :", node.data)


if __name__ == "__main__":
    l = XORList()
    l.insert(5)
    l.insert(6)
    l.insert(10)
    print("insert over")
    l.traverse()