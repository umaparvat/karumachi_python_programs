class TreeNode:
    def __init__(self):
        self.sub = ""
        self.child = []


class SuffixTree:
    def __init__(self, data):
        self.nodes = []
        self.nodes.append(TreeNode())
        #  Construct tree
        self.buildTree(data)

    def addSuffix(self, suf):
        #  Declare some useful auxiliary variables
        n = 0
        i = 0
        x2 = 0
        n2 = 0
        n3 = 0
        j = 0
        temp = None
        process = True
        sub2 = ""
        while (i < len(suf)):
            b = suf[i]
            children = self.nodes[n].child
            while (process):
                if (x2 == len(children)):
                    n2 = len(self.nodes)
                    temp = TreeNode()
                    temp.sub = suf[i:]
                    self.nodes.append(temp)
                    children.append(n2)
                    return

                n2 = children[x2]
                if (self.nodes[n2].sub[0] == b):
                    process = False
                else:
                    x2 += 1

            sub2 = self.nodes[n2].sub
            process = True
            while (j < len(sub2) and (i + j) < len(suf) and process == True):
                if (suf[i + j] != sub2[j]):
                    n3 = n2
                    n2 = len(self.nodes)
                    temp = TreeNode()
                    temp.sub = sub2[0: j]
                    temp.child.append(n3)
                    self.nodes.append(temp)
                    self.nodes[n3].sub = sub2[j:]
                    self.nodes[n].child[x2] = n2
                    process = False
                else:
                    j += 1

            i += j
            n = n2
            #  Reset value
            x2 = 0
            n2 = 0
            n3 = 0
            j = 0
            temp = None
            process = True
            sub2 = ""

    def buildTree(self, str):
        i = 0
        while (i < len(str)):
            self.addSuffix(str[i:])
            i += 1

    def printData(self, n, prefix):
        children = self.nodes[n].child
        if ((len(children) == 0)):
            print("⤑ ", self.nodes[n].sub)
            return

        print("┐ ", self.nodes[n].sub)
        i = 0
        while (i < len(children) - 1):
            c = children[i]
            print(prefix, end="├─")
            self.printData(c, prefix + "│ ")
            i += 1

        print(prefix, end="└─")
        self.printData(children[len(children) - 1], prefix + "  ")

    def visualize(self):
        if len(self.nodes) == 0:
            print("\nEmpty Tree")
            return

        self.printData(0, "")


def main():
    #  Create Suffix Tree
    tree1 = SuffixTree("coconut")
    tree2 = SuffixTree("BAABAIAIIBI")
    #  Print path
    tree1.visualize()
    tree2.visualize()


if __name__ == "__main__": main()