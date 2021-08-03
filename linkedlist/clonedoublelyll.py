from linkedlist.doublylinkedlist import DoublePtrNode

def setup():
    head = DoublePtrNode(1)
    second = DoublePtrNode(2)
    third = DoublePtrNode(3)
    fourth = DoublePtrNode(4)
    fifth = DoublePtrNode(5)
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    head.prev = third
    second.prev = head
    third.prev = fifth
    fourth.prev = third
    fifth.prev = second
    return head

def cloneList(node):
    """
    1. Place a new node between current and next node. that new node prev pointer will be
       None. whereas the current node prev pointer points to a random node.
    2. Look for a node whose prev pointer is None and modify the prev pointer
       to the old node prev pointers next node.
       when first assignment happens, that's the first node of the new list
    3. make the first node of the new list next pointer as next.next. to create a new list.

    :param node:
    :return:
    """
    current = node
    print("original list:")
    while current:
        next_node = current.next
        new_node = DoublePtrNode(data=current.data, prev=None, next=next_node)
        current.next = new_node
        print(current, end=" ")
        current = next_node
    newl_node = node
    old_node = None
    begining_list = None
    while newl_node:
        if newl_node.prev == None:
            newl_node.prev = old_node.prev.next
            if not begining_list:
                begining_list = newl_node
            old_node = newl_node.next
            next_node = newl_node.next.next if newl_node.next else None
            newl_node.next = next_node
            newl_node = next_node
        else:
            next_node = newl_node.next
            old_node = newl_node
            old_node.next = newl_node.next.next
            newl_node.next = newl_node.next.next if newl_node.next else newl_node.next
            newl_node = next_node
    new_list_head_node = begining_list
    print("\nnew list:")
    while new_list_head_node:
        print(new_list_head_node, end=" ")
        new_list_head_node = new_list_head_node.next

if __name__ == "__main__":
    nodes = setup()
    cloneList(nodes)









