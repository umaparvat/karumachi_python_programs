import os
import sys
sys.path.append(os.getcwd())

def is_same(node1, node2):
    if not node1 and not node2:
        return True
    if node1.val == node2.val and not node1.left and not node2.left and node2.right and node1.right:
        return True
    if node1.val != node2.val or (node1.left and not node2.left) or (not node1.left and node2.left) or (node2.right and not node1.right) or (not node2.right and node1.right):
        return False
    left = is_same(node1.left, node2.left) if node1.left and node2.left else True
    right = is_same(node1.right, node2.right) if node1.right and node2.right else True
    return left and right


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
    root1.left = Node(4, left=Node(8, left=Node(12)), right=Node(9))
    root1.right = Node(7, left=Node(10), right=Node(11))
    return root, root1

if __name__ == "__main__":
    tree1, tree2 = construct_tree()
    print(is_same(tree1, tree2))