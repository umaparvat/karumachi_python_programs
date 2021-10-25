

class DSU:
    parent = {}

    def makeset(self, n):
        for i in range(1, n+1):
            self.parent[i] = i

    def find_set(self, x):
        if not self.parent.get(x):
            return x
        if self.parent[x] == x:
            return x
        return self.find_set(self.parent[x])




def main():
    n = 10
    q = 5
    a = [[3,9,13], [1,4,9], [2,10,14], [2,7,10], [6,9,44]]
    ds = DSU()
    ds.makeset(n)
    ans = [0]*(n+1)
    while q:
        l, r, c = a[q-1]
        q -= 1
        v = ds.find_set(l)
        while v <= r:
            ans[v] = c
            ds.parent[v] = v+1
            v = ds.find_set(v)
        print("after l, r, c", l,r,c, "\n", ds.parent, "\n", ans)

    for i in range(1, n+1):
        print(ans[i])


if __name__ == "__main__":
    main()


