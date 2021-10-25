"""
median using insertion sort
"""
def insertionsort(elements):
    start = 0
    while start < len(elements)-1:
        last = start+1
        value = elements[last]
        while last > 0 and value < elements[last-1]:
            elements[last] = elements[last-1]
            last -= 1
        elements[last] = value
        start += 1


def median_insertion(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        insertionsort(arr)
        print(arr)
        if len(arr) & 1:
            return arr[len(arr)//2]
        else:
            mid = len(arr)//2
            return (arr[mid] + arr[mid-1])/2



if __name__ == "__main__":
    ele = [1,7,3,0,5,8,3,2,6,9]
    print(median_insertion(ele))