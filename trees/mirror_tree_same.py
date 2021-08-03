import copy

def mirroring_tree(node):
    if node:
        left = mirroring_tree(node.left)
        right = mirroring_tree(node.right)
        node.left, node.right = right, left
    return node

def is_same_mirror(node1, node2):
    if not node1 and not node2:
        return True
    print(node1)
    print(node2)
    if (node1 and not node2) or (node2 and not node1):
        print("from here")
        return False
    if node1.val != node2.val:
        print("not same")
        return False
    left = is_same_mirror(node1.left, node2.right)
    right = is_same_mirror(node1.right, node2.left)
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
    root1.left = Node(7, left=Node(11), right=Node(10))
    root1.right = Node(4, left=Node(9), right=Node(8, right=Node(12)))
    return root, root1



if __name__ == "__main__":
    tree1, tree2 = construct_tree()
    print(is_same_mirror(tree1, tree2))
    mirror_tree = mirroring_tree(copy.deepcopy(tree1))
    print(is_same_mirror(tree1, mirror_tree))
