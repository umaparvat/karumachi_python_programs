class BIT:
    def __init__(self, arr_list):
        self.tree = [0]+arr_list
        for i in range(1, len(self.tree)):
            index = i + (i&-i)
            if index < len(self.tree):
                self.tree[index] += self.tree[i]

    def sum(self, index):
        total = 0
        while index:
            total += self.tree[index]
            index -= index & -index
        return total

    def update(self, index, val):
        index += 1
        while index < len(self.tree):
            self.tree[index] += val
            index += index & -index

    def query(self, l, r):
        return self.sum(r) - self.sum(l-1)


def main():
    arr = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
    bit_tree= BIT(arr)
    print(bit_tree.tree)
    print(bit_tree.sum(5))
    print(bit_tree.query(3,5))
    k = 5
    update_val = arr[0]-k if arr[0] > k else k-arr[0]
    bit_tree.update(0, update_val)
    print(bit_tree.tree)
    print(bit_tree.query(1,3))

if __name__ == "__main__":
    main()

