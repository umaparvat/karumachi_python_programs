import os, sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def delete_a_node(node, key):
    """
    Here in a single traversal finding the deepest node(last node in tree) and it's parent
    as well as the del node which has to be deleted.

    find the node to be deleted and store it in del_node.
    the node value and it's parent of the deepest node will be there at the end of while loop
    swap the last node value with key node and delete the last node by assigning the parent child as null.

    The trade off is memory, it stored parent also in the queue.
    :param node:
    :param key: the node to be deleted.
    :return:
    """
    if not node:
        return None
    q = Queue()
    head = node
    parent = None
    q.enqueue((node, parent))
    del_node = None
    while not q.isEmpty():
        node, parent = q.dequeue()
        if node.val == key:
            del_node = node
        if node.left:
            q.enqueue((node.left, node))
        if node.right:
            q.enqueue((node.right, node))
    if del_node:
        del_node.val = node.val
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
        del node
    return head








class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left}, right={self.right}"

def construct_tree():
    root = Node(3)
    root.left = Node(4, left=Node(8, left=Node(12)), right=Node(9))
    root.right = Node(7, left=Node(10), right=Node(11))
    return root

if __name__ == "__main__":
    tree = construct_tree()
    print(tree)
    print(delete_a_node(tree, 4))