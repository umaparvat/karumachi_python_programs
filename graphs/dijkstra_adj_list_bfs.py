from collections import deque

def find_shortest(V, adj, Src):
    """
    complexity: O(V+E) -> it's a bfs approach
    :param V:
    :param adj:
    :param Src:
    :return:
    """
    dist = [float("inf")] *V
    dist[Src] = 0
    queue = deque()
    queue.append(Src)
    while queue:
        cur = queue.popleft()
        for friend, weight in adj[cur]:
            if dist[cur]+weight < dist[friend]:
                dist[friend] = dist[cur]+weight
                queue.append(friend)

    print(f"distrance from source {Src} to all vertices:", dist)


if __name__ == "__main__":
    V = 9
    adj = {0: [(1,4), (7,8)],
           1: [(2,8), (7,11)],
           2: [(3,7),(5,4), (8,2)],
           3: [(4,9), (5,14)],
           4: [(5,10)],
           5: [(6,2)],
           6: [(7,1), (8,6)],
           7: [(8,7)],
           8:[],}

    find_shortest(9, adj, 0)
