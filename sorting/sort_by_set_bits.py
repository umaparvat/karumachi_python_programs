def sortBySetBitCount(arr, n):
    # Your code goes here
    bits_arr = [0] * n
    for ind, num in enumerate(arr):
        c = 0
        #q= num
        while num:
            if num&1 != 0:
                c += 1
            num >>=1
        #print(q, c)
        bits_arr[ind] = c
    maxi = max(bits_arr)
    #print("Bits", bits_arr)
    count = [0] * (maxi + 1)
    #print("count", count)
    for each in bits_arr:
        count[each] += 1
    #print("add", count)
    for i in range(maxi - 1, -1, -1):
        count[i] += count[i + 1]
    #print(count)
    temp = [0] * n
    for i in range(n - 1, -1, -1):
        val = arr[i]
        val_bit = bits_arr[i]
        count[val_bit] -= 1
        temp[count[val_bit]] = val
    return temp

if __name__ == "__main__":
    print(sortBySetBitCount([5, 2, 3, 9, 4, 6, 7, 15, 32], 9))