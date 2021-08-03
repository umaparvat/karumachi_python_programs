from generic_trees import construct_tree


def get_parent(node, val, parent):
    if not node:
        return
    if node.val == val:
        return parent
    if not node.children:
        return
    parent = node
    for each_child in node.children:
        current_parent = get_parent(each_child, val, parent)
        if current_parent:
            return current_parent
    return


def get_sibling(node, value):
    parent = get_parent(node, value, node)
    if parent:
        return parent.lenChild()-1



class GenericTreeNode:
    def __init__(self, data):
        self.val = data
        self.firstChild = None
        self.nextSibling = None

    def __str__(self):
        return f"Node(val={self.val}, firstChild={self.firstChild}, nextSibling={self.nextSibling})"


def get_sibling_generic(node):
    if not node:
        return
    current = node
    count = 0
    print(current)
    while current:
        current = current.nextSibling
        count += 1
    return count



def construct_generic_tree_node():
    gn = GenericTreeNode(2)
    sec = GenericTreeNode(4)
    sec.nextSibling = GenericTreeNode(8)
    gn.nextSibling = sec
    return gn

if __name__ == "__main__":
    tree = construct_tree()
    print(get_sibling(tree, 8))
    gntree = construct_generic_tree_node()
    print(get_sibling_generic(gntree))