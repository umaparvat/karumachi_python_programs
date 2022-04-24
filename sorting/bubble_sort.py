

def bubble_sort(arr):
    """
    Best case: O(n)
    worst case: O(n2)
    space complexity: O(1)
    :param arr:
    :return:
    """
    n = len(arr)
    swapped = 1
    for i in range(n):
        if swapped == 0:
            break
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
                swapped = 1
    return arr

def swap(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]


if __name__ == "__main__":
    arr = bubble_sort([127,220,246,277, 321, 454, 534, 565, 933])
    print(arr)

    a = [534,246,933, 127, 277, 321, 454, 565, 220]
    print("before", a)
    a = bubble_sort(a)
    print("after", a)