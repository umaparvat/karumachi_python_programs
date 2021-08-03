
class DoublePtrNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    def __str__(self):
        return f"Node({id(self.prev)}, {self.data}, {id(self.next)})"

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        n = DoublePtrNode(data)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            prev = self.head
            while temp:
                prev = temp
                temp = temp.next
            n.prev = prev
            prev.next = n

    def remove(self, data):
        if self.head is None:
            return None
        temp = self.head
        while temp and temp.data != data:
            temp = temp.next
        if temp and temp.data == data:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            if temp == self.head:
                self.head = temp.next
            del temp
            return data
        return None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next

if __name__ == "__main__":
    doubleLl = DoublyLinkedList()
    doubleLl.insert(1)
    doubleLl.insert(2)
    doubleLl.insert(3)
    doubleLl.insert(4)
    doubleLl.insert(5)
    doubleLl.traverse()
