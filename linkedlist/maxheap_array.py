from ctypes import py_object

class Array:
    def __init__(self, size):
        py_array = py_object * size
        self._slot = py_array()
        self._size = size
        self.clear(None)

    def clear(self, value):
        for i in range(self._size):
            self._slot[i] = value

    def __len__(self):
        return self._size

    def __setitem__(self, key, value):
        assert key < self._size, "Index out of range"
        self._slot[key] = value

    def __getitem__(self, item):
        assert 0 <= item < self._size, "Index out of range"
        return self._slot[item]


class MaxHeap:
    def __init__(self, size):
        self.arr = Array(size)
        self._count = 0

    def __len__(self):
        return self._count

    def capacity(self):
        return len(self.arr)

    def add(self, item):
        assert len(self) < self.capacity(), "Cannot add item to the full heap"
        self.arr[self._count] = item
        self._count += 1
        self._siftUp(self._count-1)

    def _siftUp(self, indx):
        if indx > 0:
            curr_parent_ind = indx // 2
            if self.arr[curr_parent_ind] < self.arr[indx]:
                temp = self.arr[curr_parent_ind]
                self.arr[curr_parent_ind] = self.arr[indx]
                self.arr[indx] = temp
                self._siftUp(curr_parent_ind)
    def extract(self):
        assert self._count > 0, "cannot extract item from empty heap"
        temp = self.arr[0]
        self._count -= 1
        self.arr[0] = self.arr[self._count]
        self._siftDown(0)
        return temp

    def _swapitems(self, ind, largest):
        temp = self.arr[ind]
        self.arr[ind] = self.arr[largest]
        self.arr[largest] = temp

    def _siftDown(self, ind):
        left_child_ind = 2 * ind + 1
        right_child_ind = left_child_ind + 1
        largest = ind
        if left_child_ind <= self._count and self.arr[left_child_ind] > self.arr[largest]:
            largest = left_child_ind
        elif right_child_ind <= self._count and self.arr[right_child_ind] > self.arr[largest]:
            largest = right_child_ind
        if largest != ind:
            self._swapitems(ind, largest)
            self._siftDown(largest)

if __name__ == "__main__":

    t = MaxHeap(5)
    t.add(4)
    t.add(10)
    t.add(2)
    t.add(1)
    t.add(7)
    print("Inserted values: 4 10 2 1 7")
    print("now tree values are:")
    while len(t) > 0:
        print(t.extract(), end=" ")
