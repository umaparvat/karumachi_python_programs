import os
import sys
sys.path.append(os.getcwd())

def root_leaf_path(node, prev_path):
    if node:
        prev_path += f"{node.val}->"
        if not node.left and not node.right:
            print(prev_path+"NULL")
            return
        root_leaf_path(node.left, prev_path)
        root_leaf_path(node.right, prev_path)


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
    print("tree1 path:")
    root_leaf_path(tree1, "")