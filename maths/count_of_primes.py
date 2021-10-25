class Solution:
    def countPrimes(self, n: int) -> int:
        n -= 1 # prime numbers that are strictly less than n.
        if n < 2:
            return 0
        r = int(n ** 0.5)
        V = [n//d for d in range(1, r + 1)]
        print(r, V)
        V += list(range(V[-1] - 1, 0, -1))
        print("after range", V)
        S = {v: v - 1 for v in V}
        print("s", S)
        for p in range(2, r + 1):
            if S[p] == S[p - 1]:
                continue
            p2 = p * p
            sp_1 = S[p - 1]
            for v in V:
                if v < p2:
                    break
                S[v] -= S[v//p] - sp_1
                print(p, sp_1,v, S[v])
        return S[n]


if __name__ == "__main__":
    Solution().countPrimes(15)