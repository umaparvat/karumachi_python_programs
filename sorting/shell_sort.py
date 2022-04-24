


def shell_sort(arr):
    """
    best case: O(n)
    worst case: O(n log^2 n)
    :param arr:
    :return:
    """
    n = len(arr)
    gap = n//2
    while gap > 0:
        for j in range(gap, n):
            for i in range(j-gap, -1, -1):
                if arr[i+gap] > arr[i]:
                    break
                else:
                    swap(arr, i, i+gap)
        gap = gap//2
    return arr



def swap(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]


if __name__ == "__main__":
    arr = [6,8,1,4,5,3,7,2]
    print("before", arr)
    arr = shell_sort(arr)
    print("after", arr)
