

class DST:
    parent = {}
    def __init__(self, universe=None):
        if universe:
            self.makeset(universe)

    def makeset(self, val_list):
        for each in val_list:
            self.parent[each] = each

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.parent[xroot] = yroot


def printset(universe, ds):
    print([ds.find(each) for each in universe])

if __name__ == "__main__":
    universe = [1,2,3,4,5]
    ds = DST(universe)
    printset(universe, ds)
    ds.union(3,4)
    printset(universe, ds)
    ds.union(1,2)
    printset(universe, ds)
    ds.union(1,3)
    printset(universe, ds)
