from collections import defaultdict

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def addEdge(self, source, destination):
        self.graph[source].append(destination)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        print(stack[-1::-1])

    def topologicalSortUtil(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbour in self.graph[vertex]:
            if not visited[neighbour]:
                self.topologicalSortUtil(neighbour, visited, stack)
        stack.append(vertex)
        print(stack, vertex, visited)





if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    print("Following is a Topological Sort of the given graph")
    g.topologicalSort()