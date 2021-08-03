from linkedlist.maxheap_array import MaxHeap


def swap(theseq, start, end):
    temp = theseq[start]
    theseq[start] = theseq[end]
    theseq[end] = temp

def siftdown(theseq, pos):
    pass

def heap_sort(theseq, pos):
    swap(theseq, 0, pos)
    siftdown(theseq, pos-1)


if __name__ == "__main__":
    t = MaxHeap(5)
    t.add(4)
    t.add(10)
    t.add(2)
    t.add(1)
    t.add(7)
    theseq = t.arr
    len_arr = len(theseq)
    heap_sort(theseq, len_arr-1)