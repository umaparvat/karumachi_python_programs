

def checkpattern(s, pattern):
    """
    O(n-m+1) *O(m) => O(nm) time complexity
    space: O(1)
    :param s:
    :param pattern:
    :return:
    """
    if not pattern:
        return 0
    for ind in range(len(s)- len(pattern)+1):
        pind = 0
        sind = ind
        while pind < len(pattern) and sind < len(s) and pattern[pind] == s[sind]:
                pind += 1
                sind += 1
        if pind == len(pattern):
            return sind
    return -1

if __name__ == "__main__":
    index = checkpattern("xxxxyzabcdabcdefabc", "abc")
    if index == -1:
        print("pattern not found")
    print("pattern found at index",index )