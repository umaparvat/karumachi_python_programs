
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node(data={self.data}, left={self.left}, right={self.right}"

def buildtree(arr):
    n = len(arr)
    seg = [0]*2*(n)
    for i in range(n):
        ind = n+i
        print(ind, len(seg))
        if ind < len(seg):
            seg[ind] = arr[i]
            print(seg[ind])
    print(seg)
    for i in range(n-1, -1, -1):
        seg[i] = seg[2*i] + seg[2*i+1]
    print(seg)

def buildtree_recur(arr, start, end):
    if start == end:
        return Node(arr[start])
    mid = start + (end-start)//2
    left = buildtree_recur(arr, start, mid)
    right = buildtree_recur(arr, mid+1, end)
    n = Node(data=0)
    n.data = left.data + right.data
    n.left = left
    n.right = right
    return n

def main():
    arr = [1,3,-2,8, -7]
    buildtree(arr)
    root = buildtree_recur(arr, 0, len(arr)-1)
    print(root)

if __name__ == "__main__":
    main()