import heapq
from heapq import heappush, heappop

def kthsmallest(arr, k):
    """
    :param arr:
    :param k:
    :return:
    """
    heapq.heapify(arr)
    x = heapq.nsmallest(k, arr)
    kth = None
    for i in x:
        kth = i
    print(kth)


if __name__ == "__main__":
    lis = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    kthsmallest(lis, k)