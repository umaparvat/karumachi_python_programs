"""
1. in undirected graph
if there is a back edge to the visited node or
    node pointed to itself is cycle.
1. if the node's neighbour is in visited list and it's not parent of that node. it's a cyle

1---0---3
|   |   |
|   |   |
--2--   4

Here 1 - 0 -2 is a cycle
neighbour
0-> 1,2,3
1-> 0, 2
2-> 1, 0
3-> 4

parent
0 -> -1
1-> 0
2-> 1
3-> 0
4->3

when 1 is visted, it's neighbour is 0 and 0 is already visited. parent of 1 is 0, so ignore it.
when 2 is visited it's neighour is 0 ( 0 is already visited and 2's parent is 1 so it's a cycle)

"""
from collections import defaultdict
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def iscycle(self):
        """
        it's a DFS.
        so time complexity: O(V+E)
        space complexity: O(V)
        :return:
        """
        visited = [False] * self.V
        for v in range(self.V):
            if visited[v] is False:
                if self.iscyclicutil(v, visited, -1) is True:
                    return True
        return False

    def iscyclicutil(self, vertex, visited, parent):
        visited[vertex] = True

        for neighbour in self.graph[vertex]:
            if visited[neighbour] is False:
                if self.iscyclicutil(neighbour, visited, vertex) is True:
                    return True
            elif parent != neighbour:
                    return True
        return False


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    if g.iscycle():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")
    g1 = Graph(3)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)

    if g1.iscycle():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")