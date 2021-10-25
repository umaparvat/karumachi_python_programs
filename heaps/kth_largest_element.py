from heapq import heappush, heappop, heapreplace

class MaxHeap:
    def __init__(self, arr=None):
        self.heap = arr if arr else []
        self.size = len(arr) if arr else 0
        self.build()

    def build(self):
        if not self.heap:
            return
        parent = (len(self.heap)-1)//2+1
        for index in range(parent, -1, -1):
            self.heapify(index)

    def insert(self, value):
        self.size += 1
        if not self.heap:
            self.heap.append(value)
        else:
            self.heap.append(value)
            for index in range((self.size-1)//2+1, -1, -1):
                self.heapify(index)

    def searchelement(self, item):
        if not self.heap:
            return
        index = 0
        while index < self.size:
            if item == self.heap[index]:
                return index
            index += 1

    def parent(self, index):
        return (index-1)//2

    def left(self, index):
        return 2*index+1

    def right(self, index):
        return 2*index+2

    def rightchild(self, index):
        if index < self.size and 2*index+2 < self.size:
            return self.heap[2*index+2]
        return float("-inf")

    def leftchild(self, index):
        if index < self.size and 2*index+1 <self.size:
            return self.heap[2*index+1]
        return float("-inf")


    def heapify(self, index):
        if index < self.size:
            largest = index
            left = self.left(index)
            right = self.right(index)
            if left < self.size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < self.size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.swap(index, largest)
                self.heapify(largest)

    def swap(self, start, end):
        self.heap[start], self.heap[end] = self.heap[end], self.heap[start]

    def top(self):
        return self.heap[0] if self.heap else float("-inf")

    def removetop(self):
        if self.size == 1:
            self.size -= 1
            return self.heap.pop(0)
        elif self.size > 1:
            self.swap(0, self.size-1)
            self.size -= 1
            self.heapify(0)
            return self.heap.pop()


def kthelement(arr, k):
    """
    construct max heap for the array in O(n)
    pop k times the heap root -> klogn
    space: O(n) -> heap space
    O(n+klogn)
    :param arr:
    :param k:
    :return:
    """
    if k > len(arr):
        return  0
    m = MaxHeap(arr)
    kelement = float("-inf")
    for i in range(k):
        kelement = m.removetop()
        print(kelement)
    return kelement


def kthelement_without_delete(s, k):
    """
    construct O(n) max heap.
    construct aux heap and insert k times values from max heap->klogk
    o(n+klogk)
    space-> O(n+k)
    :param s:
    :param k:
    :return:
    """
    if k > len(s):
        return 0
    m = MaxHeap(arr=s)
    aux = MaxHeap()
    aux.insert((m.top(), 0))
    c = 1
    if c == k:
        return aux.top()
    c = 0
    itm = None
    while c != k:
        itm, index = aux.removetop()
        c += 1
        if c == k:
            return itm
        if m.right(index) < m.size:
            aux.insert((m.rightchild(index), 2*index+2))
        if m.left(index) < m.size:
            aux.insert((m.leftchild(index), 2*index+1))


def kthelement_k_heap(s, k):
    """
    construct min heap of k items first
    iterate from k to n items and compare with root.
    if value is greater than root, replace it.
    so the end of iteration, heap will have k largest items.
    O(nlogk) -> log k insertion/deletion
    n items iteration
    space -> O(k)
    :param s:
    :param k:
    :return:
    """
    pq = []
    for index in range(k):
        heappush(pq, s[index])
    for index in range(k,len(s)):
        if s[index] > pq[0]:
            heapreplace(pq, s[index])
    return heappop(pq)

if __name__ == "__main__":
    # arr = [7, 4, 6, 3, 9, 1]
    # k = 6
    # print(kthelement(arr, k))
    s =[7, 4, 6, 3, 9, 1]
    print(kthelement_without_delete(s, 6))
    s1 = [7, 4, 6, 3, 9, 1]
    print(kthelement_k_heap(s1, 6))