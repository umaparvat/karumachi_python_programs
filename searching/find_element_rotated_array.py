

def get_index(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)>>1
        #print(arr[mid])
        if arr[mid] == target:
            return mid
        elif arr[mid] >= arr[low]:
            if arr[low] <= target < arr[mid]:
                high = mid -1
            else:
                low = mid+1
        else:
            if arr[mid] <= target < arr[high]:
                low  = mid +1
            else:
                high = mid - 1

    return -1




if __name__ == "__main__":
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    k = get_index(arr, 16)
    print(arr)
    print(k, arr[k])