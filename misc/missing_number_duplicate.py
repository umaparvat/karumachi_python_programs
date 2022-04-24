def findTwoElement(arr, n):
    # code here
    i = 0
    while i < n:
        if arr[i] != arr[arr[i]-1]:
                swap(arr[i], arr[arr[i]-1])
        else:
            i += 1
    miss = 0
    dup = 0
    print(arr)
    for i in range(n):
        if arr[i] != i + 1:
            miss = i + 1
            dup = arr[i]
            return [dup, miss]


def swap(start, end):
    start , end = end, start

if __name__ == "__main__":
    arr = [13,33,43,16,25,19,23,31,29,35,10,2,32,11,47,15,34,46,30,26,41,18,5,17,37,39,6,4,20,27,9,3,8,40,24,44,14,36,7,38,12,1,42,12,28,22,45]
    n = 47
    print(findTwoElement(arr, n))