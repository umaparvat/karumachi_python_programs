
class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        if not S:
            return None
        data = S[0]
        rem = self.removeConsecutiveCharacter(S[1::])
        if not rem:
            return data
        if data != rem[0]:
            return data+rem
        else:
            return rem[1::]

    def removeAdjacentDuplicates(self, str):
        stkptr = -1
        i = 0
        size = len(str)
        while i < size:
            if (stkptr == -1 or (str[stkptr] != str[i])):
                stkptr += 1
                str[stkptr] = str[i]
                i += 1
            else:
                while i < size and str[stkptr] == str[i]:
                    i += 1
                    stkptr -= 1
        stkptr += 1
        str = str[0:stkptr]
        print(str)


if __name__ == "__main__":
    print(Solution().removeConsecutiveCharacter("careermonk"))
    print(Solution().removeAdjacentDuplicates(["c","a","r","e","e","r","m","o","n","k"]))
