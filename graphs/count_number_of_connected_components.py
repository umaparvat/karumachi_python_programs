"""
count the number of connected componets in adj list

1. apply kosraraju algorithm
The below problem is not working . Need to fix it.
"""
from collections import defaultdict
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def transpose(self):
        gr = Graph(self.V)
        for i in range(self.V):
            for j in range(self.V):
                gr.graph[j].append(i)
        return gr.graph

    def dfs(self, vertex, visited, graph):
        visited[vertex] = True
        for v in graph[vertex]:
            if visited[v] is False:
                self.dfs(v, visited, graph)

    def fillorder(self, vertex, visited, stack):
        visited[vertex] = True
        for v in self.graph[vertex]:
            if visited[vertex] is False:
                self.fillorder(v, visited, stack)
        stack.append(vertex)

    def print_count_scc(self):
        """
        time complexity: O(V+E)
        :return:
        """
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.fillorder(i, visited, stack)
        gr = self.transpose()
        output = []
        visited = [False] * self.V
        while stack:
            cur = stack.pop()
            if visited[cur] is False:
                self.dfs(cur, visited, gr)
        visited = [False] * self.V
        output = [0] * self.V
        for i in range(self.V):
            output[i] = self.count_dfs(i, self.V)
        print(output)

    def count_dfs(self, vertex, V):
        visited = [False] * V
        c = 0
        for v in self.graph[vertex]:
            if visited[v] is False:
                c += 1
                self.dfs(vertex, visited, self.graph)
        return c



if __name__ == "__main__":
    g = Graph(8)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    g.add_edge(6, 7)
    g.print_count_scc()



