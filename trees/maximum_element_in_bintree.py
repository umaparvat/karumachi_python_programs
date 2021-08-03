import os
import sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def max_element_extra_space(node):
    m = node.val
    queue = Queue()
    queue.enqueue(node)
    while not queue.isEmpty():
        n = queue.dequeue()
        m =max(m, n.val)
        if n.left:
            queue.enqueue(n.left)
        if n.right:
            queue.enqueue(n.right)
    return m

def max_element_without_space(node, m):
    if not node:
        return m
    m = max(m, node.val)
    temp = max_element_without_space(node.left, m)
    m = max(m, temp)
    t = max_element_without_space(node.right, m)
    m = max(m, t)
    return m

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
    print(max_element_extra_space(tree))
    print(max_element_without_space(tree, tree.val))