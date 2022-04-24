from copy import copy
def minSwaps(nums):
		#Code here
    print(nums)
    n = len(nums)
    t = copy(nums)
    t.sort()
    m = {}
    for i in range(n):
        m[t[i]] = i
    print(m)
    c = 0
    for i in range(n):
        j = i
        while j != m[nums[j]]:
            nums[j], nums[m[nums[j]]] = nums[m[nums[j]]], nums[j]
            c += 1
        j += 1
    return c





if __name__ == "__main__":
    #arr = [10,19,6,3,5]
    #print(minSwaps(arr))
    arr1 = [7,16, 14, 17, 6, 9, 5, 3, 18]
    print(minSwaps(arr1))