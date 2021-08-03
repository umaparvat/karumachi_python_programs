

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

def sum_vertically(node, column, hash_dict):
    if node:
        if column in hash_dict:
            hash_dict[column] += node.val
        else:
            hash_dict[column] = node.val
        sum_vertically(node.left, column-1, hash_dict)
        sum_vertically(node.right, column+1, hash_dict)
        return hash_dict
    return

if __name__ == "__main__":
    tree1, tree2 = construct_tree()
    val_dict = {}
    val_dict = sum_vertically(tree1, 0, {})
    print(val_dict)
    print(val_dict.values())