

def isAnagram(s1: str, s2: str) -> bool:
    if not s1 or not s2:
        return False
    ar = [0]*26
    s1 = s1.lower()
    s2 = s2.lower()
    for char in s1:
        ind = ord(char) - ord('a')
        ar[ind] += 1

    for char in s2:
        ind = ord(char) - ord('a')
        ar[ind] -= 1

    for each in ar:
        if each != 0:
            return False
    return True

if __name__ == "__main__":
    print(isAnagram("", ""))
    print(isAnagram("A", "A"))
    print(isAnagram("A", "B"))
    print(isAnagram("ab", "ba"))
    print(isAnagram("AB", "ab"))