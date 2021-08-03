from linkedlist.circularList import CirculatList

def base():
    c = CirculatList()
    c.insert(1)
    c.insert(2)
    c.insert(3)
    c.insert(4)
    c.insert(5)
    print("list is")
    c.traverse()
    return c

def splitListtwo(cc):
    slow = cc.head
    fast = cc.head
    while fast:
        fast = fast.next.next
        slow = slow.next
        print("now", fast.data, slow.data, fast.next == cc.head)
        if fast.next == cc.head or fast.next.next == cc.head:
            break

    if fast.next.next == cc.head:
        fast = fast.next
    t = slow.next
    slow.next = cc.head
    cc2 = CirculatList()
    cc2.head = t
    fast.next = t
    print("list 1 after split")
    cc.traverse()
    print("list 2 after split")
    cc2.traverse()

if __name__ == "__main__":
    cc = base()
    splitListtwo(cc)
