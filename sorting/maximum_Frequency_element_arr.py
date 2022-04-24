


def norml_check(arr):
    """
    O(n2)
    :param arr:
    :return:
    """
    maxi = float("-inf")
    canditate = None
    for i in range(len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > maxi:
            maxi = count
            candidate = i
    return maxi, candidate


def check_frequency(arr):
    """
    O(nlogn)
    while loop -> O(n) which is neligble because sort is higher.
    time complexity: O(nlogn)
    space => O(1)
    :param arr:
    :return:
    """
    arr.sort()
    i = 0
    j = 0
    count = 0
    maxi = 0
    candidate = None
    while j < len(arr):
        if arr[i] == arr[j]:
            count += 1
        else:
            count = 0
            i = j
        if count > maxi:
            maxi = count
            candidate = i
        j += 1
    return maxi, candidate

def counting(arr):
    """
    time compleixty: O(n)
    since input arr is small and votes are less.
    we can use count sort.
    space -> max(arr) -> k we can assume. Max value in the arr
    :param arr:
    :return:
    """
    maxi = max(arr)
    n = len(arr)
    counter = [0] * (maxi+1)
    for i in range(n):
        counter[arr[i]] += 1
    for i in range(1, maxi+1):
        counter[i] += counter[i-1]
    temp = [0]* len(arr)
    for i in range(n-1, -1, -1):
        counter[arr[i]] -= 1
        temp[counter[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = temp[i]

    i = 0
    j = 0
    count = 0
    maxi = 0
    print(arr)
    candidate = None
    while j < len(arr):
        if arr[i] == arr[j]:
            count += 1
        else:
            count = 0
            i = j
        if count > maxi:
            maxi = count
            candidate = i
        j += 1
    return maxi, candidate
if __name__ == "__main__":
    a = [3,2,1,2,2,3]
    print(check_frequency(a))
    print(norml_check(a))
    print(counting(a))