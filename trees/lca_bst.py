

class Node:
        def __init__(self, data, left=None, right=None):
            self.val = data
            self.left = left
            self.right = right

        def __str__(self):
            return f"Node(val={self.val}, left={self.left}, right={self.right})"

def construct_bst():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(8)
    root.right.right = Node(10)
    root.right.left = Node(5)
    root.right.left.right = Node(7)
    root.right.left.right.left = Node(6)
    return root


def lca_of_bst(node, alpha, beta):
    if not node:
        return
    if (alpha <= node.val and beta >= node.val) or (alpha >= node.val and beta <= node.val):
        return node
    if alpha < node.val:
        return lca_of_bst(node.left, alpha, beta)
    else:
        return lca_of_bst(node.right, alpha, beta)

def lca_of_bst_iterative(node, alpha, beta):
    while node:
        if (alpha <= node.val and beta >= node.val) or (alpha >= node.val and beta <= node.val):
            return node
        if alpha < node.val:
            node = node.left
        else:
            node = node.right


if __name__ == "__main__":
    tree = construct_bst()
    print(lca_of_bst(tree, 6, 7))
    print(lca_of_bst_iterative(tree, 6, 7))


