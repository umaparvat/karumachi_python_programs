"""
Given a string find first k non repeating characters
string=ABCDBAGHCHFAC k = 3 output D G F
"""
from heapq import heappop, heappush
class Pair:
    def __init__(self, count=0, index=0):
        self.count = count
        self.index = index

def non_repeating_characters(string, k):
    """
    space -> O(n)
    time complexity: O(n+klogn)
    create map of characters with count and index
    print the k characters whose count is 1 and index is small.

    :param string:
    :param k:
    :return:
    """
    map = dict()
    for index, char in enumerate(string):
        pair = map.setdefault(char, Pair())
        pair.count+=1
        pair.index = index
    index_list = []
    for key, pair in map.items():
        if pair.count == 1:
            heappush(index_list, pair.index)

    while k > 0 and index_list:
        print(string[heappop(index_list)], end=" ")
        k -= 1


def non_repeating_k_characters(string, k):
    """
    push only k characters into heap.
    compare the map element with heap root.
    if index is less than heap root
    replace the root element
    :param string:
    :param k:
    :return:
    space O(k)
    time complexity : O(n+ klog k)
    """
    map = dict()
    map = dict()
    for index, char in enumerate(string):
        pair = map.setdefault(char, Pair())
        pair.count+=1
        pair.index = index
    index_list = []

    for key, pair in map.items():
        if pair.count == 1:
            if k > 0:
                k -= 1
                heappush(index_list, pair.index)
            elif pair.index < index_list[0]:
                heappop(index_list)
                heappush(index_list, pair.index)
    while index_list:
        print(string[heappop(index_list)], end=" ")




if __name__ == "__main__":
    string = "ABCDBAGHCHFAC"
    k = 3
    non_repeating_characters(string, k)
    print("\n")
    non_repeating_k_characters(string, k)