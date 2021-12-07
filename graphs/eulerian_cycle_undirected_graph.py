"""
eulerian cycle in undirected graph
1. all non zero vertices connected together
2. all vertices must be even degree

eulerain path
 -> all non zero vertices are connected together
 -> zero or two vertices are odd degree, all other vertices even degree
"""
from collections import defaultdict
class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfsutil(self, v, visited):
        visited[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] is False:
                self.dfsutil(neighbour, visited)

    def is_connected(self):
        """
        time complexity: O(V+E) -> DFS
        :return:
        """
        i = 0
        while i < self.V:
            if len(self.graph[i]) > 1 :
                break
            i += 1

        # no edges in graph
        if i == self.V-1:
            return True
        visited = [False] * self.V
        self.dfsutil(i, visited)
        # all non zero degree are visited
        for j in range(self.V):
            if visited[j] == False and len(self.graph[j]) > 0:
                return False
        return True

    def isEulerian(self):
        """
        if all non zero degree vertex is connected
        and odd degree vertex is 0 , it's eulerian cycle
        if odd degree vertex count is 2, it's eulerian path
        more than 2, it's neighter path nor cycle
        :return:
        """
        if self.is_connected() is False:
            return False
        odd = 0
        for i in range(self.V):
            if len(self.graph[i])%2 != 0:
                odd += 1

        if odd == 0:
            print("Eulerian cycle")
        elif odd == 2:
            print("eulerian path")
        else:
            print("neither eulerian nor path")

if __name__ == "__main__":
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    g1.isEulerian()