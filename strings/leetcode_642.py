"""
642 Design Search Autocomplete System
Problem
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list. Your job is to implement the following functions:
The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

Example:

Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

Note: The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words. The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100. Please use double-quote instead of single-quote when you write test cases even for a character input. Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.counter = 0
class Trie:
    def __init__(self):
        self.root = self.getNode()
        self.output = []
    def getNode(self):
        return TrieNode()
    def get_index(self, string):
        if string == "#":
            return ord("#")
        return ord(string)

    def get_char(self, index):
        return chr(index)

    def insert(self, word, time):
        root = self.root
        for char in word:
            char_index = self.get_index(char)
            if char_index not in root.children:
                root.children[char_index] = self.getNode()
            root = root.children.get(char_index)
            root.counter += time
        root.is_end = True

    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix, node.counter))
        for char_index in node.children:
            self.dfs(node.children.get(char_index), prefix+self.get_char(char_index))

    def query(self, prefix):
        """
        search for the prefix in trie ds.
        if prefix not exists add that into trie.
        return only first 3 hot matches
        :param prefix:
        :return:
        """
        root = self.root
        self.output = []
        for char in prefix:
            char_index = self.get_index(char)
            if char_index not in root.children:
                self.insert(prefix, 1)
                return []
            root = root.children.get(char_index)
        self.dfs(root, prefix)
        output = sorted(self.output, key=lambda x: x[1], reverse=True)
        return [x[0] for x in output][:3]



class AutoCompleteSystem:
    def __init__(self, sentences:list, times:list):
        self.sentences = sentences
        self.times = times
        self.trie = Trie()
        self.build()

    def build(self):
        for sentence, time in zip(self.sentences, self.times):
            self.trie.insert(sentence, time)

    def search(self, prefix):
        return self.trie.query(prefix)

if __name__ == "__main__":
    ac = AutoCompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5,3,2,2])
    prefix = ""
    while True:
        prefix += input().strip()
        if "#" in prefix:
            break
        else:
            print(ac.search(prefix))