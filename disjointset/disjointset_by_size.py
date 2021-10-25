

class Disjointset:
    parent = {}
    size = {}

    def makeset(self, universe):
        for each in universe:
            self.parent[each] = each
            self.size[each] = 1

    def find(self, x):
        if self.parent[x] == x:
            return self.parent[x]
        return self.find(self.parent[x])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        xrank = self.size[xroot]
        yrank = self.size[yroot]
        if xrank < yrank:
            self.parent[xroot] = yroot
            self.size[yroot] += xrank
        elif xrank > yrank:
            self.parent[yroot] = xroot
            self.size[xroot] += yrank
        else:
            self.parent[xroot] = yroot
            self.size[xroot] += yrank

def printset(universe, ds):
    print([ds.find(each) for each in universe])

if __name__ == "__main__":

    universe = [1,2,3,4,5]
    ds = Disjointset()
    ds.makeset(universe)
    printset(universe, ds)

    ds.union(4,3)
    printset(universe, ds)

    ds.union(1,2)
    printset(universe, ds)

    ds.union(1,3)
    printset(universe, ds)