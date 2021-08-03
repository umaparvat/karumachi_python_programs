from linkedlist.queueLL import QueueLL
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class ExpressionTrees:
    def __init__(self, exprStr):
        self._expTree = None
        self._build(exprStr)

    def _build(self, exprStr):
        tokensQueue = QueueLL()
        for each in exprStr:
            tokensQueue.enqueue(each)
        root = TreeNode(None)
        self._expTree = root
        self._recBuildTree(self._expTree, tokensQueue)

    def _recBuildTree(self, node, queue):
        token = queue.dequeue()
        current = node
        if token == "(":
            current.left = TreeNode(None)
            self._recBuildTree(current.left, queue)
            current.data = queue.dequeue()  # "for operator * / + -"
            current.right = TreeNode(None)
            self._recBuildTree(current.right, queue)
            queue.dequeue()  # ")"
        else:
            current.data = token


    def evaluate(self, varDict):
        return self._evalTree(self._expTree, varDict)

    def _evalTree(self, expression, varDict):
        if expression.left is None and expression.right is None:
            if 0 <= expression.data <= 9:
                return int(expression.data)
            else:
                assert expression.data in varDict, "Invalid variable"
                return varDict.get(expression.data)
        else:
            lvalue = self._evalTree(expression.left, varDict)
            rvalue = self._evalTree(expression.right, varDict)
            return self._computeop(lvalue, rvalue, expression.data)

    @staticmethod
    def _computeop(leftval, rightval, operator):
        if operator == "+":
            return int(leftval) + int(rightval)
        elif operator == "-":
            return int(leftval) - int(rightval)
        elif operator == "/":
            assert int(rightval) > 0 , "zeroDivisionByError"
            return int(leftval) // int(rightval)
        elif operator == "*":
            return int(leftval) * int(rightval)

    def toString(self):
        return self._buildString(self._expTree)

    def _buildString(self, treeNode):
        if treeNode and treeNode.left is None and treeNode.right is None:
            return treeNode.data
        else:
            expstr = "("
            expstr += self._buildString(treeNode.left)
            expstr += str(treeNode.data)
            expstr += self._buildString(treeNode.right)
            expstr += ")"
            return expstr
