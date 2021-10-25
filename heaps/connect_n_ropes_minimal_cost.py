"""
Given n ropes of different length, connect them into
single rope with minimal cost,
Assume cost to connect two ropes is the same as sum of
their length

Input:  [5, 4, 2, 8]

Output: The minimum cost is 36

[5, 4, 2, 8] –> First, connect ropes of lengths 4 and 2 that will cost 6.
[5, 6, 8]    –> Next, connect ropes of lengths 5 and 6 that will cost 11.
[11, 8]      –> Finally, connect the remaining two ropes that will cost 19.

Therefore, the total cost for connecting all ropes is 6 + 11 + 19 = 36
"""
from heapq import heappop, heappush, heapify


def connect_ropes(arr):
    """
    n+nlogn => time complexity => O(nlogn)
    space ->O(n)
    :param arr:
    :return:
    """
    heapify(arr)
    total = 0
    if len(arr) < 2:
        return arr[0]
    while len(arr) > 1:
        first = heappop(arr)
        second = 0
        if arr:
            second = heappop(arr)
        cost = first+second
        total += cost
        heappush(arr, cost)
    return total

if __name__ == "__main__":
    arr = [ 5,4, 2,8]
    print(connect_ropes(arr))