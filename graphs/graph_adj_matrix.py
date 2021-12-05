from abc import ABC, abstractmethod


class Graph(ABC):

    def __init__(self, number_of_vertices, directed=False):
        self.number_of_vertices = number_of_vertices
        self.directed = directed

    @abstractmethod
    def add_edge(self, v1, v2, weight=1):
        pass

    @abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abstractmethod
    def get_indegree(self, v):
        pass

    @abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abstractmethod
    def display(self):
        pass


class AdjacentMatrix(Graph):

    def __init__(self, number_of_vertices, directed=False):
        super().__init__(number_of_vertices=number_of_vertices, directed=directed)
        self.matrix = [[0 for _ in range(self.number_of_vertices)] for _ in range(4)]

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.number_of_vertices or v2 >= self.number_of_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} or {v2} are out of bonds")

        if weight < 1:
            raise ValueError(f"Weight {weight} is not allowed")

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v >= self.number_of_vertices or v < 0:
            raise ValueError(f"Vertex {v} is not present in graph")
        adjacency = []
        for i in range(self.number_of_vertices):
            if self.matrix[v][i] > 0:
                adjacency.append(i)
        return adjacency

    def get_indegree(self, v):
        if v >= self.number_of_vertices or v < 0:
            raise ValueError(f"Vertex {v} is not present in graph")

        indegree = 0
        for i in range(self.number_of_vertices):
            if self.matrix[i][v] > 0:
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        if v1 >= self.number_of_vertices or v2 >= self.number_of_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} or {v2} are out of bonds")
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.number_of_vertices):
            for v in self.get_adjacent_vertices(i):
                print(f"{i} ---> {v}")


adj_matrix_graph = AdjacentMatrix(number_of_vertices=4, directed=False)

adj_matrix_graph.add_edge(0, 1)
adj_matrix_graph.add_edge(0, 2)
adj_matrix_graph.add_edge(2, 3)

adj_matrix_graph.display()

for i in range(adj_matrix_graph.number_of_vertices):
    print(f"adjacent vertices for {i} {adj_matrix_graph.get_adjacent_vertices(i)}")

for i in range(adj_matrix_graph.number_of_vertices):
    print(f"indegree of {i} {adj_matrix_graph.get_indegree(i)}")

for i in range(adj_matrix_graph.number_of_vertices):
    for j in adj_matrix_graph.get_adjacent_vertices(i):
        print(f"weight of {i} and {j} {adj_matrix_graph.get_edge_weight(i, j)}")
