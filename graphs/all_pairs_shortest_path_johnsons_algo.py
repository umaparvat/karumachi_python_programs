"""
1. if the graph has negative weight but not negative cycle
2. add a new node to connect all vertices
3. calculate bellman ford algorithm for the new node( store result in h)
4. remove the new node
5. apply w(u,v) = w(u,v)+h[u] - h[v]
6. apply dijkstra algorithm for all vertices

-> if we use adjancency list -> dijkstra's O(Elogv ) for v times -> O(VElog V)
-> bellman ford -> O(VE)
-> total complexity -> O(VE+V^2 log V) -> for dense graph -> (E= V2) -> O(V^3+V^2log V)
-> for sparse graph(E-> V) -> time compleixty(O(V^2+V^2logV)
"""
from copy import deepcopy

def min_index(distance, visited):
    min_index= None
    minimum = float("inf")
    for i in range(len(distance)):
        if visited[i] is False and distance[i] < minimum:
            min_index = i
            minimum = distance[i]
    return min_index

def dijkstras_ssp(graph, src, modified_graph):
    """
    O(v^2)
    :param graph:
    :param src:
    :return:
    """
    V = len(graph)
    visited = [False] * V
    distance = [float("inf")] * V
    distance[src] = 0
    for _ in range(V):
        u = min_index(distance, visited)
        if u is None:
            continue
        visited[u] = True
        for v in range(V):
            if visited[v] is False and graph[u][v]!= 0 and distance[v] > distance[u]+ modified_graph[u][v]:
                distance[v] = distance[u] + modified_graph[u][v]
    return distance

def bellman_ford(edges, V):
    dist = [float("inf") for _ in range(V)]
    prev = [0 for _ in range(V)]
    dist[0] = 0
    for _ in range(V-1):
        for a,b, c in edges:
            if dist[a] != float("inf") and dist[a]+c < dist[b]:
                dist[b] = dist[a] + c
                prev[b] = a

    for a,b,c in edges:
        if dist[a] != float("inf") and dist[a] + c < dist[b]:
            print("negative cycle found")
            break

    return dist[0:V-1]

def johnsons(graph):
    """
    Bellman Ford is O(VE)
    Dijkstra is O(VLogV).
    So overall time complexity is O(V^(2)*log V + VE).
    :param graph:
    :return:
    """
    vertex = len(graph)
    edges = []
    for i in range(vertex):
        for j in range(vertex):
            if graph[i][j] !=0:
                edges.append([i,j, graph[i][j]])
        edges.append([vertex, i, 0])
    #call bellman_ford
    h = bellman_ford(edges, vertex+1)
    #apply w(u,v) = w(u,v)+h[u]-h[v]
    V = len(graph)
    modified_graph = [[0 for _ in range(V)] for _ in range(V)]
    for u in range(V):
        for v in range(V):
            if graph[u][v] != 0:
                modified_graph[u][v] = graph[u][v] + (h[u]-h[v])

    print(modified_graph)
    output = [[0] * V for _ in range(V)]
    for v in range(V):
        output[v] = dijkstras_ssp(graph, v, modified_graph)
    print(output)


if __name__ == "__main__":
    graph = [[0, -8, 2, 4],
             [0, 0, 2, 6],
             [0, 0, 0, 2],
             [0, 0, 0, 0]]
    johnsons(graph)







