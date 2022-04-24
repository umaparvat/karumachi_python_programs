class Solution:
    def transfigure(self, A, B):
        # code here
        # code here
        in_dc = {}
        al = len(A)
        bl = len(B)
        if al != bl:
            return -1
        total = 0
        for i in range(al):
            total += ord(A[i])
            total -= ord(B[i])
        print(total, A, B)
        if total != 0:
            return -1
        i = al-1
        j = bl-1
        shifts = 0
        while i >= 0 and j >= 0:
            if A[i] == B[j]:
                i -= 1
                j -= 1
            else:
                i = i-1
                shifts += 1
        return shifts


if __name__ == "__main__":
    A = "GEEKSFORGEEKS"
    B = "FORGEEKSGEEKS"
    s = Solution()
    print(s.transfigure(A, B))
    A = "ABC"
    B = "BCA"
    print(s.transfigure(A, B))
    A = "AB"
    B = "BD"
    print(s.transfigure(A,B))