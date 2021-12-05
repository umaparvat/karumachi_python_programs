nv = 4
INF = 999

def floyd_warshall(G):
    """
    time complexity: O(n*n*n)
    space complexity: O(n*n)
    :param G: 
    :return:
    """
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    printarr(distance)

def printarr(distance):
    row = len(distance)
    col = len(distance[0])
    for i in range(row):
        for j in range(col):
            if distance[i][j] == INF:
                print(INF, end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")

if __name__ == "__main__":
    G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
    floyd_warshall(G)