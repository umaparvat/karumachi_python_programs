

def insertion_sort(arr):
    """
    best case: omega(n)
    avg case: theta(n2)
    worst case: O(n2)
    space = o(1)
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        k = i
        while k > 0 and temp < arr[k-1]:
            arr[k] = arr[k-1]
            k -= 1
        arr[k] = temp
    return arr

if __name__ == "__main__":
    arr = [6,8,1,4,5,3,7,2]
    print("before", arr)
    arr = insertion_sort(arr)
    print("after", arr)
