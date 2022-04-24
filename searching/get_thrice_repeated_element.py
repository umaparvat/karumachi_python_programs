

def get_repeated_twice_element_in_thrice(arr):
    """
    time complexity: O(n)
    space complexity: O(1)
    :param arr:
    :return:
    """
    n = len(arr)
    m = max(arr)
    xr = 0
    for i in range(1, m+1):
        xr^=i
    for i in range(n):
        xr^=arr[i]
    return xr

if __name__ == "__main__":
    print(get_repeated_twice_element_in_thrice([4,4,4,5,5,5,5]))