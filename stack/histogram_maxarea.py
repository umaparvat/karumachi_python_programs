class Solution:

    # Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, histogram):
        # code here
        return self.findNrSmLeft(histogram)

    def findNrSmLeft(self, histogram):
        s = []
        m = 0
        i =0
        for i in range(len(histogram)):
            while s and s[-1].get("value") >= histogram[i]:
                d = s.pop()
                if not s:
                    m = max(m, (d.get("value") * i))
                else:
                    m = max(m, d.get("value") * (i - (s[-1].get("indx") + 1)))
            s.append({"value": histogram[i], "indx": i})
            i=i
        i+=1
        while s:
            d = s.pop()
            if not s:
                m = max(m, d.get("value") * i)
            else:
                m = max(m, d.get("value") * (i - (s[-1].get("indx") + 1)))
        return m

if __name__ == "__main__":
    print(Solution().getMaxArea([1,2,3,4,5]))
