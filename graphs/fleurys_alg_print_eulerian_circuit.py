"""
This alogrithm is for undirected graph

Assume it has eulerian circuit
    criteria for eulerian circuit
        1. all non zero vertex are connected
        2. all vertex has even degree
    criteria for eulerian path
        1. same as point 1 in eulerian circuit
        2. two vertex has odd degree
step for printing eulerian circuit
    1. start from any odd vertex. if no odd degree vertex start at 0.
    2. check whether a edge is a bridge or not. consider non bridge.
        bridge -> remove the edge from (u-v). count number of nodes reachable from u. if it's decreased
                  it's a bridge.
    3. if it edge is only one consider it immediately.
"""
from collections import defaultdict
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        for ind, each in enumerate(self.graph[u]):
            if each == v:
                self.graph[u].pop(ind)
        for ind, each in enumerate(self.graph[v]):
            if each == u:
                self.graph[v].pop(ind)

    def dfs(self, v, visited):
        visited[v] = True
        count = 1
        for neighbour in self.graph[v]:
            if visited[neighbour] is False:
                count += self.dfs(neighbour, visited)
        return count

    def isValidEdge(self, u, v):
        """
        2 times DFS check
        O(V+E)
        :param u:
        :param v:
        :return:
        """
        if len(self.graph[u]) == 1:
            return True
        visited = [False]*self.V
        count_vertex = self.dfs(u, visited)
        self.remove_edge(u, v)
        visited = [False]*self.V
        count2_vertex = self.dfs(u, visited)
        valid = True
        if count_vertex > count2_vertex:
            valid = False
        self.add_edge(u,v)
        return valid


    def print_eulerian(self, v):
        """
        O(v+E)^2
        :param v:
        :return:
        """
        for neighbour in self.graph[v]:
            if self.isValidEdge(v, neighbour):
                print(f"{v}-{neighbour}")
                self.remove_edge(v, neighbour)
                self.print_eulerian(neighbour)

    def eulerian_path(self):
        v = 0
        for v in range(self.V):
            if len(self.graph[v]) %2 != 0:
                break
        self.print_eulerian(v)


if __name__ == "__main__":
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.eulerian_path()

