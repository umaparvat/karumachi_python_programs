"""
This algo works only if the pattern has repeated characters.
"""

def frequency_table(pattern):
    """
    if character in pattern matches increment i and k. and
    update the frequency table for the pattern character index(i) to k value
    if character(k) not matches in the pattern character(i),
    find the previous character frequency table value(f[k-1]) and move the k to that value
    and start comparing whether it matches or not.
    if the k reaches 0, update the frequency table for that pattern character(i) is 0
    :param pattern:
    :return:
    """
    m = len(pattern)
    f = [0]*m
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[k] != pattern[i]:
            # if pattern is not matching,
            # move the k back by looking at the previous F table value
            k = f[k-1]
        if pattern[k] == pattern[i]:
            k += 1
        f[i] = k
    return f

def kmp(s, pattern):
    """
    whenever there is  a mismatch b/w pattern and text.
    look the f table for the mismatch character pattern index previous position
    and move the matcher(q) to that position
    and start comparing from that pattern char index against text
    :param s:
    :param pattern:
    :return:
    time complexity: O(m+n)
    """
    f = frequency_table(pattern)
    print(f)
    n = len(s)
    m = len(pattern)
    q = 0
    output = []
    for i in range(n):
        while q > 0 and pattern[q] != s[i]:
            q = f[q-1]
        if pattern[q] == s[i]:
            q += 1

        if q == m:
            print("match found at index", i-m+1)
            output.append((i-m+1, s[i-m+1: i+1]))
            q = 0
    if output:
        return output
    return -1


if __name__ == "__main__":
    text = "bacbabababacacabababaca"
    pattern = "ababaca"
    print(kmp(text, pattern))
