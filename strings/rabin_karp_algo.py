

def search_pattern_all(s, pattern, q):
    """
    time complexity: O(m+n)
    :param s:
    :param pattern:
    :param q:
    :return:
    """
    d = 10
    m = len(pattern)
    n = len(s)
    p = 0
    t = 0
    h = 1

    for i in range(m-1):
        h = (h*d)% q
        print("h", h, i)

    for i in range(m):
        print("before", p, d, i)
        p = (p*d+ord(pattern[i]))% q
        t = ((t*d+ord(s[i]))) %q
        print("after", p,q, i)

    for i in range(n-m+1):
        if p == t:
            j = 0
            for j in range(m):
                if s[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("patter found at index", str(i+1))
        if i < n-m:
            t = (d * (t - ord(s[i]) * h) + ord(s[i + m])) % q

            if t < 0:
                t += q

if __name__ == "__main__":
    search_pattern_all("ABCCDDAEFG", "CDD", 13)



