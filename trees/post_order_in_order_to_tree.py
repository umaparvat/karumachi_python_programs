class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left}, right={self.right}"


def construct_tree(ind, arr, postorder):
    if not arr:
        return None, ind
    print(postorder[ind], arr)
    if len(arr) == 1 and postorder[ind] == arr[0]:
        print("matched", arr[0], ind-1, ind-2)
        return Node(arr[0]), ind-1
    item = postorder[ind]
    inorder_ind = arr.index(item)
    left = arr[0:inorder_ind:]
    right = arr[inorder_ind+1:len(arr)]
    print("itn", item, left, right)
    node = Node(item)
    node.right, other_ind = construct_tree(ind-1, right, postorder)
    print("other", other_ind, left)
    node.left, new_ind = construct_tree(other_ind, left, postorder)
    return node, new_ind


if __name__ == "__main__":
    inorder = ['D', 'B', 'E', 'A', 'F', 'C']
    postorder = ['D', 'E', 'B', 'F', 'C', 'A']
    root, indx = construct_tree(len(postorder)-1, inorder, postorder)
    print(root)
    inorder1 =  [12, 8, 4, 9, 3, 10, 7, 11]
    postorder1 = [12, 8, 9, 4, 10, 11, 7, 3]
    root1, idx = construct_tree(len(postorder1)-1, inorder1, postorder1)
    print(root1)