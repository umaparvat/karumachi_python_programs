"""
Given a string of lowercase characters from ‘a’ – ‘z’.
We need to write a program to print the characters of this string in sorted order.
"""

def sort(s):
    ar = [0]*256
    for char in s:
        ar[ord(char)] += 1

    output = ""
    for ind, val in enumerate(ar):
        if val:
            char = chr(ind)*val
            output+=char
    return output


if __name__ == "__main__":
    print("input: bbccdefbbaa", sort("bbccdefbbaa"))
    print("input: bbccdefbbaa", sort("bbccdefbbaa"))
    print("input: geeksforgeeks", sort("geeksforgeeks"))

