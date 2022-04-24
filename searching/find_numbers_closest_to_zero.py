

def find(arr):
    arr.sort()
    print(arr)
    i = 0
    j = len(arr)-1
    ans = float("inf")
    value = ()
    while i < j:
        cur_sum = arr[i]+arr[j]
        if ans > abs(cur_sum):
            ans = abs(cur_sum)
            value = (arr[i], arr[j])
        if cur_sum < 0:
            i += 1
        else:
            j -= 1
    print(ans, value)

if __name__ == "__main__":
    arr=[1, 60, -10, 70, -80, 85]
    find(arr)
    arr =[10,8,3,5,-9, -7, 6]
    find(arr)
