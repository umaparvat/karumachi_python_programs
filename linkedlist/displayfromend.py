from linkedlist import LinkedList

def base():
    l = LinkedList()
    l.insert(2)
    l.insert(3)
    l.insert(17)
    l.insert(24)
    print("linked list:")
    l.traverse()
    return l

def printlintfromend(node):
    if node:
        printlintfromend(node.next)
        print(f"{node.data}")

if __name__ == "__main__":
    l = base()
    print("from end of list:")
    printlintfromend(l.head)