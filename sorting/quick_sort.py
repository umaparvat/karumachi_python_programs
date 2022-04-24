



def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub
    while start < end:
        while arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[lb], arr[end] = arr[end], arr[lb]
    return end

def quick_sort(arr, lb, ub):
    """
    time complexity: O(n**2) -> worst case
    best case -> O(nlogn)

    :param arr:
    :param lb:
    :param ub:
    :return:
    """
    if lb < ub:
        loc = partition(arr, lb, ub)
        quick_sort(arr,lb, loc-1)
        quick_sort(arr, loc+1, ub)




if __name__ == "__main__":
    arr = [6,8,1,4,5,3,7,2]
    print("before", arr)
    quick_sort(arr, 0, len(arr)-1)
    print("after", arr)


