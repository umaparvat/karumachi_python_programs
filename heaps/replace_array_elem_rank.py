from heapq import heappop, heapify, heappush

class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value < other.value


def transform(arr):
    """
    auxilary space -> O(n) for dictionary
    time complexity-> O(nlogn) -> sorting the keys

    :param arr:
    :return:
    """
    map = dict()
    for index, value in enumerate(arr):
        map[value] = index

    rank = 1
    for key in sorted(map.keys()):
        arr[map.get(key)] = rank
        rank += 1

def minheaparr(arr):
    """
    aux space -> O(n)
    time comeplxity -> O(n log n)
    :param arr:
    :return:
    """
    pq = []
    for index, value in enumerate(arr):
        heappush(pq, Node(value, index))
    rank = 1
    while pq:
        node = heappop(pq)
        arr[node.index] = rank
        rank += 1

def maxheaparr(arr):
    """
    aux space: O(n)
    time complexity -> O(nlogn)
    :param arr:
    :return:
    """

    pq = []
    for index, value in enumerate(arr):
        heappush(pq, Node(-value, index))
    rank = len(arr)
    while pq:
        node = heappop(pq)
        arr[node.index] = rank
        rank -= 1


if __name__ == "__main__":
    A = [10, 8, 15, 12, 6, 20, 1]
    print(A)
    transform(A)
    print(A)
    B = [10, 8, 15, 12, 6, 20, 1]
    print(B)
    maxheaparr(B)
    print(B)
    C = [10, 8, 15, 12, 6, 20, 1]
    print(C)
    minheaparr(C)
    print(C)



