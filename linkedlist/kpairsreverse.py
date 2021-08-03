from linkedlist import LinkedList
from linkedlist.stack_list import Stack

def base():
    l = LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)
    l.insert(6)
    l.insert(7)
    l.insert(8)
    l.insert(9)
    l.insert(10)
    print("\nlinked list l1:")
    l.traverse()
    l1 = LinkedList()
    l1.insert("a")
    l1.insert("b")
    l1.insert("c")
    l1.insert("d")
    l1.insert("e")
    l1.insert("f")
    l1.insert("g")
    #print("\nlinked list l2:")
    #l1.traverse()
    return l, l1

def reversek(li, k):
    """
    Time complexity: O(n) actually O(nk) where k is constant.
    space complexity: O(k) => for stack
    :param li:
    :param k:
    :return:
    """
    slow = li.head
    fast = li.head
    s = Stack()
    while fast and fast.next:
        m = k
        while m and fast.next:
            s.push(fast.data)
            fast = fast.next
            m -= 1
        while not s.isempty():
            slow.data = s.pop()
            slow = slow.next

    li.traverse()


def reversekpairswithoutextraspace(li, k):
    """
    Space complexity: O(1)
    Time complexity: O(n)=>O(n/k * 2k)=> O(2n) drop the constant => O(n)
    :param li:
    :param k:
    :return:
    """
    slow = li.head
    if not slow.next:
        print("cannot reverse a single item in list")
    end = slow
    prev = slow
    begin = None
    tail = None
    while slow:
        i = 1
        while i < k and end.next:
            end = end.next
            i += 1
        next = end.next
        temp = None
        while slow and slow != end:
            temp, slow.next, slow = slow, temp, slow.next
        slow.next = temp
        if not begin:
            begin = end
            tail = prev
        else:
            tail.next = end
            tail = prev
        prev = next
        slow = next
        end = next
    li.head = begin
    li.traverse()


def reverseelementsinKpairs(li, k):
    """
    swap elements without space
    space complexity: O(1)
    Time complexity: O(n) => O(n+nk) where k is constant . O(2n)=> again 2 is constant.
    :param li:
    :param k:
    :return:
    """
    slow = li.head
    prev = li.head
    end = li.head
    while slow:
        c = 0
        for i in range(0, k):
            if not end:
                break
            end = end.next
            c += 1
        if not end and c != k:
            break
        t = k
        while t:
            m = t-1
            while m and slow.next:
                fast = slow.next
                temp = slow.data
                slow.data = fast.data
                fast.data = temp
                slow = fast
                m -= 1
            slow = prev
            if not slow.next:
                break
            t -= 1
        slow = end
        prev = end
    li.traverse()


if __name__ == "__main__":
    # l1, l2 = base()
    # print(f"\nreversekpairs(l1, 3)")
    # reversek(l1, 3)
    # print(f"\nreversekpairs(l2, 3)")
    # reversek(l2, 3)
    # l1, l2 = base()
    # print(f"\nreversekpairs(l1, 4)")
    # reversek(l1, 4)
    # print(f"\nreversekpairs(l2, 4)")
    # reversek(l2, 4)
    # l1, l2 = base()
    # print(f"\nreversekpairswithoutextraspace(l1, 3)")
    # reversekpairswithoutextraspace(l1, 3)
    # l1, l2 = base()
    # print(f"\nreversekpairswithoutextraspace(l1, 6)")
    # reversekpairswithoutextraspace(l1, 6)
    l1, l2 = base()
    print(f"\nreverseelementsinKpairs(l1, 6)")
    reverseelementsinKpairs(l1, 6)
    print("\n list l2")
    l2.traverse()
    print(f"\nreverseelementsinKpairs(l2, 3)")
    reverseelementsinKpairs(l2, 3)




