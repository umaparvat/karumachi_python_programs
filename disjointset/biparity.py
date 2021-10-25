

parent = {}
rank = {}
biparity = {}
class Pair:

    def __init__(self, first, second):
        self.first  = first
        self.second = second


def make_set(n):
    for each in range(1, n+1):
        parent[each] = Pair(each, 0)
        rank[each] = 0
        biparity[each] = True

def find_set(x):
    if parent[x].first != x:
        parity = parent[x].second
        parent[x] = find_set(parent[x].first)
        parent[x].second ^= parity
    return parent[x]



def add_edge(a,b):
    pa = find_set(a)
    pb = find_set(b)
    a = pa.first
    x = pa.second
    b = pb.first
    y = pb.second
    if a == b:
        if x == y:
            biparity[a] = False
    else:
        if rank[a] < rank[b]:
            parent[a] = Pair(b, x^y^1)
            biparity[b] &= biparity[a]
        elif rank[a] > rank[b]:
            parent[b] = Pair(a, x^y^1)
            biparity[a] &= biparity[b]
        if rank[a] == rank[b]:
            rank[a] += 1

def is_biparity(v):
    return biparity[find_set(v).first]


def main():
    n = 10
    make_set(10)
    questions = 5
    query = [[1,2, "even"],[3,4,"odd"],[5,6,"even"],[1,6, "even"],[7,10, "odd"]]
    index = 0
    while questions:
        a,b, c = query[index]
        index += 1
        questions -= 1
        add_edge(a,b)
        print(is_biparity(a), is_biparity(b))

if __name__ == "__main__":
    main()




