

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.nextsibling = None
    def __str__(self):
        return f"Node: {self.val}, left={self.left}, " \
               f"right={self.right}, nextsibling={self.nextsibling}"

def construct_tree():
    root = Node(3)
    root.left = Node(4, left=Node(8, left=Node(12)), right=Node(9))
    root.right = Node(7, left=Node(10), right=Node(11))
    root1 = Node(3)
    root1.left = Node(4, left=Node(8, left=Node(120)), right=Node(9))
    root1.right = Node(7, left=Node(10), right=Node(11))
    return root, root1

def next_sibling(node):
    """
    Time complexity: O(n)
    space complexity: O(n) recursive stack
    :param node:
    :return:
    """
    if node:
        if node.left:
            node.left.nextsibling = node.right
        if node.right:
            if node.nextsibling:
                node.right.nextsibling = node.nextsibling.left
            else:
                node.right.nextsibling = None
        next_sibling(node.left)
        next_sibling(node.right)
    return

def next_sibling_without_Extra_space(node):
    """
    Time complexity: O(n),
    space complexity: O(1)
    if the node's right is empty, left will point to the null,
    instead of pointing to the nearest right child
    :param node:
    :return:
    """
    current = None
    while node:
        if node.left:
            node.left.nextsibling = node.right
        if node.right:
            if node.nextsibling:
                node.right.nextsibling = node.nextsibling.left
                current = node
            else:
                node.right.nextsibling = None
                if not current:
                    node = node.left
                    continue
                else:
                    node = current.left
                    current = None
                    continue
        node = node.nextsibling


if __name__ == "__main__":
    tree1, tree2 = construct_tree()
    next_sibling(tree1)
    print(tree1)
    next_sibling_without_Extra_space(tree2)
    print(tree2)