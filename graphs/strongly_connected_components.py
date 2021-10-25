from collections import defaultdict
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def dfs(self, d, visitedvertex):
        visitedvertex[d] = True
        print(d, end =" ")
        for i in self.graph[d]:
            if not visitedvertex[i]:
                self.dfs(i, visitedvertex)

    def fill_order(self, d, visitedvertex, stack):
        visitedvertex[d] = True
        for i in self.graph[d]:
            if not visitedvertex[i]:
                self.fill_order(i, visitedvertex, stack)
        stack.append(d)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):
        stack = []
        visitedvertex = [False]*self.V
        for i in range(self.V):
            if not visitedvertex[i]:
                self.fill_order(i, visitedvertex, stack)
        reverse_g = self.transpose()
        visitedvertex = [False]*self.V
        while stack:
            d = stack.pop()
            if not visitedvertex[d]:
                reverse_g.dfs(d, visitedvertex)
                print(" ")


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
    g.print_scc()



