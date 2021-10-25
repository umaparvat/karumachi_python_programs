import heapq
from heapq import heappush, heappop


class Node:
    def __init__(self, value, list_num, index):
        self.value = value
        self.list_num = list_num
        self.index = index

    def __lt__(self, other):
        return self.value < other.value

def printSorted(arr):
    """
    O(m*n*logm) total element m*n
    space -> O(m) for heap space
    :param arr:
    :return:
    """
    pq = []
    for index in range(len(arr)):
        heappush(pq, Node(arr[index][0], index, 0))
    while pq:
        min = heappop(pq)
        print(min.value, end=" ")
        if min.index+1 < len(arr[min.list_num]):
            min.index += 1
            min.value = arr[min.list_num][min.index]
            heappush(pq, min)



if __name__ == '__main__':
    lists = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
        [16, 18, 22, 28]
    ]

    printSorted(lists)