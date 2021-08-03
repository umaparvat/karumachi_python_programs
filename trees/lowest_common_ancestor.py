import os
import sys
sys.path.append(os.getcwd())

def common_ancestor(node, key, path):
    if node:
        if node.val == key:
            path.append(node.val)
            return path, 1
        new_path, temp = common_ancestor(node.left, key, path+[node.val])
        if temp:
            return new_path, temp
        else:
            return common_ancestor(node.right, key, path+[node.val])
    return path, 0



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

def first_approach(node):
    """
    This approach traverse the tree 2 times in O(n).
    and gets the o(n) space array.
    and traverse array O(n)  1 time.

    Time complexity: O(n)
    space complexity: O(n)
    :param node:
    :return:
    """
    path1, found = common_ancestor(node, 4, [])
    path2, found2 = common_ancestor(node, 3,[])
    print(path1, path2)
    if found and found2:
        max_l = path1

        if len(path1) > len(path2):
            max_l = path1
            diff = len(path1)- len(path2)
        else:
            max_l = path2
            diff = len(path2) - len(path1)
        while diff and max_l:
            max_l.pop()
            diff -= 1
        print(path1, path2, len(max_l)-1)
        for i in range(len(max_l)-1, -1, -1):
            if path1[i] == path2[i]:
                print(path1[i])
                break
        else:
            print(0)
    else:
        print(0)

def both_value_exists(node, key1, key2):
    """
    Both key1 and key2 exists in the tree.
    time complexity: O(n)
    space complexity: O(n) ->recursive stack
    :param node:
    :param key1:
    :param key2:
    :return:
    """
    if node:
        if node.val == key1 or node.val == key2:
            return node
        left = both_value_exists(node.left, key1, key2)
        right = both_value_exists(node.right, key1, key2)
        if right and left:
            return node
        else:
            return left if left else right
    return

def check_common_node(node, key1, key2, v):
    if node:
        if node.val == key1:
            v[0] = node
            return node
        if node.val == key2:
            v[1] = node
            return node
        left = check_common_node(node.left, key1, key2, v)
        right = check_common_node(node.right, key1, key2,v)
        if left and right:
            return node
        else:
            return left if left else right

    return

def find_a_node_exists(node, key):
    if node:
        if node.val == key:
            return node
        temp = find_a_node_exists(node.left, key)
        if temp:
            return node
        else:
            return find_a_node_exists(node.right, key)
    return 0

def approach_three(node):
    """
    in this one, the values may or may not exists.
    rather than gathering the entire path. just two values in a array to check value exists or not.
    Time complexity: O(n)
    space complexity: O(n) - recursive stack
    :param node:
    :return:
    """
    val = [0,0]
    node = check_common_node(tree, 6, 7, val)
    if (val[0] and val[1]) or (val[0] and not val[1] and find_a_node_exists(node, 7)) or (not val[0] and val[1] and find_a_node_exists(node, 6)):
        print("found", node)
    else:
        print("NONE")
if __name__ == "__main__":
    tree = construct_tree()
    first_approach(tree)
    value = both_value_exists(tree, 6, 7)
    if value:
        print(value)
    else:
        print("NONE")
    approach_three(tree)



