from collections import defaultdict
import sys

class Minheap:
    def __init__(self):
        self.pq = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, distance):
        newNode = [v, distance]
        return newNode

    def swap(self, a, b):
        self.pq[a], self.pq[b] = self.pq[b], self.pq[a]

    def left(self, idx):
        return (2*idx)+ 1

    def right(self, idx):
        return (2*idx) + 2

    def minheapify(self, idx):
         smallest = idx
         left = self.left(idx)
         right = self.right(idx)
         if left < self.size and self.pq[left][1] < self.pq[smallest][1]:
             smallest = left
         if right < self.size and self.pq[right][1] < self.pq[smallest][1]:
            smallest = right
         if idx != smallest:
             self.pos[self.pq[idx][0]], self.pos[self.pq[smallest][0]] = self.pos[self.pq[smallest][0]], self.pos[self.pq[idx][0]]
             self.swap(idx, smallest)
             self.minheapify(smallest)

    def get_min(self):
        if not self.pq:
            return
        root = self.pq[0]
        last = self.pq[-1]
        self.pq[0] = self.pq[-1]
        self.pos[last[0]] = 0
        self.pos[root[0]] = self.size -1
        self.size -= 1
        self.minheapify(0)
        return root
    def isEmpty(self):
        return self.size == 0
    def decreaseKey(self, v, dist):
        indx = self.pos[v]
        self.pq[indx][1] = dist
        while indx > 0 and self.pq[indx][1] < self.pq[(indx-1)//2][1]:
            self.pos[self.pq[indx][0]], \
            self.pos[self.pq[(indx-1)//2][0]] = self.pos[self.pq[(indx-1)//2][0]], \
                                                self.pos[self.pq[indx][0]]
            self.swap(indx, (indx-1)//2)
            indx = (indx-1)//2

    def isInheap(self, v):
        return  self.pos[v] < self.size

    def printheap(self, dist, n):
        print("Vertex\tDistance from source")
        for i in range(n):
            print("%d\t\t%d" % (i, dist[i]))

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, source, destination, weight):
        newnode = [destination, weight]
        self.graph[source].insert(0, newnode)
        newnode = [source, weight]
        self.graph[destination].insert(0, newnode)

    def dijkstra(self, src):
        V = self.V
        distance = []
        minheap = Minheap()
        for v in range(V):
            distance.append(sys.maxsize)
            minheap.pq.append(minheap.newMinHeapNode(v, distance[v]))
            minheap.pos.append(v)
        minheap.pos[src] = src
        distance[src] = 0
        minheap.decreaseKey(src, distance[src])

        minheap.size = V
        while minheap.isEmpty() == False:
            #extract minheap
            minnode = minheap.get_min()
            u =minnode[0]
            for adjacent in self.graph[u]:
                v = adjacent[0]
                if distance[u] != sys.maxsize and minheap.isInheap(v) and distance[u]+adjacent[1] < distance[v]:
                    distance[v] = distance[u]+adjacent[1]
                    minheap.decreaseKey(v, distance[v])

        minheap.printheap(distance, V)


if __name__ == "__main__":
    graph = Graph(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)
    graph.dijkstra(0)





