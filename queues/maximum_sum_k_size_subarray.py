import os, sys
sys.path.append(os.getcwd())
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here
        i=0
        j=1
        sum = Arr[i]
        m = Arr[i]
        while j < N:
            if i+K == j:
                sum -= Arr[i]
                i += 1
            sum += Arr[j]
            m = max(m, sum)
            j += 1
            print(i, j, Arr[i], sum, m)
        return m

if __name__ == "__main__":
    print(Solution().maximumSumSubarray(4,[1,4,2,10,23,3,1,0,20], 9))