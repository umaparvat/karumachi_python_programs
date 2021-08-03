from linkedlist import LinkedList, Node

def base():
    l = LinkedList()
    l.insert(2)
    l.insert(3)
    l.insert(17)
    l.insert(24)
    print("linked list l1:")
    l.traverse()
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(4)
    l1.insert(18)
    print("\nlinked list l2:")
    l1.traverse()
    return l, l1

def mergelist(l1, l2):
    """
    Space complexity: O(n+m) where n and m are list lengths
    Time complexity: O(m+n)
    :param l1:
    :param l2:
    :return:
    """
    i = l1.head
    j = l2.head
    temp = Node(0)
    head = temp
    while i and j:
        if i.data < j.data:
            temp.next = i
            i = i.next
        elif i.data == j.data:
            temp.next = i
            i = i.next
            j = j.next
        else:
            temp.next = j
            j = j.next
        temp = temp.next
    if i:
        temp.next = i
    else:
        temp.next = j
    s = head.next
    while s:
        print(s.data, end=" ")
        s = s.next

if __name__ == "__main__":
    l1, l2 = base()
    print("\nmerger list(l1, l2)")
    mergelist(l1, l2)
