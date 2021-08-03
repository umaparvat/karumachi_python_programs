import math
import random
class Node:
    def __init__(self, data, level):
        self.data = data
        self.next = [None]*level
    
    def __str__(self):
        return f"Node({self.data}, {len(self.next)})"

class SkipList:
    def __init__(self, max_level=8):
        self.max_level = max_level
        n = Node(None, max_level)
        self.head = n
        self.verbose = False
    
    def updateList(self, element):
        update = [None]* self.max_level
        n = self.head
        self._n_traverse = 0
        level = self.max_level -1
        print(f"update list level is {level}")
        while level >= 0:
            if n.next[level] != None and n.next[level].data >= element:
                level = level + 1
                print(f"{n.next[level].data}, {level}")
            while n.next[level] and n.next[level].data < element:
                self._n_traverse +=1
                n = n.next[level]
                print(f"{n} < {element}")
            update[level] = n
            level = level -1
            print(f"update now is {update},  level is {level}")
        return update
    def find(self, data, update= None):
        if update is None:
            update = self.updateList(data)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate and candidate.data == data:
                return candidate
        return None
        
    def randomLevel(self, max_level):
        num = random.randint(1, 2**max_level -1)
        lognum = math.log(num, 2)
        level = int(math.floor(lognum))
        return max_level - level
    
    def insertNode(self, data, level=None):
        if level is None:
            level = self.randomLevel(self.max_level)
        print(f"insert level is {level}")
        node = Node(data, level)
        print(str(node))
        update = self.updateList(data)
        print(f"insert update is {update}")
        if self.find(data, update) == None:
            for i in range(level):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
    
def printLevel(sl, level):
    node = sl.head.next[level]
    while node:
        node = node.next[level]
    
x = SkipList(4)
for i in range(0, 20, 2):
    x.insertNode(i)
printLevel(x, 0)
printLevel(x, 1)
printLevel(x, 2)
                
                
            