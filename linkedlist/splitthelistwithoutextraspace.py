"""
Given a list, Listi = {A 1, A2 , ••• An-I• An} with data,
reorder it LO {A1, An, A2, An- 1·····} without
using any extra space.
"""
from linkedlist import LinkedList

def setup():
    arr1 = [1,7,8,3,6,9,4,5]
    LL1 = LinkedList()
    for i in arr1:
        LL1.insert(i)
    print("\n list is:\n")
    LL1.traverse()
    return LL1

def findMiddleNode(node):
    slow = node
    fast = node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverseNodesInPlace(node):
    current = node.next
    prev = node
    while current:
        current.next, prev, current = prev, current, current.next
    temp = node.next
    node.next = prev
    temp.next = None



def reorder(node):
    """
    Alg:
        1. Go upto middle node using floyd algorithm(hare tortoise)
        2. reverse the list from the middle to last.
        3. traverse from first node and add the middle node between 1 and 2.
    Time Complexity: O(n)
    Space complexity: O(1)

    :param node:
    :return:
    """
    midptr = findMiddleNode(node)
    reverseNodesInPlace(midptr)
    current = node
    reverseptr = midptr.next
    while current != midptr and reverseptr:
        current_next = current.next
        mid_next = reverseptr.next
        current.next = reverseptr
        reverseptr.next = current_next
        reverseptr = mid_next
        current = current_next
    midptr.next = None
    print("\nAfterReorderList:\n")
    c = node
    while c:
        print(c.data, end=" ")
        c = c.next

if __name__ == "__main__":
    li = setup()
    reorder(li.head)