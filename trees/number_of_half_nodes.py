import os, sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def half_nodes(node):
    depth = 1
    if not node:
        return depth
    q = Queue()
    q.enqueue((node, depth))
    c = 0
    while not q.isEmpty():
        node, depth = q.dequeue()
        if (node.left and not node.right) or (not node.left and node.right):
            c += 1
        if node.left:
            q.enqueue((node.left, depth+1))
        if node.right:
            q.enqueue((node.right, depth+1))
    return c

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
    print(half_nodes(tree))


