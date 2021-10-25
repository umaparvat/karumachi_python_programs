"""
each element will have priority
use min stack to implement this
"""

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, value, priority):
        self.size += 1
        if not self.heap:
            self.heap.append((value, priority))
        else:
            self.heap.append((value, priority))
            self.siftup(self.size-1)

    def getSize(self):
        return self.size

    def getMin(self):
        return self.heap[0][0] if self.heap else None

    def parent(self, index):
        return (index-1)//2

    def left(self, index):
        return (2*index)+1

    def right(self, index):
        return (2*index)+2

    def siftup(self, index):
        if (index-1)//2 >= 0 and index > 0:
            parent = self.parent(index)
            left = self.left(parent)
            right = self.right(parent)
            smallest = parent
            if left < self.size and self.heap[left][1] < self.heap[smallest][1]:
                smallest = left
            if right < self.size and self.heap[right][1] < self.heap[smallest][1]:
                smallest = right
            if smallest != parent:
                self.swap(parent, smallest)
            self.siftup(parent)

    def swap(self, parent, child):
        self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]

    def remove_min(self):
        root_val = self.heap[0]
        self.swap(0, self.size-1)
        self.size -= 1
        self.siftdown(0)
        self.heap.pop()
        return root_val[0]

    def siftdown(self, index):
        if index < self.size-1:
            smallest = index
            left = self.left(index)
            right = self.right(index)
            if left < self.size and self.heap[left][1] < self.heap[smallest][1]:
                smallest = left
            if right < self.size and self.heap[right][1] < self.heap[smallest][1]:
                smallest = right
            if smallest != index:
                self.swap(index, smallest)
                self.siftdown(smallest)

class StackUsingHeap:
    def __init__(self):
        self.heaps = MinHeap()
        self.priority = -1

    def isEmpty(self):
        return True if self.heaps.getSize() <= 0 else False

    def top(self):
        return self.heaps.getMin()

    def push(self, value):
        self.heaps.insert(value, self.priority)
        self.priority -= 1

    def pop(self):
        self.priority += 1
        return self.heaps.remove_min() if self.heaps.getSize() > 0 else None



if __name__ == "__main__":
    arr = [3,9,2,1,4,5]
    stc= StackUsingHeap()
    for each in arr:
        stc.push(each)
    print("top value is ",stc.top())
    print("pop element in stack")
    while not stc.isEmpty():
        print(stc.pop())


