from heapq import heappop, heappush, heapify

class Node:
    def __init__(self):
        self.char = None
        self.left = None
        self.right =  None
        self.freq = 0

    def __lt__(self, other):
        return self.freq < other.freq

def encode(node, huffman_tree, string):
    if not node:
        return
    if node.left is None and node.right is None:
        huffman_tree[node.char] = string if len(string) > 0 else '1'
    encode(node.left, huffman_tree, string+"0")
    encode(node.right, huffman_tree, string+"1")

def decode(string, index, node):
    if not node:
        return index
    if node.left is None and node.right is None:
        print(node.char, end="")
        return index
    index+= 1
    node = node.left if string[index] == '0' else node.right
    return decode(string, index, node)

def build_huffman_tree(string):
    """
    o(nlogn)
    :param string:
    :return:
    """
    pq = []
    map = dict()
    for char in string:
        pair = map.setdefault(char, Node())
        pair.char = char
        pair.freq +=1
    pq = list(map.values())
    heapify(pq)
    while len(pq) > 1:
        first = heappop(pq)
        second = heappop(pq)
        res = Node()
        res.left = first
        res.right = second
        res.freq = first.freq+second.freq
        heappush(pq, res)

    root = pq[0]
    huffman_tree = dict()
    encode(root, huffman_tree, "")
    print(huffman_tree)
    encoded_str = ""
    for char in string:
        encoded_str += huffman_tree.get(char)
    print(f"{string} encoded value is {encoded_str}")

    print("decoded string")
    # if only one root value exists, like a, aa,aaa, if condition will execute
    if root.left is None and root.right is None:
        while root.freq > 0:
            print(root.char, end="")
            root.freq -= 1
    else:
        index = -1
        while index < len(encoded_str)-1:
            index = decode(encoded_str, index, root)


if __name__ == "__main__":
    text = "aaaa"
    build_huffman_tree(text)
    text1 = "Huffman coding is a data compression algorithm."
    build_huffman_tree(text1)

