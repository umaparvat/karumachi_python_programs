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

def islisteven(li):
    """
    time complexity: O(n) -> iterate list
    space complexity: O(1)
    :param li:
    :return:
    """
    i = 0
    m = li.head
    while m:
        i +=1
        m = m.next
    if i %2 == 0:
        return "list is even"
    else:
        return "list is odd"


def islistevenwithptr(li):
    """
    time complexity: O(n)
    space complexity: O(1)
    :param li:
    :return:
    """
    fast = li.head
    while fast and fast.next:
        fast = fast.next.next
    if fast:
        return "list is odd"
    else:
        return "list is even"

if __name__ == "__main__":
    l1, l2 = base()
    print(f"list l1 is even or odd: {islisteven(l1)}, ptr technique: {islistevenwithptr(l1)}")
    print(f"list l2 is even or odd: {islisteven(l2)}, ptr technique: {islistevenwithptr(l2)}")