import heapq
from heapq import heappush, heappop

def sort_k_sorted_array(arr, k):
    """
    O(nlogk)
    heap is k size at any time -> space O(k)
    each insert O log k and for n items --> O(nlogk)
    :param arr:
    :param k:
    :return:
    """
    priority_queue = arr[:k+1]
    heapq.heapify(priority_queue)
    index = 0
    for i in range(k+1, len(arr)):
        arr[index] = heappop(priority_queue)
        heappush(priority_queue, arr[i])
        index += 1

    while priority_queue:
        arr[index] = heappop(priority_queue)
        index += 1


if __name__ == "__main__":
    lis = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    sort_k_sorted_array(lis,k)
    print(lis)