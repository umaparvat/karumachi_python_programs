"""
shortest ancestral bw two vertices in a dag
"""
from collections import defaultdict
from copy import deepcopy
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, w):
        self.graph[src].append((dest, w))

    def toplogysortutil(self, v, visited, stack):
        visited[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour[0]] is False:
                self.toplogysortutil(neighbour[0], visited, stack)

        stack.append(v)

    def iscyclic(self):
        visited =[False] * self.V
        recstack = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.iscyclicutil(i, visited, recstack):
                    return True
        return False

    def iscyclicutil(self, v, visited, recstack):
        visited[v] = True
        recstack[v] = True
        for neighbour,w in self.graph[v]:
            if visited[neighbour] is False:
                if self.iscyclicutil(neighbour, visited, recstack):
                    return True
            elif recstack[neighbour]:
                return True

        recstack[v] = False
        return False

    def ancestral(self, v, w):
        visited = [False] * self.V
        stack = []

        # check no cycle exists
        if self.iscyclic():
            print("cycle exists")
        for i in range(self.V):
            if visited[i] is False:
                self.toplogysortutil(i, visited, stack)

        dist = [float("inf")] * self.V
        dist[v] = 0
        wstack = deepcopy(stack)
        while stack:
            cur = stack.pop()
            for neighbour, w in self.graph[cur]:
                if dist[neighbour] > dist[cur]+w:
                    dist[neighbour] = dist[cur]+w

        wdist = [float("inf")] * self.V
        wdist[w] = 0
        while wstack:
            cur = wstack.pop()
            for neighbour, w in self.graph[cur]:
                if wdist[neighbour] > wdist[cur]+w:
                    wdist[neighbour] = wdist[cur]+w

        print(dist, wdist)
        vpath = []
        for ind, val in enumerate(dist):
            if val != float("inf"):
                vpath.append(ind)

        wpath = []
        for ind, val in enumerate(wdist):
            if val != float("inf"):
                wpath.append(ind)
        print(vpath, wpath)
        common = set(vpath) - (set(vpath)- set(wpath))
        print(common)
        if len(common) != 0:
            output = []
            for each in list(common):
                if each != float("inf"):
                    output.append(each)
            print(output)
            print(output[0])
        return "no ancestor"


if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 3, 6)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 4, 4)
    g.addEdge(2, 5, 2)
    g.addEdge(2, 3, 7)
    g.addEdge(3, 4, -1)
    g.addEdge(4, 5, -2)
    g.ancestral(4, 5)
