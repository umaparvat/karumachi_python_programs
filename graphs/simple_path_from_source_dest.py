"""
Graph is adjacent matrix
find path from source to dest
"""

def findpath(src, dest, g, output):
    """
    space complexity: O(v) excluding stack space
    time complexity ;O(E)
    :param src:
    :param dest:
    :param g:
    :param output:
    :return:
    """
    output += [src]
    if src == dest:
        return output
    for ind, neighbour in enumerate(graph[src]):
        if neighbour != 0 and ind not in output:
            res = findpath(ind, dest, g, output)
            if res:
                return res

    return None


def bfs(src, dest, graph):
    output = []
    queue = [src]
    while queue:
        node = queue.pop(0)
        output += [node]
        if node == dest:
            return output
        for ind, neighbour in enumerate(graph[node]):
            if neighbour != 0 and ind not in output:
                queue.append(ind)
    return None


if __name__ == "__main__":
    graph = [[0,1,1,0,0,0],
             [0,0,0,1,1,0],
             [0,0,0,1,1,0],
             [0,0,0,0,1,0],
             [1,0,0,0,0,0],
             [0,0,0,0,0,0]]

    print(findpath(0,4, graph, []))
    print(findpath(0,5, graph, []))
    print("in bfs")
    print(bfs(0, 4, graph))
    print(bfs(0, 5, graph))
