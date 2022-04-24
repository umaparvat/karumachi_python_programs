"""
TreeNode will have 4 pointers

left -> word which is lesser than root
right -> word which is greater than root
equal -> word which is equal to root
end -> to denote end of word

the perfix can be included always to the equal pointer
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.equal = None
        self.end = None


class Ternary:
    def __init__(self):
        self.root = None

    def addNode(self, word):
        if len(word) == 0:
            return
        self.root = self.insertelement(self.root, word, 0)

    def insertelement(self, rootNode, word, position):
        node = rootNode
        if not node:
            node = TreeNode(word[position])
        if word[position] < node.data:
            node.left = self.insertelement(node.left, word, position)
        elif word[position] > node.data:
            node.right = self.insertelement(node.right, word, position)
        else:
            if position+1 < len(word):
                node.equal = self.insertelement(node.equal, word, position+1)
            else:
                node.end = True
        return node

    def search(self, word):

        if len(word) > 0 and self.searchelement(self.root, word, 0) == True:
            return "Found"
        return "Not found"

    def searchelement(self, rootNode, word, position):
        if not rootNode:
            return False
        elif word[position] < rootNode.data:
            return self.searchelement(rootNode.left, word, position)
        elif word[position] > rootNode.data:
            return self.searchelement(rootNode.right, word, position)
        else:
            if position+1 < len(word):
                return self.searchelement(rootNode.equal, word, position+1)
            else:
                return rootNode.end

    def printWords(self, node, output, depth):
        if node:
            # visit left node
            self.printWords(node.left, output, depth)
            if node.end:
                print(" ", (output+str(node.data)))
            #visit equal node
            self.printWords(node.equal, output + str(node.data), depth + 1)
            # visit right node
            self.printWords(node.right, output, depth)

    def countsiblings(self, node):
        if not node:
            return 0
        count = 0
        if node.left:
            count += 1
        if node.right:
            count += 1

        if node.equal:
            count += 1
        return count

    def deleteWord(self, node, word, position):
        if not node:
            return None

        child = self.countsiblings(node)

        if word[position] < node.data:
            node.left = self.deleteWord(node.left, word, position)
        elif word[position] > node.data:
            node.right = self.deleteWord(node.right, word, position)
        else:
            if position+1 < len(word):
                node.equal = self.deleteWord(node.equal, word, position + 1)
            else:
                if child > 0: # child exists for that node
                    node.end = False
                else:
                    return None

        if child != self.countsiblings(node) and child == 1 and node.end is False:
            return None

        return node

def main() :
	tree = Ternary()
	#  Add words
	tree.addNode("feel")
	tree.addNode("fee")
	tree.addNode("run")
	tree.addNode("milk")
	tree.addNode("co")
	tree.addNode("code")
	print(" Ternary search tree")
	tree.printWords(tree.root, "", 0)
	#  Case A
	word = "fee"
	print("\n Delete word : ", word ," ")
	tree.root = tree.deleteWord(tree.root, word, 0)
	print(" Ternary search tree")
	tree.printWords(tree.root, "", 0)
	#  Case B
	word = "code"
	print("\n Delete word : ", word ," ")
	tree.root = tree.deleteWord(tree.root, word, 0)
	print(" Ternary search tree")
	tree.printWords(tree.root, "", 0)
	#  Case C
	word = "milks"
	print("\n Delete word : ", word ," ")
	tree.root = tree.deleteWord(tree.root, word, 0)
	print(" Ternary search tree")
	tree.printWords(tree.root, "", 0)
	#  Case D
	word = "feel"
	print("\n Delete word : ", word ," ")
	tree.root = tree.deleteWord(tree.root, word, 0)
	print(" Ternary search tree")
	tree.printWords(tree.root, "", 0)

if __name__ == "__main__":
    main()

