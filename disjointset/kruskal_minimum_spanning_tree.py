

class DST:
    parent = {}
    size = {}

    def makeset(self, n):
        for index in range(n):
            self.parent[index] = index
            self.size[index] = 1

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        xweight = self.size[xroot]
        yweight = self.size[yroot]
        if xweight < yweight:
            self.parent[xroot] = yroot
            self.size[yroot] += xweight
        else:
            self.parent[yroot] = xroot
            self.size[xroot] += yweight



def kruskal(edges, N):
    MST = []
    ds = DST()
    ds.makeset(N)
    edges.sort(key=lambda x: x[2])
    index = 0
    while len(MST) != N-1:
        source, dest, weight = edges[index]
        index += 1
        x = ds.find(source)
        y = ds.find(dest)
        if x != y:
            MST.append((source, dest, weight))
            ds.union(x,y)
    return MST


if __name__ == "__main__":
    # `(u, v, w)` Triplet represent undirected edge from
    # vertex `u` to vertex `v` having weight `w`
    edges = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]

    # total number of nodes in the graph
    N = 7

    # construct graph
    e = kruskal(edges, N)

    print(e)

