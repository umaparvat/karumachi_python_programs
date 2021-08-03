import pytest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left}, right={self.right}"


def construct_tree_iterative(str):
    """
    Time complexity: O(n)
    space complexity: O(1)
    :param str:
    :return:
    """
    if not str:
        return
    root = parent= Node(str[0])
    i = 1
    while i < len(str):
        n = Node(str[i])
        if not parent.left:
            parent.left = n
        if not parent.right:
            parent.right = n
        if str[i] == 'I':
            parent = n
        i += 1
    return root


def construct_tree_recur(i, str):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    :param i:
    :param str:
    :return:
    """
    if i == len(str) or not str:
        return None, i
    if str[i] == 'L':
        return Node(str[i]), i+1
    n = Node(str[i])
    n.left, new_ind = construct_tree_recur(i+1, str)
    n.right, new_ind = construct_tree_recur(new_ind, str)
    return n, new_ind



if __name__ == "__main__":
    print(construct_tree_iterative("IILILLILL"))
    print(construct_tree_recur(0,"IILILLILL")[0])




