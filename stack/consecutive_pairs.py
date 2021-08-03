
def pairWiseConsecutive(l):
    # add code here
    c = 0
    s = []
    while l:
        d = l.pop()
        c += 1
        s.append(d)
    if c % 2 > 1:
        return False
    incr = c - (c % 2)
    while incr:
        d1 = s.pop()
        d2 = s.pop()
        incr -= 2
        l.append(d1)
        l.append(d2)
        if d1 > d2:
            diff = d1 - d2
        else:
            diff = d2 - d1
        if diff != 1:
            return False
    if s:
        l.append(s.pop())
    return True

if __name__ == "__main__":
    print(pairWiseConsecutive([4,5,-2,-3,11,10,5,6,20]))