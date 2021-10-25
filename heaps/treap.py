from random import randrange

class TreapNode:
    def __init__(self, value, priority=100, left=None, right=None):
        self.value = value
        self.priority = randrange(priority)
        self.left = left
        self.right = right

def leftrotate(node):
    """
        r
      /  \
     z    R
         / \
        y   x
    left rotate r
          R
        /  \
       r    x
      / \
     z  y
    :param node:
    :return:
    """
    R = node.right
    y = node.right.left
    R.left = node
    node.right = y
    return R

def rightrotate(node):
    """
         r
        / \
       L  R
      / \
     x   y

     right rotate
      L
     / \
    x   r
       / \
      y  R


    :param node:
    :return:
    """
    L = node.left
    y = node.left.right
    node.left = y
    L.right = node
    return L

def insertNode(node, data):

    if not node:
        return TreapNode(data)
    if data < node.value:
        node.left = insertNode(node.left, data)
        if node.left and node.left.priority > node.priority:
            node = rightrotate(node)
    else:
        node.right = insertNode(node.right, data)
        if node.right and node.right.priority > node.priority:
            node = leftrotate(node)
    return node

def searchnode(node, data)-> bool:
    if not node:
        return False
    if data == node.value:
        return True
    if data < node.value:
        return searchnode(node.left, data)
    else:
        return searchnode(node.right, data)

def deleteNode(node, data):
    if not node:
        return
    if data < node.value:
        node.left = deleteNode(node.left, data)
    elif data > node.value:
        node.right = deleteNode(node.right, data)
    else:
        if node.left is None and node.right is None:
            node = None
        elif node.left and node.right:
            if node.left.priority < node.right.priority:
                node = leftrotate(node)
                node.left = deleteNode(node.left, data)
            else:
                node = rightrotate(node)
                node.right = deleteNode(node.right, data)
        else:
             node = node.left if node.left else node.right
        return node

if __name__ == "__main__":
    # Treap keys
    keys = [5, 2, 1, 4, 9, 8, 10]
    root = None
    for key in keys:
        root = insertNode(root, key)
