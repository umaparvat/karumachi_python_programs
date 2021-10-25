
class DST:
    parent = {}
    diameter = {}
    child = {}

    def makeset(self, n):
        for each in range(1,n+1):
            self.parent[each] = each
            self.diameter[each] = 200
            self.child[each] = False

    def find(self, x, m=200):
        if self.parent[x] != x:
            self.parent[x], m = self.find(self.parent[x], min(m,self.diameter[self.parent[x]]))
        return self.parent[x], min(m, self.diameter[self.parent[x]])



    def union(self, source, dest):
        xroot, xdia = self.find(source, self.diameter[source])
        yroot, ydia = self.find(dest, self.diameter[dest])
        self.parent[yroot] = xroot
        self.diameter[dest] = min(xdia, ydia)




def main():
    n = 9
    p = 6
    a = [7, 5, 4, 2, 9 , 3]
    b = [4, 9, 6, 8, 7, 1]
    d = [98, 72, 10, 22, 17, 66]
    ds = DST()
    ds.makeset(n)
    for i in range(p):
        source, dest, diameter = a[i], b[i], d[i]
        ds.child[source] = True
        ds.parent[dest] = source
        ds.diameter[dest] = diameter
    print(ds.parent)
    for i in range(1, n+1):
        ds.union(ds.parent[i], i)
    print(ds.parent, "now\n", ds.diameter, "\n", ds.child)
    ans = []
    tap = 0
    tank = 0
    for i in range(1,n+1):
        if ds.parent[i] == i:
            tank +=1
        elif ds.child[i] is False:
            tap += 1
            ans.append((ds.parent[i], i, ds.diameter[i]))
    ans.sort(key= lambda x: x[0])
    print(ans)






if __name__ == "__main__":
    main()



