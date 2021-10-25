"""
given a stream of integers
find the k'th largest string.
if k th element is not present
return None
"""
from heapq import heappush, heappop

def kthlargestinteger(integer, pq, k):

    if len(pq) < k-1:
        heappush(pq, integer)
        return -1
    elif integer > pq[0]:
        heappush(pq, integer)
    return heappop(pq)

if __name__ == "__main__":
    """
    space complexity: O(k)
    time complexity: O(log(k))
    """
    pq = []
    k = 3
    while True:
        try:
            integer = input().strip()
            x = kthlargestinteger(int(integer), pq, k)
            if x == -1:
                print("Kth largest element is None")
            else:
                print(f"Kth largest element is {x}")

        except (EOFError, IOError, Exception) :
            break
