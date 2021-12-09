"""
1. all non zero degere vertices are singly connected
2. all vertices has indegree and outdegree same
"""
from collections import defaultdict
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
        self.indegree = [0]*vertex

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    def checkdegree(self):
        """
        O(V)
        :return:
        """
        for v in range(self.V):
            if len(self.graph[v]) != self.indegree[v]:
                return False
        return True

    def dfsutil(self, v, visited, graph):
        visited[v] = True
        for neighbour in graph[v]:
            if visited[neighbour] is False:
                self.dfsutil(neighbour, visited, graph)

    def transpose(self):
        gr = Graph(self.V)
        for i in range(self.V):
            for neighbour in self.graph[i]:
                gr.graph[neighbour].append(i)
                gr.indegree[i] += 1
        return gr.graph

    def isSc(self):
        """
        O(v+E)
        :return:
        """
        visited = [False]*self.V
        i = 0
        for i in range(self.V):
            if len(self.graph[i]) > 0:
                break
        self.dfsutil(i, visited, self.graph)
        if any(each is False for each in visited):
            return False
        visited = [False]*self.V
        graph = self.transpose()
        self.dfsutil(i, visited, graph)
        if any(each is False for each in visited):
            return False
        return True

    def is_eulerian(self):
        """
        O(V+E)+O(V) = O(V+E)
        time compleixty: O(V+E)
        :return:
        """
        if not self.isSc():
            return False
        if not self.checkdegree():
            return False
        return "eulerian"


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
    print(g.is_eulerian())



