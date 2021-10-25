from collections import deque

"""
Time complexity: O(v+ E)
space complexity: O(V)
"""

def bfs(graph, node):
    visited, queue = set(), deque([node])
    visited.add(node)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)