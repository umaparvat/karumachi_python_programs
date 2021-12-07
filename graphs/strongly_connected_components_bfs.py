from collections import deque, defaultdict

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def transpose(self):
        gr = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                gr.graph[v].append(u)
        return gr.graph

    def bfsutil(self, v, visited, graph):
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            u = queue.popleft()
            for neighbhor in graph[u]:
                if visited[neighbhor] is False:
                    visited[neighbhor] = True
                    queue.append(neighbhor)
        return visited

    def isSc(self):
        """
        two times BFS traversal
        Kosaraju's BFS strongly connected components algorithm
        O(V+E)
        :return:
        """
        visited = [False] * self.V
        v = 0
        bfs_visited = self.bfsutil(v, visited, self.graph)
        if any(each == False for each in visited):
            return False
        gr = self.transpose()
        visited = [False] * self.V
        gr_visited = self.bfsutil(v, visited, gr)
        if any(each == False for each in visited):
            return False
        return True



if __name__ == "__main__":
    """
     0 -> 1-> 2  ->  3
     ^        ^     /
     \        ||   /
      \       4   /
       \_ _ _ ___/
       
    transpose
     0 <- 1 <- 2 <- 3
     |         ^    ^ 
     |         |    |
     |         v    |
     |         4    |
     |______________|
     
    """
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(2, 4)
    g.add_edge(4, 2)
    print(g.isSc())


