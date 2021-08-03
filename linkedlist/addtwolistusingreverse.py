# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    # Function to add two numbers represented by linked list.

    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        f = first
        s = second
        fprev = None
        sprev = None
        while f:
            f.next, fprev, f = fprev, f, f.next
        print(fprev.data)
        while s:
            s.next, sprev, s = sprev, s, s.next
        print(sprev.data)
        balance = 0
        flist = None
        f = fprev
        s = sprev
        while f and s:
            sum = f.data + s.data + balance
            balance = sum // 10
            value = sum % 10
            if not flist:
                flist = Node(value)
            else:
                t = Node(value)
                t.next = flist
                flist = t
            f = f.next
            s = s.next
        while f:
            sum = f.data + balance
            balance = sum // 10
            value = sum % 10
            t = Node(value)
            t.next = flist
            flist = t
            f = f.next
        while s:
            sum = s.data + balance
            balance = sum // 10
            value = sum % 10
            t = Node(value)
            t.next = flist
            flist = t
            s = s.next

        if balance > 0:
            t = Node(balance)
            t.next = flist
            flist = t
        return flist


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    arr1 = [1,7,8,3,6,9,4]
    LL1 = LinkedList()
    for i in arr1:
        LL1.insert(i)
    arr2 = [8,4,8,5,7,2,3,8,3]
    LL2 = LinkedList()
    for i in arr2:
        LL2.insert(i)
    res = Solution().addTwoLists(LL1.head, LL2.head)
    printList(res)
