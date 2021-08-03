import os, sys
sys.path.append(os.getcwd())

def addnodes(node, num, sum):
    if not node:
        return sum
    if not node.left and not node.right:
        sum += num
    else:
        num = num * 10
        if node.left:
            sum = addnodes(node.left, num+node.left.val, sum)
        if node.right:
            sum = addnodes(node.right, num+node.right.val, sum)
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
    return root

if __name__ == "__main__":
    tree = construct_tree()
    sum = 0
    print(addnodes(tree, tree.val, sum))