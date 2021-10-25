num, query = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
tree = [0] * 2 * num


def buildtree(index, arr, start, end):
    if start == end:
        tree[index] = arr[start]
    else:
        mid = start + (end - start) // 2
        buildtree(2 * index, arr, start, mid)
        buildtree(2 * index + 1, arr, mid + 1, end)
        tree[index] = min(tree[2 * index], tree[2 * index + 1])

def updatetree(index, arr, start, end, s_index, value):
    if start == end:
        arr[s_index] = value
        tree[index] = value
    else:
        mid =start + (end-start)//2
        if s_index <= mid:
            updatetree(2*index, arr, start, mid, s_index, value)
        else:
            updatetree(2*index+1, arr, mid+1, end, s_index, value)
        tree[index] = tree[2*index]+ tree[2*index+1]


def querytree(index, arr, start, end, l, r):
    if r < start or end < l:
        return float("inf")
    if l <= start and r >= end:
        return tree[index]
    mid = start + (end - start) // 2
    p1 = querytree(2 * index, arr, start, mid, l, r)
    p2 = querytree(2 * index + 1, arr, mid + 1, end, l, r)
    return min(p1, p2)


buildtree(1, arr, 0, num - 1)
print(tree)
while query:
    l, r = map(int, input().split(" ")[1::])
    print(querytree(1, arr, 0, num - 1, l - 1, r - 1))
    query -= 1
