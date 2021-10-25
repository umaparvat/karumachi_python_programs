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

def getMinimumVertex(mst:list, key):
    minKey = float("inf")
    vertex = -1
    for ind in range(self.vertices):
        if not mst[ind] and minKey > key[ind]:
            minKey = key[ind]
            vertex  = ind
    return vertex


class Resultset:
    def __int__(self, parent=None, weight = None):
        self.parent = parent
        self.weight = weight


def primMst(vertices):
    mst = [False for _ in range(vertices)]
    resultset = [Resultset for _ in range(vertices)]
    key = [float("inf") for each in range(vertices)]
    key[0] = 0
    resultset[0].parent = -1

