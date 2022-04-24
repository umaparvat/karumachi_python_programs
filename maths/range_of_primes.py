def primeRange(M, N):
    # code here
    out = [1] * (N)
    for i in range(2, N):
        for j in range(i, N):
            print(f"{i}*{j}={i*j}")
            val = i * j
            if val < N:
                out[val] = 0
            else:
                break
    res = []
    for i in range(2, N):
        if out[i]:
            res.append(i)
    return res

if __name__ == "__main__":
    print(primeRange(1, 10))