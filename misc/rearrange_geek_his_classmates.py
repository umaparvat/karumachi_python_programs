def prank(a, n):
    # code here
    out = [0] * n
    for i in range(n-1, -1, -1):
        val = a[i]
        ind = a.index(i)
        a[ind] = -val

    return a

if __name__ == "__main__":
    a = [0,5,1,2,4,3]
    print(a)
    print(prank(a, 6))