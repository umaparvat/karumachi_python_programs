

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for _ in range(vertex)]for _ in range(vertex)]

    def minimum_vertex(self, visited, distance):
        min = float("inf")
        for v in range(self.V):
            if distance[v] < min and visited[v] is False:
                min = distance[v]
                min_index = v
        return min_index

    def dijistra(self, src):
        """
        time complexity: O(V*V)
        1. find minmum vertex.(initally starts with 0)
        2. calculate the adjacent vertex for the selected minimum vertex if the adjacet is not visited
            distance(adjancent_vertex) > distance(minmum_vertex)+edge(minimum_vertex, adjacent_vertex)
            then update the distance of adjacent to distance(minmum_vertex)+edge(minimum_vertex, adjacent_vertex)
        :param src:
        :return:
        """
        distance = [float("inf")] * self.V
        visited = [False] * self.V
        distance[src] = 0

        for _ in range(self.V):
            min_index = self.minimum_vertex(visited, distance)
            visited[min_index] = True
            for v in range(self.V):
                if self.graph[min_index][v] > 0 and \
                    visited[v] is False and \
                        distance[v] > distance[min_index]+self.graph[min_index][v]:
                    distance[v] = distance[min_index]+self.graph[min_index][v]

        print(self.solution(distance))

    def solution(self, distance):
        print("distance from node ")
        for v in range(self.V):
            print(v, "t", distance[v])


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
    g.dijistra(0)