
def removeDuplicates(nums) -> int:
    n = len(nums)
    c = 1
    start = 1
    for i in range(1 ,n):
        if nums[i] == nums[ i -1]:
            c += 1
        else:
            nums[start] = nums[i]
            start += 1
            c = 1
        if c == 2:
            nums[start] = nums[i]
            start += 1

    return start

if __name__ == "__main__":
    arr = [0,0,1,1,1,1,2,2,3,3]
    print(arr)
    t=removeDuplicates(arr)
    print(arr[:t])
    arr1 = [1,1,1,2,2,3]
    print(arr1)
    t = removeDuplicates(arr1)
    print(arr1[:t])