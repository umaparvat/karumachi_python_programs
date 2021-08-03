import os
import sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def insert_element(node, key):
    queue = Queue()
    queue.enqueue(node)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n.val == key:
           return n
        if not n.left:
            n.left = Node(key)
            return n
        else:
            queue.enqueue(n.left)
        if not n.right:
            n.right = Node(key)
            return n
        else:
            queue.enqueue(n.right)

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
    print(insert_element(tree, key=14))
