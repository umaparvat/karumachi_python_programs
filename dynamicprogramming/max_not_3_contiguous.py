"""
not select 3 contiguous element
M(i) = { 0 if i=0
        arr[0] if i =1
        max(arr[0], arr[1]) if i = 2
        max(arr[0]+M(2), arr[0]+M(3), arr[0]+M(1)+M(3)) if i >= 3
        or
        max(arr[i]+arr(i-1)+M(i-3), arr[i]+M(i-2), M(i-1) )if i>=3
"""

def recursive(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n==2:
        return max(arr[0], arr[1])
    return max(arr[n]+arr[n-1]+recursive(arr, n-3), arr[n]+recursive(arr,n-2), recursive(arr, n-1))


def top_down(arr, n, mem):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    if mem.get(n) is not None:
        return mem.get(n)
    mem[n] = max(arr[n]+arr[n-1]+top_down(arr, n-3, mem),
                 arr[n]+top_down(arr, n-2, mem),
                 top_down(arr, n-1, mem))
    return mem[n]

def bottom_up(arr, n):
    output = [0]*(n+1)
    output[0] = 0
    output[1] = arr[0]
    output[2] = max(arr[0], arr[1])
    for i in range(3, n+1):
        output[i] = max(arr[i]+arr[i-1]+output[i-3],
                        arr[i]+output[i-2], output[i-1])
    return output[-1]

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    print(recursive(arr, 5))
    print(top_down(arr, 5, {0:0, 1:arr[0], 2:max(arr[0], arr[1])}))
    print(bottom_up(arr, 5))
