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

def reversell(l):
    """
    reverse list in place with 2 variables
    Time complexity: O(n)
    Space complexity: O(1)

    :param l:
    :return:
    """
    prev = None
    cur = l.head
    while cur:
        prev, cur.next, cur = cur, prev, cur.next
    l.head = prev
    l.traverse()

def reversellwith3(l):
    """
    reverse list in place with 3 variables
    Time complexity: O(n)
    Space complexity: O(1)

    :param l:
    :return:
    """
    prev = None
    cur = l.head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    l.head = prev
    l.traverse()

def recursivereverse(n):
    """
    T(n) = T(n-1)+O(1) = O(n) => Master theorem subract and subtitute O(n^(k+1) here k is 0
    space complexity: O(n) => for stack
    :param n:
    :return:
    """
    if n == None:
        return n
    if n.next == None:
        return n

    node1 = recursivereverse(n.next)
    n.next.next = n
    n.next = None
    return node1




if __name__ == "__main__":
    print("original list")
    l = base()
    print("after reverse")
    reversell(l)
    print("again reverse")
    reversellwith3(l)
    print("recursivereverse")
    n = l.head
    ret = recursivereverse(n)
    l.head = ret
    l.traverse()
