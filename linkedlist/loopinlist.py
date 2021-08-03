from linkedlist import Node, LinkedList

def base():
    head = Node(5)
    b = Node(4)
    c = Node(3)
    d = Node(2)
    e = Node(8)
    f = Node(6)
    g = Node(9)
    h = Node(7)
    head.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    h.next = c

    l = LinkedList()
    l.insert(5)
    l.insert(1)
    l.insert(17)
    l.insert(4)
    return head, l


def hashtableloop(l):
    """
    Time complexity : O(n) => scanning list
    Space complexity : O(n) => hash table
    :param l:
    :return:
    """
    t = l
    if t.next is None:
        return -1
    hashl = dict()
    while t:
        i = id(t)
        if i not in hashl:
            hashl[i] = t.data
        else:
            return "loop exists"
        t = t.next


def floydapproach(l):
    """
    Time complexity: O(n) -> traverse the list
    Space complexity: O(1) -> for slow and fast pointers.
    :param l:
    :return:
    """
    slow = l
    fast = l
    while slow and fast:
        fast = fast.next
        if slow == fast:
            return True
        fast = fast.next
        if slow == fast:
            return True
        slow = slow.next
    return False

def detectstartcycle(l):
    """
    Time complexity: O(n)
    space complexity: O(1)
    :param l:
    :return:
    """
    if not l or not l.next or not l.next.next:
        return None
    slow = l.next
    fast = slow.next
    while slow != fast:
        slow = slow.next
        try:
            fast = fast.next.next
        except AttributeError:
            return None
    slow = l
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

def detectstartcycletortoise(l):
    """
    Time complexity: O(n)
    space complexity: O(1)
    :param l:
    :return:
    """
    if not l or not l.next or not l.next.next:
        return None
    slow = l.next
    fast = slow.next
    while slow != fast:
        slow = slow.next
        try:
            fast = fast.next.next
        except AttributeError:
            return None
    fast = l
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

def lengthofcycle(l):
    """
    time complexity: O(n)
    space complexity: O(1)
    :param l:
    :return:
    """
    if not l or not l.next or not l.next.next:
        return None
    slow = l.next
    fast = slow.next
    while slow != fast:
        slow = slow.next
        try:
            fast = fast.next.next
        except AttributeError:
            return None
    slow = slow.next
    c = 0
    while slow != fast:
        slow = slow.next
        c +=1
    return c



if __name__ == "__main__":
    l, ll = base()
    print(f"\nhashtableloop(l): {hashtableloop(l)}")
    print(f"floydapproach(l): {floydapproach(l)}")
    check = floydapproach(ll.head)
    if check:
        print(f"snailorsnake: snail")
    else:
        print(f"snailorsnake: snake")
    nod = detectstartcycle(l)
    print(f"detectstartcycle(l): {nod.data}")
    print(f"detectstartcycletortoise(l): {detectstartcycletortoise(l).data}")
    print(f"lengthofcycle(l): {lengthofcycle(l)}")