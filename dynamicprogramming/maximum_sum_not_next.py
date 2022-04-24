"""
Find the maximum sum of contiguous sub sequence
but not two consecutive numbers

recursive:
    ABCDEF -> n is the size
    F is selected, E should not be selected and A-D can be considered
    F is not selected, E can be selected and D is nt included
    Max(i) = { 0 if i = 0
               arr[0] if i == 1
               max(arr[0], arr[1]) if i == 2
               max(arr[i]+Max([i-2]), Max(arr[i-1])  if i >= 3

"""

def recursive(arr, n):
    if n <= 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    return max(arr[n] + recursive(arr,n-2), recursive(arr, n-1))


def top_down(arr, n, mapdict):
    if n <= 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    if mapdict.get(n) is not None:
        return mapdict.get(n)
    mapdict[n] = max(arr[n]+recursive(arr, n-2), recursive(arr, n-1))
    return mapdict[n]

def bottom_up(arr, n):
    output = [0]* (n+1)
    output[0] = 0
    output[1] = arr[0]
    output[2] = max(arr[0], arr[1])
    for ind in range(3, n+1):
        output[ind] = max(arr[ind]+output[ind-2], output[ind-1])
    return output[-1]

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    print(recursive(arr, len(arr)-1))
    print(top_down(arr, len(arr)-1, {0:0, 1:arr[0], 2: max(arr[0], arr[1])}))
    print(bottom_up(arr, len(arr)-1))