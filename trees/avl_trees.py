

class Node:
    def __init__(self, data, left=None, right=None, height= 1):
        self.val = data
        self.left = left
        self.right = right
        self.height = height

def height(node):
    if not node:
        return 0
    return node.height


class Avl:

    def left_rotate(self, z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = 1 + max(height(z.left), height(z.right))
        y.height = 1 + max(height(y.left), height(y.right))
        return z

    def right_rotate(self, z):
        y = z.left
        t2 = y.right
        y.right = z
        z.left = t2
        z.height = 1 + max(height(z.left), height(z.right))
        y.height = 1 + max(height(y.left), height(y.right))
        return z

    def insert_a_node(self, node, key):
        if not node:
            return Node(key)
        elif key < node.val:
            node.left = self.insert_a_node(node.left, key)
        else:
            node.right = self.insert_a_node(node.right, key)
        node.height = 1 + max(height(node.left), height(node.right))
        balancefactor = self.getbalance(node)
        if balancefactor > 1:
            if key < node.left.val:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if node.balancefactor < -1 :
            if key > node.right.val:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        return node

    def delete(self, node, key):
        if not node:
            return node
        elif key < node.val:
            node.left = self.delete(node.left, key)
        elif key > node.val:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.getMinNode(node.right)
            node.val = temp.val
            node.right = self.delete(node.right, temp.val)
        if node is None:
            return node
        node.height = 1 + max(height(node.left), height(node.right))
        balancefactor = self.getbalance(node)
        if balancefactor > 1:
            if self.getbalance(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balancefactor < -1:
            if self.getbalance(node.right) <= 0 :
                return self.right_rotate(node.right)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        return node

    def getbalance(self, node):
        if not node:
            return 0
        return height(node.left) - height(node.right)

    def getMinNode(self, node):
        if not node or node.left is None:
            return node
        self.getMinNode(node.left)




