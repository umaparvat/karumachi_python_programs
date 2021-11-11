

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u,v, w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, a, b, parent, rank):
        xroot = self.find(parent, a)
        yroot = self.find(parent, b)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            rank[xroot] += 1
            parent[yroot] = xroot

    def kruskal(self):
        """
        O(Elog E)
        :return:
        """
        result = []
        e = i= 0
        self.graph.sort(key=lambda x:x[2])
        parent = []
        rank = []
        for i in range(self.V):
            parent.append(i)
            rank.append(0)

        while e < self.V -1:
            u,v,w = self.graph[i]
            i = i+1
            x= self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append([u,v,w])
                self.union(x, y, parent, rank)
                e += 1
        for u, v, w in result:
            print("%d - %d: %d" % (u, v, w))

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 0, 4)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 2, 3)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 2, 4)
    g.add_edge(4, 3, 3)
    g.add_edge(5, 2, 2)
    g.add_edge(5, 4, 3)
    g.kruskal()


