

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[999 for _ in range(vertices)] for _ in range(vertices)]
        self.edges = []
    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = -weight
        self.graph[dest][src] = -weight
        self.edges.append([src, dest, -weight])

    def find(self, vertex, parent):
        if parent[vertex] == vertex:
            return parent[vertex]
        return self.find(parent[vertex], parent)

    def union(self, x, y, parent, rank):
        xroot = self.find(x, parent)
        yroot = self.find(y, parent)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot

        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1



    def kruskal(self):
        parent = []
        rank = []
        mst = []
        for i in range(self.V):
            parent.append(i)
            rank.append(0)
        self.edges.sort(key=lambda x: x[2])
        i = e = 0
        while e < self.V -1:
            u,v, w = self.edges[i]
            i = i+1
            x = self.find(u, parent)
            y = self.find(v, parent)
            if x != y:
                self.union(x,y, parent, rank)
                mst.append([u,v,-w])
                e = e+1
        for each in mst:
            print(each)


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0,1, -1)
    g.add_edge(0,3,1)
    g.add_edge(0,2,3)
    g.add_edge(1,3,2)
    g.add_edge(1,2,1)
    g.add_edge(2,3,1)
    g.kruskal()