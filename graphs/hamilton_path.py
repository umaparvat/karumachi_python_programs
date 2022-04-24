from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def hamilton(self, v, visited, path, n):
        if len(path) == n:
            print(path)
            return
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                visited[neighbour] = True
                path.append(neighbour)
                self.hamilton(neighbour, visited, path, n)
                visited[neighbour] = False
                path.pop()

    def get_paths(self):
        """
        time complexity: exponential
        :return:
        """

        for i in range(self.V):
            visited = [False] * self.V
            visited[i] = True
            path = []
            path.append(i)
            self.hamilton(i, visited, path, self.V)


if __name__ == "__main__":

    gr = Graph(4)
    gr.addEdge(0,1)
    gr.addEdge(0,2)
    gr.addEdge(0,3)
    gr.addEdge(1,2)
    gr.addEdge(1,3)
    gr.addEdge(2,3)
    gr.get_paths()