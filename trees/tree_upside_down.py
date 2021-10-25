class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left.val if self.left else ''}, right={self.right.val if self.right else ''}"

def construct_tree():
    root = Node(1)
    root.left = Node(2, left=Node(4), right=Node(5))
    root.right = Node(3)

    return root


def call(root):
    if not root:
        return None
    return dfs(root, root)[0]

def getNode(root):
    """
    O(|n|) -> number of nodes in left or right
    :param root:
    :return:
    """
    if not root.left and not root.right:
        return root
    if root.left:
        return getNode(root.left)
    if root.right:
        return getNode(root.right)


def dfs(root, parent):
    """
    O(n) traversal, Space O(n) -> number of nodes, if nodes counted
    if not , space O(1)
    :param root:
    :param parent:
    :return:
    """
    if not root.left and not root.right:
        return root, None
    newroot, right = dfs(root.left, root)
    if newroot.left:
        right.left = root.right if root else None
        right.right = root
    else:
        newroot.left = root.right if root else None
        newroot.right = root
    root.left = None
    root.right = None
    return newroot, newroot.right


def upside_iterative(root):
    """
    O(n)
    space O(1)
    :param root:
    :return:
    """
    current = root
    next = tmp = prev = None

    while current:
        next = current.left
        current.left = tmp
        tmp = current.right
        current.right = prev
        prev = current
        current = next
    return prev

if __name__ == "__main__":
    root = construct_tree()
    r = call(root)
    print(r)
    t = r
    q = [t]
    while q:
        n = q.pop(0)
        print(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

    print("iter")
    root = construct_tree()
    r = upside_iterative(root)
    t = r
    q = [t]
    while q:
        n = q.pop(0)
        print(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
