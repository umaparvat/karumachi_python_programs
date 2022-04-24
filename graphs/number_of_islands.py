# User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, m, n):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            grid[i][j] = 2
            for dire in dirs:
                new_x = i + dire[0]
                new_y = j + dire[1]
                if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                    dfs(new_x, new_y, m, n)

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j, m, n)
                    ans += 1
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends