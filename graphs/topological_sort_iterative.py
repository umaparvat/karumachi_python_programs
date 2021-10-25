from collections import defaultdict

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def addEdge(self, source, destination):
        self.graph[source].append(destination)

    def get_neighbour(self, vertex):
        for neighbour in self.graph[vertex]:
            yield neighbour

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        print(stack[::-1])

    def topologicalSortUtil(self, vertex, visited, stack):
        visited[vertex] = True
        working_stack = [(vertex, self.get_neighbour(vertex))]
        while working_stack:
            v, gen = working_stack.pop()
            visited[v] = True
            continue_flag = True
            while continue_flag:
                neighbour = next(gen, None)
                if neighbour is None:
                    stack.append(v)
                    continue_flag = False
                    continue
                if not visited[neighbour]:
                    working_stack.append((v, gen))
                    working_stack.append((neighbour, self.get_neighbour(neighbour)))
                    continue_flag = False
                    continue

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