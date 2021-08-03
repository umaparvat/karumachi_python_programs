from linkedlist import LinkedList

def setup():
    l = LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)
    print("original list:")
    l.traverse()
    evenlist = LinkedList()
    evenlist.insert(2)
    evenlist.insert(4)
    evenlist.insert(6)
    return l, evenlist
def bringevenfirstList(li):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Here the even numbers will come first then odd numbers.
    if even and odd mix, all even first then odd.
    if all odd numbers, no change.
    if all even numbers, no change.
    but the even numbers will be in reverse.
    :param li:
    :return:
    """
    current = li.head
    prev = None
    is_prev_even = False
    while current:
        next = current.next
        if current.data % 2 != 0:
            prev = current
            is_prev_even = False
        elif prev and not is_prev_even:
            prev.next = next
            current.next = li.head
            li.head = current
        else:
            prev = current
            is_prev_even = True
        current = next
    print("\n now list is:")
    li.traverse()

def bringevenfirstListnotreverse(li):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Here the even numbers will come first then odd numbers.
    if even and odd mix, all even first then odd.
    if all odd numbers, no change.
    if all even numbers, no change.
    but the even numbers won't be in reverse.
    :param li:
    :return:
    """
    current = li.head
    second = None
    prev = None
    is_prev_even = False
    swapped = False
    while current:
        next = current.next
        if current.data % 2 != 0:
            prev = current
            is_prev_even = False
        elif prev and not is_prev_even:
            prev.next = next
            if not swapped:
                current.next = li.head
                li.head = current
                second = li.head
                swapped = True
            else:
                swapped = True
                temp = second.next
                second.next = current
                current.next = temp
                second = current
        else:
            prev = current
            second = current
            swapped = True
            is_prev_even = True
        current = next
    print("\n now list is:")
    li.traverse()

if __name__ == "__main__":
    l, e = setup()
    bringevenfirstList(l)
    print("\n original even list:")
    e.traverse()
    bringevenfirstList(e)
    print("\nswap even without reverse: ")
    l, e = setup()
    bringevenfirstListnotreverse(l)