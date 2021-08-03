import pytest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left.val if self.left else ''}, right={self.right.val if self.right else ''}"

def construct_tree():
    a = Node(2, left=Node(4), right=Node(5))
    b = Node(3, left=Node(6), right=Node(7))
    root = Node(1, left=a, right=b)
    return root


def print_ancestors(node, key, path):
    if node:
        if node.val == key or print_ancestors(node.left, key, path) or print_ancestors(node.right, key, path):
            path.insert(0,node.val)
            return path
    return

@pytest.mark.unit_test
def test_ancestor():
    tree = construct_tree()
    result = print_ancestors(tree, 7, [])
    print(result)
    assert result == [1, 3, 7]


if __name__ == "__main__":
    test_ancestor()