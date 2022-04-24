"""
Given a binary tree, find the largest value in each level.
Input :
        1
       / \
      2   3

Output : 1 3
Explanation :
There are two levels in the tree :
1. {1}, max = 1
2. {2, 3}, max = 3
Given an array arr[] of n integers,
construct a Product Array prod[] which is equal to target

"""
def get_pairs(arr, target):
    """
    time complexity: O(nlogn)
    space: O(1)
    :param arr:
    :param target:
    :return:
    """
    arr.sort()
    print(arr)
    i = 0
    j = len(arr)-1
    out = []
    while i < j:
        prod = arr[i] * arr[j]
        if prod == target:
            out.append((arr[i],arr[j]))
            i += 1
            j -= 1
        elif prod > target:
            j -= 1
        else:
            i += 1
    return out






from collections import deque
def distance(s1, s2):
    """
    the below works only s1 and s2 are same length
    and asked only the distance.
    :param s1:
    :param s2:
    :return:

    time complexity: O(length of string)
    space complexity: O(1)
    """
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

def print_distance(s1, s2):
    """
    same length of string and print the transition till end
    s1 and s2 is lowercase letters
    :param s1:
    :param s2:
    :return:
    """
    queue = deque()
    queue.append(s1)
    level = 0
    ans = [s1]
    pos = 0
    while queue:
        level = level+1
        ql = len(queue)
        for _ in range(ql):
            word = queue.popleft()
            if word == s2:
                return level-1, ans
            sp_word = [j for j in word]
            n = len(sp_word)
            if sp_word[pos] == s2[pos]:
                pos += 1
            for i in range(ord('a'), ord('z')+1):
                if chr(i) == s2[pos]:
                    sp_word[pos] = chr(i)
                    queue.append("".join(sp_word))
                    ans.append("".join((sp_word)))
                    pos += 1
                    break


def levenshtien_distance(s1, s2):
    """
    time complexity: O(mn)
    space complexity: O(mn)
    :param s1:
    :param s2:
    :return:
    """
    m = len(s1)
    n = len(s2)
    dp = [[0]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][0] = i
            dp[0][j] = j

    for j in range(n):
        for i in range(m):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    print(dp)
    return dp[-1][-1]


def valid_abbr(word, abbr):
    m = len(word)
    n = len(abbr)
    i = 0
    j = 0
    while i < m and j < n:
        if word[i] == abbr[j]:
            i += 1
            j += 1
            continue
        if abbr[j] < '0' or abbr[j] > '9':
            return False
        start = j
        while j < n and abbr[j].isdigit():
            j += 1
        num = int(abbr[start:j])
        i += num
    return i == m and j == n




if __name__ == "__main__":

    arr =[8, 10, 20, 9, 50, 40]
    print(get_pairs(arr, 400))

    # print("word: apple, a2e", valid_abbr("apple", "a2e"))
    # print("words: internationalization, i18n", valid_abbr("internationalization", "i18n"))
    # print("words: internationalization, i12iz4n", valid_abbr("internationalization", "i12iz4n"))
    # s1="cat"
    # s2 = "dog"
    # # print(print_distance(s1, s2))
    # # print(distance(s1, s2))
    # print(levenshtien_distance(s1, s2))
    #
    # s1= "cat"
    # s2 = "dal"
    # # print(print_distance(s1, s2))
    # # print(distance(s1, s2))
    # print(levenshtien_distance(s1, s2))