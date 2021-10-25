

def convert(arr):
    non_leaf_node = (len(arr)-1)//2 + 1
    for index in range(non_leaf_node, -1, -1):
        heapify(arr, index)


def heapify(arr, index):
    if index < len(arr):
        smallest = index
        left = 2*index+1
        right = 2*index+2
        if left < len(arr) and arr[left]< arr[smallest]:
            smallest = left
        if right < len(arr) and arr[right] < arr[smallest]:
            smallest = right
        if smallest != index:
            arr[index], arr[smallest] = arr[smallest] ,arr[index]
            heapify(arr, smallest)


if __name__ == "__main__":
    A = [9, 4, 7, 1, -2, 6, 5]
    print(f"max heap: {A}")
    convert(A)
    print("min heap:",A)