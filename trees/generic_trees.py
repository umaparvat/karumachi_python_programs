

class GNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __str__(self):
        return f"Node(val={self.val}, children=[{self.children}])"

    def lenChild(self):
        return len(self.children)

    def nthChild(self, n):
        if n < self.lenChild():
            return self.children[n]
        else:
            return None

    def add_children(self, value):
        self.children.append(GNode(value))

    def remove_children(self, value):
        if not self.children:
            return None
        remove_node_ind = None
        for ind, each_child in enumerate(self.children):
            if each_child.val == value:
                if not each_child.children:
                    remove_node_ind = ind
                    break
                else:
                    raise Exception("Node is not empty")
        self.children.pop(remove_node_ind)


def construct_tree():
    parent = GNode(1)
    parent.add_children(2)
    parent.add_children(3)
    parent.add_children(4)
    parent.add_children(5)
    first_child = parent.nthChild(0)
    first_child.add_children(7)
    first_child.add_children(8)
    third_child = parent.nthChild(2)
    third_child.add_children(9)
    third_child.add_children(10)
    fourth_child = parent.nthChild(3)
    fourth_child.add_children(11)
    return parent

def root_to_leaf(node, path, paths):
    """
    preorder traversal: O(n)
    space:O(n)-> recursive stack
    :param node:
    :param path:
    :param paths:
    :return:
    """
    if not node:
        return paths
    if not node.children:
        path.append(node.val)
        paths.append(path)
    for each_child in node.children:
        root_to_leaf(each_child, path+[node.val], paths)
    return paths

def sum_all_elements_recursive(node, sum):
    """
    post order traversal: O(n)
    space :O(n) -> recursive stack
    :param node:
    :return:
    """
    if not node:
        return 0
    if not node.children:
        return sum+node.val
    for each_child in node.children:
            sum = sum_all_elements_recursive(each_child, sum)
    sum = sum+node.val
    return sum



if __name__ == "__main__":
    tree = construct_tree()
    paths = root_to_leaf(tree, [], [])
    print(paths)
    print(sum_all_elements_recursive(tree, 0))



        




