import pytest
import os
import sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue


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

def add_node(node, lst, level):
    if level % 2 == 0:
        lst.append(node.val)
    else:
        lst.insert(0, node.val)
    return lst

def zigzag(node):
    """
    Time complexity: O(n)
    space complexity: queue->O(n), current_list -> O(n) => O(n)
    :param node:
    :return:
    """
    if not node:
        return
    que = Queue()
    level = prev_level = 0
    current_lst = []
    output = []
    que.enqueue((node, level))
    while not que.isEmpty():
        node, level = que.dequeue()
        if level == prev_level:
            current_lst = add_node(node, current_lst, level)
        else:
            output += current_lst
            current_lst = [node.val]
        if node.left:
            que.enqueue((node.left, level+1))
        if node.right:
            que.enqueue((node.right, level+1))
        prev_level = level
    if current_lst:
        output += current_lst
    return output


@pytest.mark.unit_test
class TestZigZag:

    def test_zigzag_no_node(self):
        assert zigzag(0) == None

    def test_zigzag_nodes(self):
        tree = construct_tree()
        assert zigzag(tree) == [1,3,2,4,5,6,7]


def main():
    tstcls = TestZigZag()
    tstcls.test_zigzag_no_node()
    tstcls.test_zigzag_nodes()


if __name__ == "__main__":
    main()

