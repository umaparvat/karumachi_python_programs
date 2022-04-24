

def radix_sort(arr):
    """
    time complexity: O(n+k)
    space : O(maximum element)
    count sort is applicable till 1...n or 2n.. or 3n.

    we the range is n^2, n^3... and solve the problem in linear
    we need to use radix sort.
    if it's n^2 range , radix sort will solve in 2(n) times
    :param arr:
    :return:
    """
    maximum = max(arr)
    pos = 1
    while (maximum / pos) > 0:
        count_sort(arr, pos)
        pos *=10
    return arr

def count_sort(arr, pos):
    n = len(arr)
    count = [0]*10
    for val in arr:
        index = (val//pos)%10
        count[index] += 1
    for i in range(1, 10):
        count[i]+=count[i-1]
    temp = [0]*10
    for i in range(n-1, -1, -1):
        val = arr[i]
        index = (val//pos)%10
        count[index] -= 1
        temp[count[index]] = val

    for i in range(n):
        arr[i] = temp[i]


if __name__ == "__main__":
    arr = [121, 432, 564, 23, 1, 45, 788]
    print("before:", arr)
    print("after:", radix_sort(arr))
