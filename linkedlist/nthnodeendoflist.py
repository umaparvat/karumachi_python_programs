from linkedlist import LinkedList

def base():
    l = LinkedList()
    l.insert(5)
    l.insert(1)
    l.insert(17)
    l.insert(4)
    print("linked list:")
    l.traverse()
    return l

def nthNodeLLHashTable(linkedl, n):
    """
        Time complexity = O(m) to created hash table
        Space complexity = O(m) space for hash table
    """
    if n < 0:
        return None
    t = linkedl.head
    hashll = dict()
    c = 0
    while t:
        c = c+1
        hashll[c], t = t, t.next
    m = len(hashll)
    node = hashll.get((m-n)+1)
    return node.data if node else None


def nthNodeLL2traversal(linkedl, n):
    """
        2 traversal of the list T(n) = O(n) + O(n) ~= O(n)
        Time Complexity = O(n) size of the linkedl
        Space Complexity = O(1)
    """
    if n < 0:
        return None
    c = 0
    t = linkedl.head
    while t:
        c += 1
        t = t.next
    if c < n:
        return "fewer number of nodes in the list"
    m = c-n # (c-1)-(n-1)  or c-n where c = len(linkedl)
    c = 0
    t = linkedl.head
    while c != m:
        c += 1
        t = t.next
    return t.data

def nthNodeLL1traversal(linkedl, n):
    """
        single traversal O(n)
        Time complexity: O(n)
        Space complexity: O(1)
    """
    if n < 0:
        return None    
    t = linkedl.head
    ptrN = linkedl.head
    c = 0
    while c< n and t:
        c += 1
        t = t.next
    if t is None and c < n:
        return "fewer number of nodes in the list"
    while t:
        ptrN, t = ptrN.next, t.next
    return ptrN.data

if __name__ == "__main__":
    l = base()
    print(f"\nnthNodeLLHashTable(l, 3): {nthNodeLLHashTable(l, 3)}")
    print(f"nthNodeLL2traversal(l, 2): {nthNodeLL2traversal(l, 2)}")
    print(f"nthNodeLL1traversal(l, 5): {nthNodeLL1traversal(l, 5)}")
