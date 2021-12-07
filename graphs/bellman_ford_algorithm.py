

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, src, destination, weight):
        self.graph.append([src,destination,weight])
    def print_soln(self, distance):
        for k in range(self.V):
            print("{0}\t\t{1}".format(k, distance[k]))
            print("\n")


    def bellman_ford(self, src):
        dist = [float("inf") for _ in range(self.V)]
        prev = [ 0 for _ in range(self.V)]
        dist[src] = 0
        for i in range(self.V-1):
            for a, b, c in self.graph:
                if dist[a] != float("inf") and dist[a]+c < dist[b]:
                    dist[b] = dist[a]+c
                    prev[b] = a


        for a,b,c in self.graph:
                if dist[a] != float("inf") and dist[a] + c < dist[b]:
                    raise Exception("loop exists")


        self.print_soln(dist)

if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(0, 1, 2)

    g.add_edge(0, 2, 4)

    g.add_edge(1, 3, 2)

    g.add_edge(2, 4, 3)

    g.add_edge(2, 3, 4)

    g.add_edge(4, 3, -5)

    g.bellman_ford(0)



