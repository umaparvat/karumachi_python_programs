
class _TreeNodes:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

class Trees:
    def __init__(self):
        pass
    def preorder_traversal(self, node):
        """
        Root -> left -> Right
        :param node:
        :return:
        """
        if node:
            print(node.data)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_travesal(self, node):
        """
        Left,Root, Right
        :param node:
        :return:
        """
        if node:
            self.inorder_travesal(node.left)
            print(node.data)
            self.inorder_travesal(node.right)
    def postorder_traversal(self, node):
        """
        left, right, root
        :param node:
        :return:
        """
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data)