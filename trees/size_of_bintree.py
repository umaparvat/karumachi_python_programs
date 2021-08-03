import os
import sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def size_of_a_tree(node):
    queue = Queue()
    if not node:
        return 0
    c = 0
    queue.enqueue(node)
    while not queue.isEmpty():
        n = queue.dequeue()
        c += 1
        if n.left:
            queue.enqueue(n.left)
        if n.right:
            queue.enqueue(n.right)
    return c

def findrecursive(node):
    if not node:
        return 0
    return findrecursive(node.left) + findrecursive(node.right) + 1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left.val if self.left else ''}, right={self.right.val if self.right else ''}"
def construct_tree():
    root = Node(3)
    root.left = Node(4, left=Node(8, left=Node(12)), right=Node(9))
    root.right = Node(7, left=Node(10), right=Node(11))
    return root

if __name__ == "__main__":
    tree = construct_tree()
    print(size_of_a_tree(tree))
    print(findrecursive(tree))
