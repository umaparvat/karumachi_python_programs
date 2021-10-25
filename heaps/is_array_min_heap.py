

def recursive_solution(arr, index):
    """
    o(n) time complexity:
    space O(n) -> for internal stack
    :param arr:
    :param index:
    :return:
    """
    if (2*index)+2 > len(arr):
        # leaf node are always heap
        return True
    if (2*index)+1 < len(arr) and arr[index] > arr[(2*index)+1]:
        return True
    if (2*index)+2 < len(arr) and arr[index] > arr[(2*index)+2]:
        return True
    left = recursive_solution(arr, (2*index)+1)
    right = recursive_solution(arr, (2*index)+2)
    return left and right


def iterative_solution(arr):
    """
    o(n) time complexity.
    o(1) space 
    :param arr:
    :return:
    """
    non_leaf_node = (len(arr)-1)//2 +1
    for index in range(0, non_leaf_node):
        if ((2*index)+1 < len(arr) and arr[index] > arr[(2*index)+1]) or ((2*index)+2 < len(arr) and arr[index] > arr[(2*index)+2]):
            return False
    return True


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    print(recursive_solution(A, 0))
    print(iterative_solution(A))
