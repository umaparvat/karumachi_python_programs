import pytest

class DLLNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    def __str__(self):
        return f"Node(data={self.data}, prev={self.prev}, next={self.next}"

class Node:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node(val={self.val}, left={self.left}, right={self.right})"

def converttodll(node):
    if not node:
        return None
    DNode = DLLNode(node.val)
    DNode.prev = DNode
    DNode.next = DNode
    tmp = converttodll(node.left)
    if tmp:
        last_node = tmp.prev
        node_last = DNode.prev
        last_node.next = DNode
        DNode.prev = last_node
        tmp.prev = node_last
        node_last.next = tmp
        DNode = tmp
    tmp1 = converttodll(node.right)
    if tmp1:
        last_node = tmp1.prev
        node_last = DNode.prev
        DNode.prev = last_node
        node_last.next = tmp1
        tmp1.prev = node_last
        last_node.next = DNode
    return DNode


def construct_tree():
    root = Node(3)
    root.left = Node(4, left=Node(8, left=Node(12)), right=Node(9))
    root.right = Node(7, left=Node(10), right=Node(11))
    root1 = Node(3)
    root1.left = Node(4, left=Node(8, left=Node(120)), right=Node(9))
    root1.right = Node(7, left=Node(10), right=Node(11))
    return root, root1

@pytest.mark.unit_test
class TestallCases:
    def test_no_node(self):
        assert converttodll(None) is None

    def test_one_node(self):
        data = converttodll(Node(9))
        assert data.next == data and data.prev == data

    def test_minimum_tree(self):
        tree = Node(9)
        tree.left = Node(8)
        tree.right = Node(10)
        head = converttodll(tree)
        assert head.data == 8 and head.prev.data == 10 and head.next.data == 9



if __name__ == "__main__":
    tree1, tree2 = construct_tree()
    head = converttodll(tree1)
    current = head.next
    print(f"{head.data}", end="=>")
    while current != head:
        print(f"{current.data}", end="=>")
        current = current.next
    print(f"{current.data}", end="")