# User function Template for python3

class Solution:

    ##Complete this function
    # Function to swap odd and even bits.
    def swapBits(self, n):
        # Your code here
        bin_list = list(bin(n).replace('0b', '').zfill(8))
        print(bin_list)
        even = both = False
        if bin_list.count('1') == bin_list.count('0'):
            both = True
        else:
            even = False
        if even or both:
            for i in range(1, len(bin_list) - 1):
                if i % 2 == 0:
                    bin_list[i], bin_list[i + 1] = bin_list[i + 1], bin_list[i]
        print(bin_list)

        if not even or both:
            for i in range(1, len(bin_list)):
                if i%2 != 0:
                    bin_list[i-1], bin_list[i] = bin_list[i], bin_list[i-1]
        print(bin_list)
        return int("".join(bin_list), 2)


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        ob = Solution()
        print(ob.swapBits(n))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends