"""
the problem from https://www.spoj.com/problems/KQUERY/
"""
num = int(input())
arr = list(map(int, input().split(" ")))
qur = int(input())
def mergesort(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i=j=0
    o = []
    while i<n and j < m:
        if arr1[i] < arr2[j]:
            o.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            o.append(arr2[j])
            j += 1
        else:
            o.append(arr1[i])
            o.append(arr2[j])
            i += 1
            j += 1
    while i < n:
        o.append(arr1[i])
        i += 1

    while j< m:
        o.append(arr2[j])
        j+= 1
    return o

def ceilbinary(arr, k):
    low = 0
    high = len(arr)-1
    if arr[high] <= k:
        return 0
    if low == high:
        if arr[low] < k:
            return 0
        return 1
    while low < high:
        mid = low + (high-low)//2
        if arr[mid] <= k:
                low = mid+1
        else:
            high = mid
    return high

tree = [0]*2 * num

def buildtree(index, arr, start, end):
    if start == end:
        tree[index] = [arr[start]]
    else:
        mid = start + (end-start)//2
        buildtree(2*index,arr, start, mid)
        buildtree(2*index+1, arr, mid+1, end)
        tree[index] = mergesort(tree[2*index], tree[2*index+1])

def querytree(index, arr, start, end, l, r, k):
    # print(index, arr, start, end, l, r, k)
    if r < start or l > end:
        return 0
    if l <= start and r >= end:
        high = len(tree[index])-1
        low = 0
        if tree[index][high] <= k:
            return 0
        if low == high:
            if tree[index][low] > k:
                return 1
            return 0
        while low < high:
            mid = low + (high-low)//2
            if tree[index][mid] <= k:
                low = mid+1
            else:
                high = mid
        return len(tree[index])-high
    mid = start+(end-start)//2
    p1 = querytree(2*index, arr, start, mid, l, r, k)
    p2 = querytree(2*index+1, arr, mid+1, end, l, r, k)
    return p1+p2


if __name__ == "__main__":
    buildtree(1, arr, 0, num-1)
    while qur:
        l,r, k = map(int, input().split(" "))
        print(querytree(1, arr, 0, num-1, l-1,r-1,k))
        qur -= 1


