# User function Template for python3
from collections import OrderedDict


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

    def __str__(self):
        return str(self.children)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
            cur.count += 1
        cur.is_end = True

    def dfs(self, word, prefix, output):

        #print(word)
        cur = self.root
        for char in word:
            #print(char, prefix, output, cur.children)
            prefix += char
            #print(prefix)
            cur = cur.children[char]
            if cur.count == 1:
                output.append(prefix)
                return
        if cur.is_end:
            output.append(prefix)
        return


class Solution:
    def findPrefixes(self, arr, N):
        """
        Time complexity: O(N* length of each word)
        space complexity: O(N* length of each word)
        :param arr:
        :param N:
        :return:
        """
        # code here
        tr = Trie()
        for each in arr:
            # print("insert", each)
            tr.insert(each)
        output = []
        for each in arr:
            tr.dfs(each, "", output)
        return output


# {
#  Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(10 ** 6)
if __name__ == '__main__':
    arr = ["geeksgeeks" ,"geeksquiz", "geeksforgeeks"]

    s =Solution()
    print(s.findPrefixes(arr, 3))
    arr =["zebra", "dog", "dove", "duck"]
    print(s.findPrefixes(arr, 4))
# } Driver Code Ends