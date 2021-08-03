import sys
import os
sys.path.append(os.getcwd())
from stack import list_stack

def reverse(s):
    newstk = list_stack.Stack()
    while not s.isEmpty():
        newstk.push(s.pop())
    return newstk

def main():
    """
    time complexity: O(n)
    space complexity: O(n)-> for creating a new stack
    :return:
    """
    s = list_stack.Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s = reverse(s)
    print("now value")
    while not s.isEmpty():
        print(s.pop())

if __name__ == "__main__":
    main()