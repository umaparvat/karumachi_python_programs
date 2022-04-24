

def selection_sort(arr):
    """
    time complexity: O(n2)
    space complexity: O(1)
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        least = i
        for j in range(i+1, n):
            if arr[j] < arr[least]:
                least = j
        swap(arr, i, least)
    return arr

def swap(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]


if __name__ == "__main__":
    arr = [54,26,93,17,77,31, 44, 55, 20]
    print("before", arr)
    arr = selection_sort(arr)
    print("after sort:", arr)