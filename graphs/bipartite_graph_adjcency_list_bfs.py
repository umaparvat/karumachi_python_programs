from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.gr = defaultdict(list)

    def addEdge(self, src, dest):
        self.gr[src].append(dest)

    def is_bipartite(self):
        colors = [-1]* self.V
        queue = []
        for i in range(self.V):
            if colors[i] == -1:
                colors[i] = 0
                queue.append([i, 0])
                while queue:
                    cur, colr = queue.pop(0)
                    for neighbours in self.gr[cur]:
                        if colors[neighbours] == -1:
                            now_clr = None
                            if colr == 1:
                                now_clr = 0
                            else:
                                now_clr = 1
                            colors[neighbours] = now_clr
                            queue.append([neighbours, now_clr])

                        elif colors[neighbours] == colr:
                            return  False
        return True


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(1,3)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(0,2)
    print(g.is_bipartite())