

def reverse(s):
    t = list(s)
    for i in range(len(t)//2):
        t[i],t[len(t)-i-1] = t[len(t)-i-1], t[i]
    print("".join(t))

if __name__ == "__main__":
    s= "CareerMonk Publications"
    reverse(s)