
def check_dublicates(arr):
    """
    sorting -> O(nlogn)
    o(n) for loop -> time complexity total => O(nlogn)
    space -> O(1)
    :param arr:
    :return:
    """
    arr.sort()
    for ind in range(1, len(arr)):
        if arr[ind] == arr[ind-1]:
            return True
    return False