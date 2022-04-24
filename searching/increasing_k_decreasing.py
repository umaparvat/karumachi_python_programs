

def find_k(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + ((high-low)//2)
        if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
            return mid
        elif arr[mid-1] > arr[mid] and arr[mid] < arr[mid+1]:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":

    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print(arr)
    k = find_k(arr)
    print(k, arr[k])
