"""
unbounded knapsack
M(i, j) = {0 if i,j= 0
           M(i-1, j) if i > j
           min(M(i-1,j), M(i, j-coin[i]) if i <= j
"""

def recursive(coins, i, j):
    #print(coins, i, j)
    if i<=0 or j <= 0:
        return float("inf")-1
    if i != 0 and j == 0:
        return 0
    if i == 1 and j != 0:
        if coins[i]%j == 0:
            return coins[i]//j
        else:
            return float("inf")
    if coins[i-1] > j:
        return recursive(coins, i-1, j)
    else:
        return min(1+recursive(coins, i, j-coins[i-1]), recursive(coins, i-1, j))

def top_down(coins, i, j , mem):
    #print(i,j, mem)
    if (i <= 0 or j <= 0) :
        mem[(i,j)] = float("inf")-1
        return float("inf")-1
    if (i > 0 and j == 0):
        return 0
    if mem.get((i,j)) is not None:
        return mem.get((i,j))
    if i == 1 and j != 0:
        if coins[i] %j == 0:
            return coins[i]//j
        else:
            return float("inf")
    if coins[i-1] > j:
        mem[(i,j)] = top_down(coins,i-1, j, mem)
    else:
        mem[(i,j)] = min(1+top_down(coins, i, j-coins[i], mem),
                         top_down(coins, i-1, j, mem))
    return mem[(i,j)]

def bottom_up(coins, i, j):
    output = [[-1 for _ in range(j+1)] for _ in range(i+1)]
    for i in range(0, i+1):
        for j in range(0, j+1):
            if i == 0:
                output[i][j] = float("inf")-1
            elif j == 0 and i != 0:
                output[i][j] = 0
    for i in range(1, i+1):
        for j in range(1, j+1):
            if coins[i-1] > j:
                output[i][j] = output[i-1][j]
            else:
                output[i][j] = min(1+output[i][j-coins[i-1]], output[i-1][j])
    #print(output)
    return output[i][j]
if __name__ == "__main__":
    arr = [1,5,10, 25]
    amount = 30
    ans = recursive(arr, len(arr), amount)
    print( -1 if ans == float("inf") else ans)
    second = top_down(arr, len(arr)-1, amount, {})
    print(second if second != float("inf") else -1)

    print(bottom_up(arr, len(arr)-1, amount))