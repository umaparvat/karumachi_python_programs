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


class Node:

    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacent_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError(f"Vertex {v} cannot be adjacent to itself")
        self.adjacent_set.add(v)

    def get_adjacent_vertices(self):
        return self.adjacent_set


class AdjacentSet(Graph):

    def __init__(self, number_of_vertices, directed=False):
        super().__init__(number_of_vertices=number_of_vertices, directed=directed)
        self.vertex_list = []

        for i in range(number_of_vertices):
            self.vertex_list.append(Node(vertex_id=i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.number_of_vertices or v2 >= self.number_of_vertices or v1 < 0 or v2 < 0:
            return ValueError(f"Vertices v1 and v2 are out of bond")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v >= self.number_of_vertices or v < 0:
            raise ValueError(f"Vertex {v} not present")
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        degree = 0
        for i in range(len(self.vertex_list)):
            if v in self.get_adjacent_vertices(i):
                degree += 1
        return degree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(len(self.vertex_list)):
            for v in self.get_adjacent_vertices(i):
                print(f"{i} ---> {v}")


adj_set_graph = AdjacentSet(4, True)

adj_set_graph.add_edge(0, 1)
adj_set_graph.add_edge(0, 2)
adj_set_graph.add_edge(2, 3)

for i in range(adj_set_graph.number_of_vertices):
    print(f"adjacent vertices of {i} {adj_set_graph.get_adjacent_vertices(i)}")

for i in range(adj_set_graph.number_of_vertices):
    print(f"indegree of {i} {adj_set_graph.get_indegree(i)}")

adj_set_graph.display()
