from collections import defaultdict

def check_duplicate(arr):
    """
    O(n*n) -> time complexity
    space complexity: O(1)
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                print("duplicate", arr[i])
                return True
    return False

def hashing(arr):
    """
    time : O(n)
    space: O(n)
    :param arr:
    :return:
    """
    ds = defaultdict(int)
    for num in arr:
        if num in ds:
            print("duplicate", num)
            return True
        else:
            ds[num]+=1
    return False

def negation_technique(arr):
    """
    time : O(n)
    space: O(1)
    This will work only if the array can be modified
    all the numbers are positive
    and all the numbers are in the range [0, n-1]. If not, list index out of range error.
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        if arr[abs(arr[i])] < 0:
            print("duplicate", abs(arr[i]))
            return True
        else:
            arr[abs(arr[i])] = -arr[abs((arr[i]))]
    return False

if __name__ == "__main__":
    arr = [3,2,1,2,2,3]
    print(check_duplicate(arr))
    print(hashing(arr))
    print(negation_technique(arr))