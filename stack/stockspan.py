
class Solution:

    # Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self, a, n):
        # code here
        result = self.findNrGrtLeft(a, n)
        print(result)
        for i in range(len(a)):
            t = i - result[i]
            print(a[i], i, result[i], t)
            result[i] = t
        print(result)
        return result

    def findNrGrtLeft(self, a, n):
        o = []
        s = []
        for i in range(len(a)):
            if not s:
                o.append(-1)
            elif s and s[-1].get("price") > a[i]:
                o.append(s[-1].get("value"))
            else:
                while s and s[-1].get("price") <= a[i]:
                    s.pop()
                if not s:
                    o.append(-1)
                else:
                    o.append(s[-1].get("value"))
            s.append({"price": a[i], "value": i})
        return o

if __name__ == "__main__":
    s = Solution()
    n=78
    a = [74,665,742,512,254,469,748,445,663,758,38,60,724,142,330,779,317,636,591,243,289,507,241,143,65,249,247,606,691,330,371,151,607,702,394,349,430,624,85,755,357,641,167,177,332,709,145,440,627,124,738,739,119,483,530,542,34,716,640,59,305,331,378,707,474,787,222,746,525,673,671,230,378,374,298,513,787,491]
    s.calculateSpan(a, n)