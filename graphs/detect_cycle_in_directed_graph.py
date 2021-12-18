"""
if there is a back edge in the graph, it has a cycle

0 ----|
| --- 2 <- 1

here 2-> 0 is a cycle

1. track of stack nodes which is being visited.
if a node is already there in stack. it's a back edge


"""
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclic(self):
        """
        if cycle exists, return True
        else return False
        Time complexity: O(V+E)
        space complexity:O(V)
        :return:
        """
        visited = [False]*self.V
        recStack = [False]*self.V

        for v in range(self.V):
            if visited[v] is False:
                if self.iscycle_util(v, visited, recStack) is True:
                    return True
        return False

    def iscycle_util(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for u in self.graph[v]:
            if visited[u] is False:
                if self.iscycle_util(u, visited, recStack) is True:
                    return True
            elif recStack[u] is True:
                return True
        recStack[v] = False
        return False

if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    if g.isCyclic() == 1:
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")