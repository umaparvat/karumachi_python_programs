import sys
import os
sys.path.append(os.getcwd())
from stack.list_stack import Stack

def is_palindrome(s):
    st = Stack()
    for each in s:
        if each != "X":
            st.push(each)
    for i in range(len(s)-1,-1,-1):
        if s[i] == "X":
            break
        else:
            if st.pop() != s[i]:
                return False
    return True

def main():
    print("is_palindrome([m,a,x,a,m])", is_palindrome(["m", "a", "X", "a", "m"]))

if __name__ == "__main__":
    main()