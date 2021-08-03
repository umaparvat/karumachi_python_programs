from linkedlist.linkedlistDS import LinkedListds

def base():
    l = LinkedListds()
    l.insert(2)
    l.insert(3)
    l.insert(17)
    l.insert(24)
    print("linked list:")
    l.traverse()
    return l

def middleoflist(l):
    """
    time complexity: O(n)
    space complexity: O(1)
    :param l:
    :return:
    """
    list_length = 0
    m = l.head
    while m:
        list_length += 1
        m = m.next
    mid = list_length//2
    m = l.head
    i = 0
    while i< mid:
        i += 1
        m = m.next
    return m.data

def middleoflisthash(l):
    """
    time complexity: O(n)
    space complexity: O(n) -> for hash table
    :param l:
    :return:
    """
    hash_table = {}
    list_length = 0
    m = l.head
    while m:
        hash_table[list_length] = m.data
        list_length += 1
        m = m.next
    mid = list_length//2
    return hash_table.get(mid)

def middleusingsinglescan(l):
    """
    time complexity: O(n)
    space complexity: O(1)
    :param l:
    :return:
    """
    slow = fast = l.head
    while fast:
        fast = fast.next
        if not fast:
            return slow.data
        fast = fast.next
        slow = slow.next
    return slow.data

if __name__ == "__main__":
    l = base()
    print(f"middleoflist(l): {middleoflist(l)}")
    print(f"middleoflisthash(l): {middleoflisthash(l)}")
    print(f"middleusingsinglescan(l): {middleusingsinglescan(l)}")