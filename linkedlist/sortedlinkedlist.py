from linkedlist import LinkedList, Node

def base():
    l = LinkedList()
    l.insert(2)
    l.insert(3)
    l.insert(17)
    l.insert(24)
    print("linked list:")
    l.traverse()
    return l

def insertedsorteddata(l, data):
    """
    Time complexity: O(n) => traverse the list
    Space complexity : O(1) => assignments
    :param l:
    :param data:
    :return:
    """
    t = Node(data)
    current = l.head
    prev = None
    while current and current.data < data:
        prev, current = current, current.next
    if not prev:
        # start of the node
        t.next = l.head
        l.head = t
    else:
        t.next = current
        prev.next = t
    l.traverse()


if __name__ == "__main__":
    l = base()
    print(f"inserted 25: ")
    insertedsorteddata(l, 25)
    print(f"inserted 15:")
    insertedsorteddata(l, 15)
    print(f"insertedsorteddata(l, 1)")
    insertedsorteddata(l,1)