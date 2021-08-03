from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
    
    def push(self, data):
        self.list.insert(data=data, pos=0)

    def pop(self):
        if self.list.isempty():
            return None
        data = self.list.remove(self.list.head.data)
        #print(f"removed:{data}")
        return data
    
    def seek(self):
        if self.list.isempty():
            return None
        return self.list.head.data
    
    def traverse(self):
        self.list.traverse()        
    def isempty(self):
        return self.list.isempty()

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(2)
    s.push(3)
    s.traverse()
    print("removed elements")
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
