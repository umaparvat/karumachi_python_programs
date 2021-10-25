# User function Template for python3
class Maxheap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def top(self):
        return self.heap[0] if self.heap else float("-inf")

    def __len__(self):
        return self.size

    def heapify(self, index):
        if index < self.size:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < len(self) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.swap(index, largest)
                self.heapify(largest)

    def swap(self, start, end):
        self.heap[start], self.heap[end] = self.heap[end], self.heap[start]

    def insert(self, value):
        if not self.heap:
            self.heap.append(value)
            self.size += 1
        else:
            self.size += 1
            self.heap.append(value)
            parent = (self.size-1)//2
            for i in range(parent, -1, -1):
                self.heapify(i)
        return

    def removemax(self):
        if self.size > 1:
            self.swap(0, self.size - 1)
            self.size -= 1
            self.heapify(0)
            self.heap.pop()
        else:
            return self.heap[0] if self.heap else float("-inf")

class Solution:

    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):

        # code here
        maxheap = Maxheap()
        todrop = Maxheap()
        ans = []
        for index in range(k):
            maxheap.insert(arr[index])
        ans.append(maxheap.top())
        for index in range(k, n):
            todrop.insert(arr[index-k])
            while len(todrop) != 0 and todrop.top() == maxheap.top():
                maxheap.removemax()
                todrop.removemax()
            maxheap.insert(arr[index])
            ans.append(maxheap.top())
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
        arr = [1,2,3,1,4,5,2,3,6]
        n = len(arr)
        k = 3
        ob = Solution()
        res = ob.max_of_subarrays(arr, n, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends