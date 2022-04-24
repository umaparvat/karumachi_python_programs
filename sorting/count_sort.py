

def count_sort(arr):
    """
    time complexity: O(n+k)
    it's works with positive number
    to work with negative number,
    normalize it by adding a postive of that negative value into all elements in the array.
     The range has to be 0< k< max(arr). note the max value should be O(n) not O(n**n)
     if k is constant, then time complexity is O(n)
    :param arr:
    :return:
    """
    n = len(arr)
    maximum = max(arr)
    count = [0]*(maximum+1)
    for ind in range(n):
        count[arr[ind]] += 1
    for ind in range(1, maximum+1):
        count[ind] += count[ind-1]
    temp = [0]*n
    for ind in range(n-1, -1, -1):
        count[arr[ind]] -= 1
        temp[count[arr[ind]]] = arr[ind]
    for ind in range(n):
        arr[ind] = temp[ind]


if __name__ == "__main__":
    arr = [1, 4, 1, 2, 7, 5, 2]
    print("before sort:", arr)
    count_sort(arr)
    print("after sort:", arr)
    a = [3,2,1,2,2,3]
    print("before", a)
    count_sort(a)
    print("after", a)