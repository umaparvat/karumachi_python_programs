class Minheap:
    def __init__(self, arr):
        self.size = len(arr)
        self.heap = arr
        self.build_heap()

    def build_heap(self):
        """
        iterate from middle to 0
        and build max heap
        :return:
        """
        number = (self.size - 1) // 2 + 1
        for index in range(number, -1, -1):
            self.min_heapify(index)

    def parent(self, index):
        return (index -1) // 2

    def left(self, index):
        return 2*index + 1

    def right(self, index):
        return 2*index + 2

    def min_heapify(self, k):
        """
        set k as smallest
        get K index left and right child index
        if both child is within the size limit
        compare smallest with left and set the smallest
        compare the smallest with right and set the smallest
        swap the smallest with k index
        o(log(n))

        :param k:
        :return:
        """
        smallest = k
        left = self.left(k)
        right = self.right(k)
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != k:
            self.swap(k, smallest)
            self.min_heapify(smallest)

    def swap(self, start, end):
        """
        swap start and end position.
        :param start:
        :param end:
        :return:
        """
        self.heap[start], self.heap[end] = self.heap[end], self.heap[start]

    def insert(self, value):
        """
        if heap is empty, insert a value at 0's index
        and increase the size.
        if heap has value, add the element at last and
        call maxheapify from it's parent till 0'th index.
        and increase size by 1
        o(logn)
        :param value:
        :return:
        """
        self.size += 1
        if not self.heap:
            self.heap.insert(0, value)
        else:
            parent = self.parent(self.size-1)
            self.heap.append(value)
            for i in range(parent, -1, -1):
                self.min_heapify(i)

    def remove(self, value):
        """
        O(n)
        :param value:
        :return:
        """
        if not self.heap:
            return -1
        index = -1
        try:
            index = self.heap.index(value) # o(n)
        except ValueError:
            return index
        if index == self.size-1:
            # last element, remove the element
            self.size -= 1
            return self.heap.pop()
        self.heap[index], self.heap[self.size-1] = self.heap[self.size-1], self.heap[index]
        self.size -= 1
        self.min_heapify(index)
        val = self.heap.pop()
        return val



    def get_min(self):
        """
        o(1)
        :return:
        """
        if self.size > 0:
            return self.heap[0]
        return -1

    def remove_min(self):
        """
        O(n)
        :return:
        """
        if self.size > 0:
            return self.remove(self.heap[0])
        return -1



if __name__ == "__main__":
    arr = [3,9,2,1,4,5]
    heaps = Minheap(arr)
    print(heaps.heap)
    print(heaps.remove_min())
    print(heaps.heap)
    heaps.insert(15)
    print(heaps.heap)
    print(heaps.remove(3))
    print(heaps.heap)

