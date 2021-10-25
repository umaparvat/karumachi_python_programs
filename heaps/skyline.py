import heapq
class Solution:
    def getSkyline(self, buildings) -> list:
        N, hs = len(buildings), []
        for i, (l, r, h) in enumerate(buildings):
            hs.append((l, 0, -h, i))
            hs.append((r, 1, h, i))
        hs.sort()
        print(hs)
        alive = [False] * N

        res, heap, current_height = [], [], 0
        for x, tp, h, i in hs:
            if tp == 0:  # start of i-th building
                heapq.heappush(heap, (h, i))
                alive[i] = True
                if current_height < -h:
                    res.append([x, -h])
                    current_height = -h
            else:  # end of i-th building
                alive[i] = False
                print(heap, current_height)
                while heap and not alive[heap[0][1]]:
                    heapq.heappop(heap)
                if heap and -heap[0][0] < current_height:
                    current_height = -heap[0][0]
                    res.append([x, current_height])
                elif heap and heap[0][0] < h:
                    heapq.heappop(heap)
                    current_height = h
                    res.append([x,current_height])
                elif not heap and h >= current_height:
                    current_height = 0
                    res.append([x, current_height])
        return res

if __name__ == "__main__":
    print(Solution().getSkyline([[2,9,10], [3,7,12], [5,12,15], [15,20,10], [19,24,8]]))