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
        return [output]
    paths = []
    for ind, neighbour in enumerate(graph[src]):
        if neighbour != 0 and ind not in output:
            res = findpath(ind, dest, g, output)
            paths += res

    return paths

if __name__ == "__main__":
    graph = [[0,1,1,0,0,0],
             [0,0,0,1,1,0],
             [0,0,0,1,1,0],
             [0,0,0,0,1,0],
             [1,0,0,0,0,0],
             [0,0,0,0,0,0]]

    print(findpath(0,4, graph, []))
    print(findpath(0,5, graph, []))