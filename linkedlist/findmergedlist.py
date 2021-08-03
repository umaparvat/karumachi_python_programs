from linkedlist import Node
from linkedlist.stack_list import Stack
import ctypes

def base():
    ll = Node(5)
    b = Node(4)
    c = Node(3)
    d = Node(2)
    e = Node(8)
    f = Node(6)
    g = Node(9)
    h = Node(7)
    ll.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h

    al = Node(15)
    ab = Node(14)
    ac = Node(23)
    ad = Node(40)
    ae = Node(1)
    al.next = ab
    ab.next = ac
    ac.next = ad
    ad.next = ae
    ae.next = c
    print("l1:")
    s = ll
    while s:
        print(s.data)
        s = s.next
    s = al
    print("l2:")
    while s:
        print(s.data)
        s = s.next
    return ll, al

def bruteforceFindMergePoint(l1, l2):
    """
    l1 length m and l2 length n
    Time complexity O(m*n)
    Space complexity: O(1)
    :param l1:
    :param l2:
    :return:
    """
    if not l1 or not l2:
        return None
    print("in bruteforce")
    m = l1
    n = l2
    while m:
        while n:
            if m == n:
                return n
            n = n.next
        m = m.next
        n = l2

def findmergeusingsort(l1, l2):
    """
    Time complexity: O(mlogm) + O(nlogn) + O(m+n)
    Space complexity: O(m+n) => space for m array and n array
    :param l1:
    :param l2:
    :return:
    """
    s = []
    m = l1
    while m:
        s.append(id(m))
        m=m.next
    s.sort() # timsort O(nlogn)
    n = l2
    t = []
    while n:
        t.append(id(n))
        n = n.next
    t.sort() # timsort O(nlogn)
    i = 0
    j = 0
    while i < len(s) and j < len(t): # O(m + n)
        if s[i] < t[j]:
            i += 1
        elif s[i] == t[j]:
            return ctypes.cast(s[i], ctypes.py_object).value
        else:
            j += 1

def mergenodeusinghash(l1, l2):
    """
    Time complexity: O(m)+ O(n) => m l1 list length and l2 list length
    Space complexity: O(m) or O(n) => if l1 list , space O(m) else O(n) for l2 list
    :param l1:
    :param l2:
    :return:
    """
    hashnode = dict()
    m = l1
    while m:
        hashnode[m] = 1
        m = m.next
    n = l2
    while n:
        if hashnode.get(n):
            return n
        n = n.next

def mergenodeusingstack(l1, l2):
    """
    Time complexity: O(m) + O(n)
    Space complexity: O(m) + O(n)
    :param l1:
    :param l2:
    :return:
    """
    s1 = Stack()
    m = l1
    if not l2 or not l1:
        return None
    while m:
        s1.push(m)
        m = m.next
    n = l2
    s2 = Stack()
    while n:
        s2.push(n)
        n = n.next
    a = None
    b = None
    c = None
    while not s1.isempty() and not s2.isempty():
        a = s1.pop()
        b = s2.pop()
        if a != b:
            break
        c = a
    return c

def mergenodefirstrepeatingapproach(l1, l2):
    """
    time complexity: O(m+n) -> first while loop and for loop a
    Space complexity: O(m+n) => for array and hash
    :param l1:
    :param l2:
    :return:
    """
    a = []
    m, n = l1, l2
    while m and n:
        a.append(m.data)
        a.append(n.data)
        m, n = m.next, n.next
    table = {}
    for each in a:
        if each in table and table.get(each) == 1:
            table[each] = -2
        elif each in table and table.get(each) < 0:
            table[each] -= 1
        elif each != "":
            table[each] = 1
        else:
            table[each] = 0
    maximum = 0
    firstrepeat = None
    for each in a:
        if table.get(each) < maximum:
            maximum = table.get(each)
            firstrepeat = each
    return firstrepeat

def binsearch(arr, elem):
    """
    Time complexity: O(logn )
    Space complexity: O(1)
    :param arr:
    :param elem:
    :return:
    """
    l = 0
    high = len(arr)-1
    while l <= high:
        mid = (l+high)//2
        if arr[mid] < elem:
            l = mid+1
        elif arr[mid] == elem:
            return True
        else:
            high = mid-1
    return False

def mergernodeusingsortsearch(l1, l2):
    """
    Time complexity: O(nlogn or mlogm)
    Space complexity: O(m or n)
    :param l1:
    :param l2:
    :return:
    """
    m, n = l1, l2
    a =[]
    while m:
        a.append(m.data) # O(m) or O(n) space depends on list chosen
        m = m.next

    a.sort() # O(nlogn) or O(mlogm)
    while n:
        if binsearch(a, n.data): # either mlogm or nlogn depends on the list size
            return n.data
        n = n.next

def mergenodeusinglength(l1, l2):
    """
    Time complexity: O(m) or O(n)
    space complexity: O(1)
    :param l1:
    :param l2:
    :return:
    """
    m = l1
    n = l2
    c1 = 0
    while m:
        c1 += 1
        m = m.next
    c2= 0
    while n:
        c2 += 1
        n = n.next
    m, n = l1, l2
    if c2 >= c1:
        i = 0
        diff = c2-c1
        while n and i < diff:
            i+=1
            n = n.next
    else:
        i = 0
        diff = c1 - c2
        while m and i < diff:
            i+=1
            m = m.next

    while m and n:
        if m == n:
            return m.data
        m, n = m.next, n.next









if __name__ == "__main__":
    l1, l2 = base()
    node = bruteforceFindMergePoint(l1, l2)
    print(f"merging node: {node.data}")
    snode = findmergeusingsort(l1, l2)
    print(f"sorting technique merging node: {snode.data}")
    hashn = mergenodeusinghash(l1, l2)
    print(f"HAshing technique find merge node: {hashn.data}")
    stacknode = mergenodeusingstack(l1, l2)
    print(f"stack techinque find merge node: {stacknode.data}")
    d = mergenodefirstrepeatingapproach(l1, l2)
    print(f"mergenode using first repeating element approach:{d}")
    ss = mergernodeusingsortsearch(l1, l2)
    print(f"find merge node using sort and search method: {ss}")
    d = mergenodeusinglength(l1, l2)
    print(f"merge node using length value: {d}")
