"""
Topological sort for DAG(Directed Acyclic graph)

it's a iterative method.

1. take a count of indegree for all the nodes
2. enqueue only zero indegree nodes and decrease the indegree by 1
3. traverse the nodes in queue (add the popped node in result)
    and decrease the indegree for it's neighbours.
    whichever neighbour has indegree 0, enqueue the node
    traverse until the queue is empty.
"""
from  collections import defaultdict, deque
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.indegree = defaultdict(int)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    def topologicalsort(self):
        """
        time complexity:O(V+E)
        space complexity: O(V)
        :return:
        """
        queue = deque()
        for v in range(self.V):
            if self.indegree[v] == 0:
                queue.append(v)
                self.indegree[v] -= 1

        res = []
        cnt = 0
        while queue:
            current = queue.popleft()
            res.append(current)
            for neighbour in self.graph[current]:
                self.indegree[neighbour] -= 1
                if self.indegree[neighbour] == 0:
                    queue.append(neighbour)
            cnt += 1

        if cnt != self.V:
            print ("cycle exists")


        print(res)

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.topologicalsort()