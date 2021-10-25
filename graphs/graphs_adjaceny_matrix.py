"""
O(v*v) complexity  and space O(v*v)
"""
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.matrix = [[0 for _ in range(vertex)] for _ in range(vertex)]

    def add_edge(self, source, destination):
        self.matrix[source][destination] = 1
        self.matrix[destination][source] = 1

    def remove_edge(self, source, destination):
        if not self.matrix[source][destination]:
            return
        self.matrix[source][destination] = 0
        self.matrix[destination][source] = 0

    def print_matrix(self):

        for ind, row in enumerate(self.matrix):
            print(ind, end=" ")
            for val in row:
                print("{:4}".format(val), end=" ")
            print(" ")


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()

if __name__ == "__main__":
    main()