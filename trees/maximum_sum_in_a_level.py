import sys, os
sys.path.append(os.getcwd())
from queues.queue_list import Queue

def maximum_level_sum(node):
    if not node:
        return 0
    q = Queue()
    level = 0
    prev_level = 0
    m_sum = 0
    sum = 0
    max_level = 0
    q.enqueue((node,level))
    while not q.isEmpty():
        node, level = q.dequeue()
        if level == prev_level:
            sum += node.val
        elif sum > m_sum and level != prev_level:
                m_sum = sum
                max_level = prev_level
                sum = node.val

        if node.left:
            q.enqueue((node.left, level+1))
        if node.right:
            q.enqueue((node.right, level+1))
        prev_level = level
    if sum > m_sum:
        # if leaf node is greater than all levels
        m_sum = sum
        max_level = prev_level
        sum = 0
    return max_level, m_sum



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node: {self.val}, left={self.left.val if self.left else ''}, right={self.right.val if self.right else ''}"

def construct_tree():
    root = Node(3)
    root.left = Node(4, left=Node(8, left=Node(12)), right=Node(9))
    root.right = Node(7, left=Node(10), right=Node(11))
    root1 = Node(3)
    root1.left = Node(4, left=Node(8, left=Node(120)), right=Node(9))
    root1.right = Node(7, left=Node(10), right=Node(11))
    return root, root1

if __name__ == "__main__":
    tree1, tree2 = construct_tree()
    print("tree1 max:", maximum_level_sum(tree1))
    print("tree2 max:", maximum_level_sum(tree2))