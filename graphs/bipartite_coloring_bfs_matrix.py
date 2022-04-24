
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_bipartite(self, src):
        """ this works only if the graph is connected.
        no edge connected vertex is also bipartite refer below algorithm
        time complexity: O(V+E)
        """
        colors = [-1] * self.V
        colors[src] = 1
        queue = [src]
        while queue:
            current = queue.pop(0)
            if self.graph[current][current] == 1:
                # if it's a self loop
                return False
            for neighbour in self.graph[current]:
                if self.graph[current][neighbour] == 1 and colors[neighbour] == -1:
                    colors[neighbour] = 1- colors[current]
                    queue.append(neighbour)
                elif self.graph[current][neighbour] == 1 and colors[neighbour] == colors[current]:
                    return False
        return True

    def util(self, src, colors):
        colors[src] = 1
        queue = [src]
        while queue:
            current = queue.pop(0)
            if self.graph[current][current] == 1:
                # if it's a self loop
                return False
            for neighbour in self.graph[current]:
                if self.graph[current][neighbour] == 1 and colors[neighbour] == -1:
                    colors[neighbour] = 1- colors[current]
                    queue.append(neighbour)
                elif self.graph[current][neighbour] == 1 and colors[neighbour] == colors[current]:
                    return False
        return True
    def is_bipartiteutil(self):
        """
        time complexity: O(V^2)
        This works well with diconnected graph.
        :return:
        """
        colors = [-1] * self.V

        for i in range(self.V):
            if colors[i] == -1:
                if not self.util(i, colors):
                    return False
        return True


if __name__ == "__main__":
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]
              ]
    print(g.is_bipartite(0))
    print()