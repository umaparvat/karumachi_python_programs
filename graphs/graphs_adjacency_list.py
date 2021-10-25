"""
adjacency list
O(|E|+|v|)
"""

class AdjacentNode:
    def __init__(self, value):
        self.vertex = value
        self.next  = None

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = [None] * vertex

    def add_edge(self, source, destination):
        node = AdjacentNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node


        node = AdjacentNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node


    def remove_edge(self, source, destination):
        temp = self.graph[source]
        prev = None
        if not temp:
            return
        while temp and temp.vertex != destination:
            prev = temp
            temp = temp.next
        print("rem", temp.vertex)
        if temp.vertex == destination:
            if prev:
                prev.next = temp.next
            else:
                self.graph[source] = temp.next
            del temp
        temp = self.graph[destination]
        prev = None
        if not temp:
            return
        while temp and temp.vertex != source:
            prev = temp
            temp = temp.next
        if temp.vertex == source:
            if prev:
                prev.next = temp.next
            else:
                self.graph[destination] = temp.next
            del temp

    def print_graph(self):
        for i in range(self.V):
            print(f"vertex: {str(i)}: ", end="")
            temp = self.graph[i]
            while temp:
                print(f"-> {temp.vertex}", end="")
                temp = temp.next
            print("\n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_graph()
    graph.remove_edge(0,2)
    graph.remove_edge(0,3)
    graph.remove_edge(0,1)
    print("after removal")
    graph.print_graph()