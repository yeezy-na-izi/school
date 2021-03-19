def hashh(s):
    n = len(s)
    h = 0
    for i in range(n):
        d = ord(s[i]) - ord("a") + 1
        h = h * 27 + d
    return h


dl = 100
mn = [[] for i in range(dl)]
inp = input()
while inp != "#":
    inp = inp.split()
    ind = hashh(inp[1]) % dl
    if inp[0] == "?":
        if inp[1] not in mn[ind]:
            print("NO")
        else:
            print("YES")
    elif inp[0] == "+":
        if inp[1] not in mn[ind]:
            mn[ind].append(inp[1])
    inp = input()