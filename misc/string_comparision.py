def moveRobots(s1, s2):
    # code here
    n = len(s1)
    i = n - 1
    j = len(s2) - 1
    ans = 0
    while i >= 0 and j >= 0:
        s1t = s1[i].isalpha()
        s2t = s2[j].isalpha()
        print(i, j, s1[i], s2[j])
        if s1[i] == s2[j]:
            i -= 1
            j -= 1
        elif s1t and s2t and s1[i] != s2[j]:
            return False
        elif not s1t and s2t:
            i -= 1
        elif s1t and not s2t:
            j -= 1
    print("f", i, j)
    return True

if __name__ == "__main__":
    s1 = "#B#A#"
    s2 = "##BA#"
    #print(moveRobots(s1,s2))
    print(moveRobots("#A#B#B#", "#A#B#B"))