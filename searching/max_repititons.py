

def maxrep(arr):
    n = len(arr)
    maxi = 0
    for i in range(n):
        arr[arr[i]%n] += n
    print(arr)
    for i in range(n):
        if arr[i]//n > maxi:
            maxi = arr[i]//n
            num = i
    print(maxi, num)



if __name__ == "__main__":
    arr= [3,2,1,1,2,2,3,3,3]
    print(arr)
    maxrep(arr)