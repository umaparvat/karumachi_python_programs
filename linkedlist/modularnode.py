from linkedlist import LinkedList, Node
from random import randint

def setup(range_end, random = None):
    l = LinkedList()
    if not random:
        for i in range(0, range_end):
            l.insert(i)
    else:
        for i in range(0, range_end):
            l.insert(randint(1,100))
    print("\nnow list:")
    l.traverse()
    return l

def modularNode(node, k):
    """
    Time complexity: O(n)
    Space complexity: O(1) -> for counter variable
    :param node:
    :param k:
    :return:
    """
    counter = 1
    slow = node
    fast = node
    while fast and fast.next:
        if counter % k == 0:
            slow = fast
            counter = 0
        fast = fast.next
        counter += 1
    return  slow

def modularkNodefromend(node, k):
    """
    Time complexity: O(n)
    Space complexity: O(1) -> for counter variable
    :param node:
    :param k:
    :return:
    """
    counter = 0
    slow = node
    fast = node
    while counter < k and fast:
        counter += 1
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    return slow

def nbykthelement(node, k):
    counter = 0
    kele = None
    current = node
    while current:
        if counter % k == 0:
            if not kele:
                kele = node
            else:
                kele = kele.next
        counter += 1
        current = current.next
    return kele

def sqrtofnnode(node):
    slow = node
    fast = node
    i = j = 1
    while fast:
        if i == j*j:
            slow = slow.next
            j += 1
        i += 1
        fast = fast.next

    return slow

def medianofnumbers(node):
    """
    Assume the input is sorted linked list
    Median can be found in ascending order of numbers
    if n is odd, median is middle value
    if n is even, median is middle + next / 2
    Time complexity: O(n) -> single scan throughout list
    Space complexity : O(1)
    :param node:
    :return:
    """
    slow = node
    fast = node
    while fast and fast.next and fast.next.next:
        fast = fast.next
        if not fast:
            break
        fast = fast.next
        slow = slow.next
    if fast.next == None:
        return slow.data
    median = (slow.data + slow.next.data) // 2
    return median


def mergelist(list1_node, list2_node):
    """
    Merging two sorted lists.
    Time complexity: O(n) or O(m) where n and m are list lengths
    Space complexity: O(1)
    :param list1_node:
    :param list2_node:
    :return:
    """
    ptr = Node(0)
    begin = ptr
    while list1_node and list2_node:
        if list1_node.data < list2_node.data:
            ptr.next = list1_node
            list1_node = list1_node.next
        else:
            ptr.next = list2_node
            list2_node = list2_node.next
        ptr = ptr.next
    if list1_node:
        ptr.next = list1_node
    if list2_node:
        ptr.next = list2_node
    begin = begin.next
    return begin

def middleOfList(node):
    slow = node
    begin = slow
    fast = node.next
    prev = fast
    while fast and fast.next:
        fast = fast.next
        if not fast:
            break
        prev = fast.next if fast.next else fast
        fast = fast.next
        slow = slow.next
    next = slow.next
    slow.next = None
    prev.next = None
    return begin, next

def Mergesort(node):
    if not node:
        return
    if node and node.next == None:
        return node
    beforemid, aftermid = middleOfList(node)
    left = Mergesort(beforemid)
    right = Mergesort(aftermid)
    return mergelist(left, right)

def medianInUnsortedList(node):
    """
    Input list is unsorted list.
    Find the median in unsortedlist
    Time complexity: O(nlogn) +O(n) => O(nlogn)
    Space complexity: O(1)
    :param node:
    :return:
    """
    sorted_list = Mergesort(node)
    print(f"\nmedian is:", medianofnumbers(sorted_list))



if __name__ == "__main__":
    # l = setup(20)
    # print(f"\nfind {19- (19%3)} thnode:", modularNode(l.head, 3).data)
    # l = setup(21)
    # print(f"\nfind {20 - (20 % 3)} thnode:", modularNode(l.head, 3).data)
    # l = setup(20)
    # print(f"\nfind 3rd node from end:", modularkNodefromend(l.head, 3).data)
    # l = setup(21)
    # print(f"\nfind 3 rd node from end:", modularkNodefromend(l.head, 3).data)
    # l = setup(20)
    # print(f"\nfind {19/3}rd node:", nbykthelement(l.head, 3).data)
    # l = setup(21)
    # print(f"\nfind {20/3} rd node:", nbykthelement(l.head, 3).data)
    # l= setup(5)
    # print(f"\n find sqtr of 5 nodes:", sqrtofnnode(l.head).data)
    # l = setup(9)
    # print(f"\n find sqtr of 9 nodes:", sqrtofnnode(l.head).data)
    # l = setup(8)
    # print(f"\nmedian of 8 numbers:" ,medianofnumbers(l.head))
    # l = setup(13)
    # print(f"\n median of 13 numbers:", medianofnumbers(l.head))
    randomlist1 = setup(9, True)
    medianInUnsortedList(randomlist1.head)
    randomlist1 = setup(10, True)
    medianInUnsortedList(randomlist1.head)






