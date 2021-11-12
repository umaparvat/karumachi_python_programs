"""
Water distribution pipeline
Bipartite matching problem
Circulation with demands
"""


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.V = len(self.graph)

    def search_alg_bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, each_v in enumerate(self.graph[u]):
                if visited[ind] == False and each_v > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return  True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0
        while self.search_alg_bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink
            while s!= source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


if __name__ == "__main__":
    graph = [[0, 8, 0, 0, 3, 0],
             [0, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 7, 2],
             [0, 0, 0, 0, 0, 5],
             [0, 0, 7, 4, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    g = Graph(graph)

    source = 0
    sink = 5

    print("Max Flow: %d " % g.ford_fulkerson(source, sink))

