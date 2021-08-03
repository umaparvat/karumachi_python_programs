from linkedlist import LinkedList

def base():
    l = LinkedList()
    l.insert(2)
    l.insert(3)
    l.insert(17)
    l.insert(24)
    print("linked list l1:")
    l.traverse()
    l1 = LinkedList()
    l1.insert(2)
    l1.insert(3)
    l1.insert(17)
    print("linked list l2:")
    l1.traverse()
    return l, l1

def reversedataspairs(li):
    """
    Time complexity: O(n)
    space complexity: O(1)
    :param li:
    :return:
    """
    slow = li.head
    fast = slow
    t = None
    while fast and fast.next:
        fast = fast.next
        t = slow.data
        slow.data = fast.data
        fast.data = t
        fast = fast.next
        slow = fast
    li.traverse()

def reversenodespairs(li):
    """
    Time complexity: O(n)
    space complexity: O(1)
    :param li:
    :return:
    """
    t = None
    slow = li.head
    if not slow:
        print("cannot be reversed")
    while slow and slow.next:
        fast = slow.next
        temp = fast.next
        fast.next = slow
        if t:
            t.next = fast
            slow.next = None
        else:
            li.head = fast
            slow.next = t
        t = slow
        slow = temp
    t.next = slow
    li.traverse()


if __name__ == "__main__":
    l1, l2 = base()
    print(f"reversedataspairs(l1):")
    reversedataspairs(l1)
    print(f"reversedataspairs(l2):")
    reversedataspairs(l2)
    l1, l2 = base()
    print(f"reversenodespairs(l1):")
    reversenodespairs(l1)
    print(f"reversenodespairs(l2):")
    reversenodespairs(l2)
