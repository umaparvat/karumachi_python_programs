import os
import sys
sys.path.append(os.getcwd())
from queues.queue_list import Queue
from stack.list_stack import Stack

def reverse(node):
    queue = Queue()
    queue.enqueue((node, 0))
    s = Stack()
    o = []
    while not queue.isEmpty():
        n, l = queue.dequeue()
        if n.left:
            queue.enqueue((n.left, l+1))
        if n.right:
            queue.enqueue((n.right, l+1))
        if not s.isEmpty() and s.peek()[1] != l:
            while not s.isEmpty():
                val = s.pop()[0].val
                o.insert(0, val)
            s.push((n,l))
        else:
            s.push((n,l))
    while not s.isEmpty():
        o.insert(0, s.pop()[0].val)
    return o


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left.val if self.left else ''}, right={self.right.val if self.right else ''}"
def construct_tree():
    a = Node(2, left=Node(4), right=Node(5))
    b = Node(3, left=Node(6), right=Node(7))
    root = Node(1, left=a, right=b)
    return root

if __name__ == "__main__":
    tree = construct_tree()
    print(reverse(tree))
