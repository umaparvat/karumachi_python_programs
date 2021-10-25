class Minheap:
    def __init__(self):
        self.heaps = []
        self.size = 0

    def __len__(self):
        return self.size

    def top(self):
        return self.heaps[0] if self.heaps else None

    def insert(self, value):
        """
        O(logn)
        :param value:
        :return:
        """
        if len(self) == 0:
            self.heaps.append(value)
            self.size += 1
        else:
            self.heaps.append(value)
            self.size += 1
            self.siftup(self.size-1)

    def left(self, index):
        return 2*index+1

    def right(self, index):
        return 2*index+2

    def siftup(self, index):
        if index > 0 and (index-1)//2 >=0:
            parent = (index-1)//2
            left = self.left(parent)
            right = self.right(parent)
            smallest = parent
            if left < len(self) and self.heaps[left] < self.heaps[smallest]:
                smallest = left
            if right < len(self) and self.heaps[right] < self.heaps[smallest]:
                smallest = right
            if parent != smallest:
                self.swap(parent, smallest)
            self.siftup(parent)


    def siftdown(self, index):
        if index < self.size-1:
            left = self.left(index)
            right = self.right(index)
            smallest = index
            if left < len(self) and self.heaps[left] < self.heaps[smallest]:
                smallest = left
            if right < len(self) and self.heaps[right] < self.heaps[smallest]:
                smallest = right
            if smallest != index:
                self.swap(index, smallest)
                self.siftdown(smallest)

    def swap(self, start, end):
        self.heaps[start], self.heaps[end] = self.heaps[end], self.heaps[start]

    def removeTop(self):
        """
        O(logn)
        :return:
        """
        if len(self) > 0:
            top = self.top()
            self.swap(0, len(self)-1)
            self.size -= 1
            self.siftdown(0)
            self.heaps.pop()
            return top
        else:
            return None


class Maxheap:
    def __init__(self):
        self.heaps = []
        self.size = 0

    def __len__(self):
        return self.size

    def top(self):
        return self.heaps[0] if self.heaps else 0

    def insert(self, value):
        if len(self) == 0:
            self.heaps.append(value)
            self.size += 1
        else:
            self.heaps.append(value)
            self.size += 1
            self.siftup(self.size - 1)

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def siftup(self, index):
        if index > 0 and (index - 1) // 2 > 0:
            parent = (index - 1) // 2
            left = self.left(parent)
            right = self.right(parent)
            largest = parent
            if left < len(self) and self.heaps[left] > self.heaps[largest]:
                largest = left
            if right < len(self) and self.heaps[right] > self.heaps[largest]:
                largest = right
            if parent != largest:
                self.swap(parent, largest)
            self.siftup(parent)

    def siftdown(self, index):
        if index < self.size - 1:
            left = self.left(index)
            right = self.right(index)
            largest = index
            if left < len(self) and self.heaps[left] > self.heaps[largest]:
                largest = left
            if right < len(self) and self.heaps[right] > self.heaps[largest]:
                largest = right
            if largest != index:
                self.swap(index, largest)
                self.siftdown(largest)

    def swap(self, start, end):
        self.heaps[start], self.heaps[end] = self.heaps[end], self.heaps[start]

    def removeTop(self):
        if len(self) > 0:
            top = self.top()
            self.swap(0, len(self) - 1)
            self.size -= 1
            self.siftdown(0)
            self.heaps.pop()
            return top
        else:
            return None

def median(elements):
    minheap = Minheap()
    maxheap = Maxheap()
    if len(elements) == 1:
        return elements[0]
    else:
        for current in elements:
            if len(maxheap) == 0 or maxheap.top() >= current:
                maxheap.insert(current)
            else:
                minheap.insert(current)
            balanceheaps(maxheap, minheap)
        return findMedian(maxheap, minheap)

def balanceheaps(maxheap, minheap):
    if len(maxheap) > len(minheap)+1:
        minheap.insert(maxheap.removeTop())
    elif len(maxheap) < len(minheap):
        maxheap.insert(minheap.removeTop())
    else:
        return


def findMedian(maxheap, minheap):
    if len(maxheap) == len(minheap):
        return (maxheap.top()+minheap.top())/2
    else:
        return maxheap.top()

if __name__ == "__main__":
    ele = [1,7,3,0,5,8,3,2,6,9]
    print(median(ele))