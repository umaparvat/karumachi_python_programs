class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class IterativeMethodAdd:
    # Function to add two numbers represented by linked list.
    def converTonum(self, node, k):
        digit = 0
        current = node
        while k and current:
            digit += current.data * (10 ** (k - 1))
            k -= 1
            current = current.next
        return digit

    def digitToList(self, num):
        flist = None
        while num > 0:
            rem = num % 10
            num = num // 10
            if not flist:
                flist = Node(rem)
            else:
                t = Node(rem)
                t.next = flist
                flist = t
        return flist

    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        first_len = 0
        second_len = 0
        f = first
        s = second
        while f:
            first_len += 1
            f = f.next
        while s:
            second_len += 1
            s = s.next
        first_digit = self.converTonum(first, first_len)
        second_digit = self.converTonum(second, second_len)
        sum = first_digit + second_digit
        return self.digitToList(sum)


# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        t = Node(data)
        if not self.head:
            self.head = t
        else:
            t.next = self.head
            self.head = t

    def pop(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        return data


class UsingExtraSpaceStack:
    # Function to add two numbers represented by linked list.

    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        f = first
        s = second
        fstack = Stack()
        while f:
            fstack.push(f.data)
            f = f.next
        sstack = Stack()
        while s:
            sstack.push(s.data)
            s = s.next
        balance = 0

        flist = None
        while not fstack.isEmpty() or not sstack.isEmpty():
            sum = 0
            fdata = fstack.pop() if not fstack.isEmpty() else 0
            sdata = sstack.pop() if not sstack.isEmpty() else 0
            sum += fdata + sdata + balance
            balance = sum // 10
            value = sum % 10
            if not flist:
                flist = Node(value)
            else:
                t = Node(value)
                t.next = flist
                flist = t
        if balance > 0:
            t = Node(balance)
            t.next = flist
            flist = t
        return flist

def sumlistusingrecursion(n1, n2):
    if n1 and n2 and n1.next == None and n2.next == None:
        return 0, None
    balance, flist = sumlistusingrecursion(n1.next, n2.next)
    sum = n1.data + n2.data + balance
    balance = sum // 10
    rem = sum % 10
    if not flist:
        flist = Node(rem)
    else:
        t = Node(rem)
        t.next = flist
        flist = t
    return balance, flist



# {
#  Driver Code Starts
# Initial Template for Python 3

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
    for _ in range(int(input())):

        n = int(input())
        arr1 = (int(x) for x in input().split())
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)

        m = int(input())
        arr2 = (int(x) for x in input().split())
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)

        res = IterativeMethodAdd().addTwoLists(LL1.head, LL2.head)
        printList(res)

        res = UsingExtraSpaceStack().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends