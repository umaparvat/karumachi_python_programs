


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0]*vertices for _ in range(vertices)]

    def add_edge(self, src, dest, w):
        self.graph[src][dest] = w
        self.graph[dest][src] = w

    def min_index(self, distance, visited):
        minimum = float("inf")
        min_index = None
        for v in range(self.V):
            if distance[v] < minimum and visited[v] is False:
                minimum = distance[v]
                min_index = v
        return min_index

    def dijkstras_ssp(self, src):
        """
        time complexity: O(V *V)
        space : O(V)
        :param src:
        :return:
        """
        visited = [False]*self.V
        distance = [float("inf")]*self.V
        distance[src] = 0
        for _ in range(self.V):
            u = self.min_index(distance, visited)
            if not u:
                continue
            visited[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] is False and distance[v] > distance[u]+self.graph[u][v]:
                    distance[v] = distance[u]+self.graph[u][v]


        return distance

    def dijkstras_allpair(self):
        """
        time complexity: O(V*V*V)
        space complexity: O(V*V)
        :return:
        """
        output = [[0]*self.V for _ in range(self.V)]
        for v in range(0, self.V):
            output[v] = self.dijkstras_ssp(v)
        print(output)

if __name__ == "__main__":
    if __name__ == "__main__":
        g = Graph(9)
        g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                   [4, 0, 8, 0, 0, 0, 0, 11, 0],
                   [0, 8, 0, 7, 0, 4, 0, 0, 2],
                   [0, 0, 7, 0, 9, 14, 0, 0, 0],
                   [0, 0, 0, 9, 0, 10, 0, 0, 0],
                   [0, 0, 4, 14, 10, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 2, 0, 1, 6],
                   [8, 11, 0, 0, 0, 0, 1, 0, 7],
                   [0, 0, 2, 0, 0, 0, 6, 7, 0]
                   ]
        g.dijkstras_allpair()