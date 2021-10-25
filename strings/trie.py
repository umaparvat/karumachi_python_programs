

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.counter = 0
    def __str__(self):
        return f"Node(children = {self.children}, is_end={self.is_end})"

class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def index(self, value):
        return ord(value)

    def insert(self, word):
        root = self.root
        for char in word:
            word_index = self.index(char)
            if word_index not in root.children:
                root.children[word_index] = self.get_node()
            root = root.children.get(word_index)
        root.is_end = True
        root.counter += 1

    def search(self, word):
        if not self.root.children:
            return "Trie is empty"
        root = self.root
        for char in word:
            char_index = self.index(char)
            if char_index not in root.children:
                return "word not found"
            root = root.children.get(char_index)

        if root.is_end is True:
            return "found"
        else:
            return "word not exists"

    def delete(self, word):
        if not self.root.children:
            return -1
        root = self.root
        for char in word:
            char_index = self.index(char)
            if char_index not in root.children:
                return -2
            root = root.children.get(char_index)
        if not root:
            return -1
        else:
            root.is_end = False
            root.counter -= 1
            return 0

    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val <= 0:
            self.insert(new_word)

    def dfs(self, node, prefix, output):
        if node.is_end is True:
            output.append([prefix, node.counter])
            return output
        for char_index in node.children:
            output = self.dfs(node.children.get(char_index), prefix+chr(char_index), output)
        return output

    def query(self, prefix):
        if not self.root.children:
            return []
        root = self.root
        for char in prefix:
            char_index = self.index(char)
            if char_index in root.children:
                root = root.children.get(char_index)
        if not root:
            """
            prefix not found in trie ds
            """
            return []
        output = []
        output = self.dfs(root, prefix, output)
        return sorted(output, key=lambda x:x[1] ,reverse=True)




if __name__ == "__main__":
    trie_ds = Trie()
    trie_ds.insert("was")
    trie_ds.insert("washington")
    trie_ds.insert("were")
    trie_ds.insert("won")
    print("search w", trie_ds.query("w"))
    print("search was", trie_ds.search("was"))
    print("delete won", trie_ds.delete("won"))
    trie_ds.update("were", "work")
    print("updated were with work")
    print("query wo", trie_ds.query("wo"))
    print("search w", trie_ds.query("w"))

