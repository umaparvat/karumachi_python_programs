import os
import sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def search_element_extra_space(node, key):
    m = node.val
    queue = Queue()
    queue.enqueue(node)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n.val == key:
            return True
        if n.left:
            queue.enqueue(n.left)
        if n.right:
            queue.enqueue(n.right)
    return m

def search_without_space(node, key):
    if not node:
        return 0
    if node.val == key:
        return 1
    else:
        t = search_without_space(node.left, key)
        if t == key:
            return 1
        else:
            return search_without_space(node.right, key)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree():
    root = Node(3)
    root.left = Node(4, left=Node(8, left=Node(12)), right=Node(9))
    root.right = Node(7, left=Node(10), right=Node(11))
    return root

if __name__ == "__main__":
    tree = construct_tree()
    print(search_element_extra_space(tree, key=11))
    print(search_without_space(tree, 11))