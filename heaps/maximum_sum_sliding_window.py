

class MaximumSum:

    def __init__(self, data):
        self.data = data

    def find_max_sum(self, window) -> list:
        """
        single traverse -> O(n)
        space -> O(1) excluding output. including output variable O(k)
        :param window:
        :return:
        """
        start = end = 0
        total = 0
        greatest = 0
        gt_start = start
        gt_end = end
        while end < len(self.data):
            total += self.data[end]
            if end-start+1 == window:
                if greatest < total:
                    greatest = total
                    gt_start = start
                    gt_end = end+1
                total -= self.data[start]
                start += 1
            end += 1
        return self.data[gt_start:gt_end]

if __name__ == "__main__":
    arr = [1, 3, -1, -3, 5 , 3, 6, 7]
    msum = MaximumSum(arr)
    print(msum.find_max_sum(3))


