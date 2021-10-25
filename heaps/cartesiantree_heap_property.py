
def findmin(arr, start, end):
    min = arr[start]
    index = start
    for i in range(start+1, end+1):
        if arr[i] < min:
            min = arr[i]
            index = i
    return index


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def cartesiantree(arr, start, end):
    """
    O(n^2) time complexity
    :param arr:
    :param start:
    :param end:
    :return:
    """
    if start > end:
        return
    min_index = findmin(arr, start, end)
    root = Node(arr[min_index])
    root.left = cartesiantree(arr, start, min_index-1)
    root.right = cartesiantree(arr, min_index+1, end)
    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.value, end=" ")
        inorderTraversal(root.right)

if __name__ == "__main__":
    inorder = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]
    root = cartesiantree(inorder, 0, len(inorder)-1)
    inorderTraversal(root)
