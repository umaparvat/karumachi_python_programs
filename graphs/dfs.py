"""
complexity: O(|E|+|v|)
space : O(V)
"""

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    for each in graph[node]:
        if each not in visited:
            dfs(graph, each, visited)
    return visited

if __name__ == "__main__":
    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])}

    dfs(graph, '0')