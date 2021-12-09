"""
print eulerian circuit in directed graph
    1. all non zero degree vertex should be strongly connected
    2. in degree and out degree each vertex should be same

step
    1. start at any vertex and make note of vertex(current)
    2. move on it's one of the edge.
    3. if it's stuck at any vertex(which has no unvisited edge), move that vertex to circuit
        .and  backtrack to previous vertex(u) and search for any unvisisted vertex and travel until it
        reach back to the same vertex(u).
    4. join the circuit with vertex with current(in reverse order).
    5. that will be the eulerian circuit
"""
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.indegree = [0]*vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[u]+=1

    def removeEdge(self, u, v):
        for ind, each in enumerate(self.graph[u]):
            if each == v:
                self.graph[u].pop(ind)
                if self.indegree[u] != 0:
                    self.indegree[u] -= 1

    def print_circuit(self, v, current, circuit):
        if len(self.graph[v]) == 0:
            circuit.append(v)
            if current:
                v = current.pop()
                self.print_circuit(v, current, circuit)
            else:
                circuit.reverse()
                return

        else:
            current.append(v)
            neighbour = self.graph[v].pop()
            self.print_circuit(neighbour, current, circuit)

    def print_eulerian(self):
        """
        O(v+E) time complexity
        :return:
        """
        v = 0
        circuit = []
        current = []
        print(self.graph)
        self.print_circuit(v, current, circuit)
        for each in circuit:
            print(each, end=" ")
            if each is not None:
                print("->", end=" ")
        print("\n")

    def print_eulerian_iterative(self):
        """
        time complexity: O(v+E)
        :return:
        """
        v = 0
        current = [v]
        circuit = []
        while len(current):
            if len(self.graph[v]):
                current.append(v)
                neighbour = self.graph[v].pop()
                v = neighbour
            else:
                circuit.append(v)
                if len(current):
                    v = current.pop()
                else:
                    break
        for each in circuit:
            print(each, end="->")
        print("\n")



if __name__ == "__main__":
    g = Graph(3)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,0)
    #g.print_eulerian()
    g.print_eulerian_iterative()

    g1 = Graph(7)
    g1.addEdge(0,1)
    g1.addEdge(0,6)
    g1.addEdge(1,2)
    g1.addEdge(2,0)
    g1.addEdge(2,3)
    g1.addEdge(3,4)
    g1.addEdge(4,2)
    g1.addEdge(4,5)
    g1.addEdge(5,0)
    g1.addEdge(6,4)
    g1.print_eulerian()