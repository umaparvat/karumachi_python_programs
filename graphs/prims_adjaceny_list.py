from collections import defaultdict

class MinHeap:
    def __init__(self):
        self.arr = []
        self.pos = []
        self.size = 0

    def left(self, index):
        return (2*index)+1

    def right(self, index):
        return (2*index)+2

    def __len__(self):
        return self.size

    def swap(self, a, b):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]

    def swap_pos(self, a, b):
        self.pos[self.arr[a][0]], self.pos[self.arr[b][0]] = self.pos[self.arr[b][0]], self.pos[self.arr[a][0]]

    def heapify(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)
        if left < self.size and self.arr[smallest][1]> self.arr[left][1]:
            smallest = left
        if right < self.size and self.arr[smallest][1] > self.arr[right][1]:
            smallest = right
        if smallest != index:
            self.swap_pos(index, smallest)
            self.swap(index, smallest)
            self.heapify(smallest)

    def get_min(self):
        if not self.arr:
            return
        root = self.arr[0]
        last = self.arr[-1]
        self.arr[0] = last
        self.arr[-1] = root
        self.pos[root[0]] = self.size -1
        self.pos[last[0]] = 0
        self.size -= 1
        self.heapify(0)
        return root

    def is_empty(self):
        return self.size == 0

    def decreaseKey(self, vertex, distance):
        index = self.pos[vertex]
        self.arr[index][1] = distance
        while index > 0 and self.arr[index][1] < self.arr[(index-1)//2][1]:
            self.swap_pos(index, (index-1)//2)
            self.swap(index, (index-1)//2)
            index = (index-1)//2

    def isInheap(self, v):
        return  self.pos[v] < self.size

    def printheap(self, parent, n):
        print("Vertex\tDistance from source")
        for i in range(1, n):
            print("%d\t\t%d" % (parent[i], i))


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, source, dest, distance):
        newnode = [dest, distance]
        self.graph[source].insert(0, newnode)
        newnode = [source, distance]
        self.graph[dest].insert(0, newnode)

    def prim(self):
        V = self.V
        key = []
        parent = []
        minheap = MinHeap()
        for ind in range(V):
            parent.append(-1)
            key.append(float("inf"))
            minheap.arr.append([ind, key[ind]])
            minheap.pos.append(ind)
        key[0] = 0
        minheap.pos[0] = 0
        minheap.decreaseKey(0, key[0])
        minheap.size = V

        while minheap.is_empty() == False:
            minNode = minheap.get_min()
            u = minNode[0]
            for neighbour in self.graph[u]:
                v = neighbour[0]
                if minheap.isInheap(v) and neighbour[1] < key[v]:
                    key[v] = neighbour[1]
                    parent[v] = u
                    minheap.decreaseKey(v, key[v])

        print(parent)
        minheap.printheap(parent, V)


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
    graph.prim()


