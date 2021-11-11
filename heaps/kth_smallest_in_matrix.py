# User function Template for python3
import heapq


class pair:
    def __init__(self, data, ind):
        self.data = data
        self.ind = ind

    def __lt__(self, other):
        return self.data > other.data


def kthSmallest(mat, n, k):
    # Your code goes here
    pq = []
    row = column = 0
    terminate = False
    for j in range(n):
        for i in range(n):
            if len(pq) < k:
                heapq.heappush(pq, -mat[i][j])
                print(i,j, mat[i][j], terminate)
            else:
                if mat[i][j] < -pq[0]:
                    heapq.heapreplace(pq, -mat[i][j])

    print(pq, row, column)
    return -pq[0]


# {
#  Driver Code Starts
# Initial Template for Python 3

# Driver Code

def main():
    n = 4
    k = 7
    mat =[[10, 20, 30, 40],
          [15, 25, 35, 45],
          [24, 29, 37, 48],
          [32, 33, 39, 50]]
    print(kthSmallest(mat, n, k))



if __name__ == "__main__":
    main()

# } Driver Code Ends