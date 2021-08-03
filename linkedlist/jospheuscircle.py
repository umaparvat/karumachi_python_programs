import os, sys
sys.path.append(os.getcwd())
from linkedlist.circularList import CirculatList

def jospheuscircle(m, n):
    """
    Time complexity : O(m)
    Space complexity: O(m) -> circular list creation.
    :param m:
    :param n:
    :return:
    """
    c = CirculatList()
    for i in range(0,m):
        c.insert(i)
    fast = c.head
    prev = c.head
    executed = list()
    while fast.next != fast:
        for i in range(0, n):
            """n iterations"""
            prev = fast
            fast = fast.next
        prev.next = fast.next
        executed.append(fast.data)
        fast = fast.next
        prev = fast
    print("executed order", executed)
    print("survival is ", fast.data)

def josphesucirclerecursive(prev, fast, executeorder, counter, exeuctedlist):
    if fast.next == fast:
        return prev, fast, exeuctedlist
    if counter < executeorder:
        prev = fast
        fast = fast.next
        counter += 1
    else:
        return prev, fast, exeuctedlist
    prev, fast, exeuctedlist = josphesucirclerecursive(prev, fast, executeorder, counter, exeuctedlist)
    if fast.next != fast:
        exeuctedlist.append(fast.data)
    prev.next = fast.next
    fast = fast.next
    prev = fast
    counter = 0
    return josphesucirclerecursive(prev, fast, executeorder, counter, exeuctedlist)

# def josphesucirclerecursiveot(prev, fast, executeorder, counter, exeuctedlist):
#     if fast.next == fast:
#         return prev, fast
#     if counter%executeorder == 0:
#         exeuctedlist.append(fast.data)
#         prev.next = fast.next
#         prev = fast
#         fast = fast.next
#         return prev, fast
#     prev = fast
#     fast = fast.next
#     counter += 1
#     return josphesucirclerecursiveot(prev, fast, executeorder, counter, exeuctedlist)

if __name__ == "__main__":
    jospheuscircle(6,3)
    c = CirculatList()
    for i in range(0,6):
        c.insert(i)
    fast = c.head
    prev = c.head
    _, survival, executedpeople = josphesucirclerecursive(prev, fast, 3, 0, [])
    print("executed order", str(executedpeople))
    print("survival", survival.data)
    # exlist = []
    # _, survival = josphesucirclerecursiveot(prev, fast, 3, 0, exlist)
    # print("otexecuted order", str(exlist))
    # print("otsurvival", survival.data)