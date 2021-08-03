import os
import sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def sum_all_elements_recursive(node):
    if not node:
        return 0
    left = sum_all_elements_recursive(node.left)
    right = sum_all_elements_recursive(node.right)
    return node.val + left+right

def sum_all_elements(node):
    queue = Queue()
    if not node:
        return 0
    queue.enqueue(node)
    sum = 0
    while not queue.isEmpty():
        node = queue.dequeue()
        sum += node.val
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return sum


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
    root1 = Node(3)
    root1.left = Node(4, left=Node(8, left=Node(120)), right=Node(9))
    root1.right = Node(7, left=Node(10), right=Node(11))
    return root, root1

if __name__ == "__main__":
    tree1, tree2 = construct_tree()
    print(sum_all_elements_recursive(tree1), sum_all_elements(tree1))
