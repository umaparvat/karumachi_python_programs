from heapq import heappop, heappush
import heapq

class Node:
    def __init__(self, value, list_num, list_index):
        self.value = value
        self.list_num = list_num
        self.list_index = list_index

    def __str__(self):
        return f"Node: value:{self.value}\n list_num:{self.list_num}\n list_index: {self.list_index}"

    def __lt__(self, other):
        return self.value < other.value


def merge_m_list(lists):
    """
    O(nlogm)
    log m insertion and deletion for each item
    total number of n => nlog(m)
    space complexity -> O(m) -> m numbers will be there at a time in heap.
    :param lists:
    :return:
    """
    pq = [Node(lists[each][0], each, 0) for each in range(len(lists)) if len(lists[each]) >= 1]
    heapq.heapify(pq)
    while pq:
        min = heappop(pq)
        print(min.value, end=" ")
        if min.list_index+1 < len(lists[min.list_num]):
            min.value = lists[min.list_num][min.list_index+1]
            min.list_index +=1
            heappush(pq, min)

if __name__ == "__main__":
    lists = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
    merge_m_list(lists)