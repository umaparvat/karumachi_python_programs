# your code goes here
# your code goes here
class DSU:
    parent = {}

    def makeset(self, n):
        for i in range(1, n + 1):
            self.parent[i] = i

    def find_set(self, x):
        if not self.parent.get(x):
            return x
        if self.parent[x] == x:
            return x
        return self.find_set(self.parent[x])


n, q = map(int, input().strip().split())
ds = DSU()
ds.makeset(n)
queries = []
index = 0
ans = [0] * (n + 1)
while index != q:
    l, r, c = map(int, input().strip().split())
    index += 1
    queries.append([l, r, c])

while q:
    l, r, c = queries[q - 1]
    q -= 1
    v = ds.find_set(l)
    while v <= r:
        print("v", v)
        ans[v] = c
        ds.parent[v] = v + 1
        v = ds.find_set(v)
        print(l,r,c, v, "now", ds.parent)

for i in range(1, n + 1):
    print(ans[i])

