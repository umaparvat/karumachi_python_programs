class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left}, right={self.right}"


def construct_tree(ind, arr, preorder):
    if ind == len(preorder):
        return None, ind+1
    if not arr:
        return None, ind
    if len(arr) == 1 and preorder[ind] == arr[0]:
        return Node(arr[0]), ind+1
    inorder_ind = arr.index(preorder[ind])
    left = arr[0:inorder_ind:]
    right = arr[inorder_ind+1:len(arr)]
    node = Node(preorder[ind])
    node.left, new_ind = construct_tree(ind+1, left, preorder)
    node.right, other_ind = construct_tree(new_ind, right, preorder)
    return node, other_ind


if __name__ == "__main__":
    inorder = ['D', 'B', 'E', 'A', 'F', 'C']
    preorder = ['A', 'B', 'D', 'E', 'C', 'F']
    root, indx = construct_tree(0, inorder, preorder)
    print(root)
    inorder1 =  [12, 8, 4, 9, 3, 10, 7, 11]
    preorder1 = [3, 4, 8, 12, 9, 7, 10, 11]
    root1, idx = construct_tree(0, inorder1, preorder1)
    print(root1)