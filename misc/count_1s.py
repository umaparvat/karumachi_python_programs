from collections import deque


class Solution:
    def ValidCorner(self, matrix):
        # Your code goes here
        def solve(x, y, m, n, i):
            if x >= m or y >= n:
                return False
            if matrix[x][y] == 1:
                return True
            i += 1
            return solve(x + i, y, m, n, i) and solve(x, y + i, m, n, i) and solve(x + i, y + i, m, n, i)

        if not matrix:
            return "Yes"
        queue = deque()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    queue.append([i, j])
        if not queue:
            return False
        while queue:
            x, y = queue.popleft()
            ans = solve(x, y, m, n, 1)
            if ans == True:
                return True
        return False


if __name__ == "__main__":
    arr = [[1,0,0,1,0],
           [0,0,0,0,1],
           [0,0,0,1,0],
           [1,0,1,0,1]]
    s = Solution()
    print(s.ValidCorner(arr))