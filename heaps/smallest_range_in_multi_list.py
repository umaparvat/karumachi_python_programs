import heapq
from heapq import heappop, heappush

class Node:
    def __init__(self, value, list_num, index):
        self.value = value
        self.list_num = list_num
        self.index = index

    def __lt__(self, other):
        return self.value < other.value


def find_range(arr):
    """
    O(nlogM) -> log M insertion/deletion.
    N items
    :param arr:
    :return:
    """
    range_val = (0, float("inf"))
    high = float("-inf")
    pq = []
    for index in range(len(lis)):
        heappush(pq, Node(lis[index][0], index, 0))
        high = max(high, lis[index][0])
    while True:
        min = heappop(pq)
        if high - min.value < range_val[1]-range_val[0]:
            range_val = (min.value, high)
        if min.index+1 < len(lis[min.list_num]):
            min.index += 1
            min.value = lis[min.list_num][min.index]
        else:
            return range_val
        heappush(pq, min)
        high = max(high, min.value)




if __name__ == "__main__":
    lis = [[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]]
    print(find_range(lis))