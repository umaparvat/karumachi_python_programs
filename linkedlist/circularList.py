from linkedlist.linkedlistDS import Node

class CirculatList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        n = Node(data)
        if self.head is None:
            n.next = n
            self.head = n
        elif self.head and self.head.next == self.head:
            self.head.next = n
            n.next = self.head
        else:
            t = self.head.next
            prev = self.head
            while t != self.head:
                prev = t
                t = t.next
            prev.next = n
            n.next = self.head


    def traverse(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next
            if t == self.head:
                break
    def remove(self, data):
        t = self.head.next
        prev = t
        while t and t != self.head:
            prev = t
            t = t.next
            if t.data == data:
                break
        if t:
            prev.next = t.next
            del t
            return data
        return None


if __name__ == "__main__":
    c = CirculatList()
    c.insert(1)
    c.insert(2)
    c.insert(3)
    c.insert(4)
    c.traverse()
    print("removing", c.remove(3))
    print("after removal list is")
    c.traverse()
