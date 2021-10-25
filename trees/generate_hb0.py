
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node(val={self.val}, left={self.left}, right={self.right})"

class Avl:
    def __init__(self):
        self.root = None
        self.val = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.root}->Node(val={self.val}, left={self.left}, right={self.right})"


count = 0
def hb(h):
    global count
    if h <= 0:
        return None
    n = Node()
    n.left = hb(h-1)
    n.right = hb(h-1)
    n.val = count
    count += 1
    return n

if __name__ == "__main__":
    root = hb(2)
    print(root)
