"""
either consider the item or not condiser it
M(i, j) = { 0 if i, j = 0
            max(M(i-1,j), value[j]+M(i-1, j-W)) if i,j 1= 0

"""

def recursive(vaulearr, wtarr, i, j):
    if i <= 0 or j <= 0:
        return 0
    if wtarr[i-1] > j:
        return recursive(vaulearr, wtarr, i-1, j)
    else:
        return max(vaulearr[i-1]+ recursive(vaulearr, wtarr, i-1, j-wtarr[i-1]),
                     recursive(vaulearr, wtarr, i-1, j))


def top_down(valuearr, wtarr, i, j, mem):
    if i <= 0 or j <= 0:
        return 0
    if mem.get((i, j)) is not None:
        return mem.get(i,j)
    if wtarr[i-1] > j:
        mem[(i,j)] = top_down(valuearr, wtarr, i-1, j, mem)
        return mem[(i,j)]
    else:
        mem[(i,j)] = max(valuearr[i-1] + top_down(valuearr, wtarr, i-1, j-wtarr[i-1], mem),
                         top_down(valuearr, wtarr, i-1, j, mem))
        return mem[(i,j)]

def bottom_up(valuearr, wtarr, i, j):
    output = [[0 for _ in range(j+1)] for _ in range(i+1)]
    for i in range(i+1):
        for j in range(j+1):
            if i == 0:
                output[i][j] = 0
            elif j == 0:
                output[i][j] = 0
            else:
                if wtarr[i-1] > j:
                    output[i][j] = output[i-1][j]
                else:
                    output[i][j] = max(valuearr[i-1]+ output[i-1][j-wtarr[i-1]], output[i-1][j])
    return output[i][j]


if __name__ == "__main__":
    valuearr = [60, 100, 120]
    wtarr = [10,20, 30]
    W = 50
    print(recursive(valuearr, wtarr, len(valuearr), W))
    print(top_down(valuearr, wtarr,len(valuearr), W, {0:0}))
    print(bottom_up(valuearr, wtarr, len(valuearr), W))
