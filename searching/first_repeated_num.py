from collections import defaultdict
def find_repeated_first(nums):
    """
    space: O(n)
    time : O(n)
    :param nums:
    :return:
    """
    ds = defaultdict(int)
    for num in nums:
        ds[num] += 1

    for num in nums:
        if ds[num] > 1:
            return num


def another_approach(nums):
    ds = defaultdict(int)
    maxi = 0
    for num in nums:
        if num in ds and ds[num] == 1:
            ds[num] = -2
        elif num in ds and ds[num] < 0:
            ds[num] -= 1
        elif num != "":
            ds[num] = 1
        else:
            ds[num] = 0
    element = None
    print(ds)
    for num in nums:
        if ds[num] < maxi:
            maxi = ds[num]
            element = num
    print(f"{element} is repeated for {abs(maxi)} times ")


if __name__ == "__main__":
    arr = [3,2,1,2,2,3,3,3]
    print(find_repeated_first(arr))
    print(another_approach(arr))