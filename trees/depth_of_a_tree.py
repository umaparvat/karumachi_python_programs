import os
import sys
sys.path.append(os.getcwd())

def depth_of_a_tree(node):
    if node:
        return max(depth_of_a_tree(node.left), depth_of_a_tree(node.right))+1
    return 0

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
    print(depth_of_a_tree(tree))