import heapq
def maxEvents(start, end, N):
    # code here
    events = []
    for s1, e1 in zip(start, end):
        events.append([s1, e1])
    events.sort(key=lambda x: (x[0], x[1]))
    idx = 0
    # priority queue ---- heap-----heapq
    n = len(events)
    heap = []
    res = 0
    d = events[idx][0]
    print(events)
    print("first", d)
    while heap or idx < n:
        if not heap:
            d = events[idx][0]
        print("after", heap, d, idx, events[idx])
        while idx < n and events[idx][0] <= d:
            heapq.heappush(heap, events[idx][1])
            idx += 1
        print("heap now", heap)
        heapq.heappop(heap)
        print("pop", heap)
        res += 1
        d += 1
        print("res, d", res, d, idx)
        while heap and heap[0] < d:
            heapq.heappop(heap)
    return res


if __name__ == "__main__":
    start = [5, 10, 1, 2, 4, 1, 1, 1, 1]
    end  =  [5, 10, 2, 7, 9, 3, 3, 1, 5]
    N = 9
    print(maxEvents(start, end, N))