
def merge_sort(arr):
    """
    time complexity: O(n log n)
    :param arr:
    :return:
    """
    if len(arr) > 1:
        n = len(arr)//2
        left = arr[:n]
        right = arr[n:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1

if __name__ == "__main__":
    arr = [6,8,1,4,5,3,7,2,3]
    print("before", arr)
    merge_sort(arr)
    print("after", arr)
