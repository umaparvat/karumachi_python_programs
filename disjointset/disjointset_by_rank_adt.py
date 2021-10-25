"""
union by height is rank
"""

class DisjointSet:
    parent = {}
    rank = {}

    def makeset(self, universe):
        for each in universe:
            self.parent[each] = each
            self.rank[each] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1


def printset(universe, ds):
    print([ds.find(each) for each in universe])

if __name__ == "__main__":

    universe = [1,2,3,4,5]
    ds = DisjointSet()
    ds.makeset(universe)
    printset(universe, ds)

    ds.union(4,3)
    printset(universe, ds)

    ds.union(1,2)
    printset(universe, ds)

    ds.union(1,3)
    printset(universe, ds)
