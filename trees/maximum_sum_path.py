import os
import sys
sys.path.append(os.getcwd())

def max_path(nleft, nright, lpath, rpath):
    if nleft > nright:
        return nleft, lpath
    else:
        return nright, rpath


def find_max_sum_path(node, mSum, mPath):
    if not node:
        return 0, []
    if not node.left:
        node.lPath =[]
        node.sLeft = 0
    if not node.right:
        node.rPath = []
        node.sRight = 0
    if node.left:
        find_max_sum_path(node.left, mSum, mPath)
    if node.right:
        find_max_sum_path(node.right, mSum, mPath)
    if node.left:
        node.sLeft, node.lPath = max_path(nleft=node.left.sLeft, nright=node.left.sRight,
                                          lpath=node.left.lPath, rpath=node.left.rPath)
        node.sLeft += node.left.val
    if node.right:
        node.sRight, node.rPath = max_path(nleft=node.right.sLeft, nright=node.right.sRight,
                                          lpath=node.right.lPath, rpath=node.right.rPath)
        node.sRight += node.right.val
    if max(node.sLeft+node.val, node.sRight+node.val) > mSum:
        mSum, mPath = max_path(nleft=node.sLeft+node.val, nright=node.sRight+node.val,
                                          lpath=node.lPath, rpath=node.rPath)
        mPath.insert(0, node.val)
    return mSum, mPath



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
    print(find_max_sum_path(tree1, 0,[]))