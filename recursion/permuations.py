# User function Template for python3
from copy import deepcopy
class Solution:
    def uniquePerms(self, arr, n):
        # code here
        map_dict = {}
        if len(arr) < n:
            return 0

        def permutation(start, end):
            if start == end:
                s= "".join(map(str, arr))
                map_dict[s] = deepcopy(arr)
            for  i in range(start, end+1):
                arr[i], arr[start] = arr[start], arr[i]
                permutation(start+1, end)
                arr[i], arr[start] = arr[start], arr[i]
        arr.sort()
        permutation(0, len(arr)-1)
        return list(map_dict.values())





# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    n = 6
    arr = [2, 1, 2, 3, 4, 5]
    ob = Solution()
    res = ob.uniquePerms(arr, n)
    for i in range(len(res)):
        for j in range(n):
            print(res[i][j], end=" ")
        print()
# } Driver Code Ends