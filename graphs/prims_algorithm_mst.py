"""
Minimum spanning tree with adjacency_matrix
O(V2)

"""

class Graph:
    def __init__(self, vertex):
        self.vertices = vertex
        self.matrix = [[0 for _ in range(vertex)] for _ in range(vertex)]

    def addEdge(self, source, destination, weight):
        self.matrix[source][destination] = weight
        self.matrix[destination][source] = weight

    def getMinimumVertex(self, mst:list, key):
        minKey = float("inf")
        vertex = -1
        for ind in range(self.vertices):
            if not mst[ind] and minKey > key[ind]:
                minKey = key[ind]
                vertex  = ind
        return vertex

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(parent[i], "-", i, "\t", self.matrix[i][parent[i]])

    def prims(self):
        key = [float("inf") for _ in range(self.vertices)]
        key[0] = 0
        parent = [None for _ in range(self.vertices)]
        mst = [False for _ in range(self.vertices)]
        parent[0]  = -1
        for cout in range(self.vertices):
            u = self.getMinimumVertex(mst, key)
            mst[u] = True
            for v in range(self.vertices):
                if self.matrix[u][v] > 0 and mst[v] == False and key[v] > self.matrix[u][v]:
                    key[v] = self.matrix[u][v]
                    parent[v] = u
        print(parent)
        self.printMST(parent)


if __name__ == "__main__":
    g = Graph(5)
    g.matrix = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
    g.prims()