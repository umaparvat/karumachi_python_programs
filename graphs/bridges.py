"""
cutbridge -> edge(u,v)  if v has a back edge to ancestors of u
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def APUtil(self, u, parent, disc, visited, ap, low):
        children = 0
        low[u] = self.time
        disc[u] = self.time
        self.time += 1
        visited[u] = True
        for v in self.graph[u]:
            if visited[v] is False:
                parent[v] = u
                children += 1
                self.APUtil(v, parent, disc, visited, ap, low)

                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    ap[u] = True
                    print("edges", (u,v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])


    def AP(self):
        """
        time complexity: O(V+E)
        :return:
        """
        visited = [False] * self.V
        ap = [False] * self.V
        parent = [-1] * self.V
        disc = [float("INF")] * self.V
        low = [float("INF")] * self.V
        for i in range(self.V):
            if visited[i] is False:
                self.APUtil(i, parent, disc, visited, ap, low)

        for index, value in enumerate(ap):
            if value is True:
                print(index)


if __name__ == "__main__":

    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    g1.AP()
    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print("bridges in second  graph")
    g2.AP()

    g3 = Graph(7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    print("bridges in third graph")
    g3.AP()