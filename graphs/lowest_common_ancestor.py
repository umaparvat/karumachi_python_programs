from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.parents = defaultdict(list)
        self.depth = [1]*vertices

    def addEdge(self, src, dest):
        """time complexity
        O(E*(v+E)) => O(VE)
        """
        self.graph[src].append(dest)
        self.parents[dest].append(src)
        if self._iscyclic():
            self.graph[src].remove(dest)
            self.parents[dest].remove(src)
            return

        self._incrementNodeDepth(dest, self.depth[src])

    def _iscyclic(self):
        visited = [False] * self.V
        recstack = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self._iscyclicutil(i, visited, recstack):
                    return True
        return False

    def _iscyclicutil(self, vertex, visited, recstack):
        visited[vertex] = True
        recstack[vertex] = True

        for neighbour in self.graph[vertex]:
            if not visited[neighbour]:
                if self._iscyclicutil(neighbour, visited, recstack):
                    return True
            elif recstack[neighbour]:
                return True

        recstack[vertex] = False
        return False

    def _incrementNodeDepth(self, node, inc):
        flag = False
        if self.depth[node] < inc+1:
            self.depth[node] = inc+1
            flag = True

        queue = [node]
        parent = node
        while queue:
            parent = queue.pop(0)
            children = self.graph[parent]
            for child in children:
                if flag:
                    self.depth[child] = self.depth[parent]+1
                    queue.append(child)

    def getDepth(self, node):
        return self.depth[node]

    def hasDirectPathto(self, src, dest):
        if dest in self.graph[src]:
            return True
        return False

    def _getParentsOf(self, val):
        queue = [val]
        parents = []
        while queue:
            cur = queue.pop(0)
            for each in self.parents.get(cur, []):
                if each not in parents:
                    parents.append(each)
                    queue.append(each)
        return parents


    def lca(self, val_1, val_2):
        """
        O(V+E)
        :param val_1:
        :param val_2:
        :return:
        """
        if not self.graph:
            return None
        if val_1 not in self.graph or val_2 not in self.graph:
            return None
        if val_1 == val_2:
            return val_1

        parent1 = self._getParentsOf(val_1)
        parent2 = self._getParentsOf(val_2)
        print("parents", parent1, parent2)
        common_anscetor = set(parent1) - (set(parent1)- set(parent2))
        common_anscetor = list(common_anscetor)

        if not common_anscetor:
            return None
        deepest = common_anscetor[0]
        print("common", common_anscetor)
        print("depth", self.depth)
        for i in range(1, len(common_anscetor)):
            if self.depth[common_anscetor[i]] > self.depth[deepest]:
                deepest = common_anscetor[i]

        return deepest


if __name__ == "__main__":
    gr = Graph(6)
    gr.addEdge(0,1)
    gr.addEdge(1,2)
    gr.addEdge(1,3)
    gr.addEdge(1,4)
    gr.addEdge(1,5)
    gr.addEdge(2,3)
    gr.addEdge(2,4)
    gr.addEdge(4,5)
    # print("lca (2,5)", gr.lca(2,5))
    # print("lca (1,2)", gr.lca(1,2))
    print("lca (5,3)", gr.lca(5,3))
    #print("lca (3,4)", gr.lca(3,4))





