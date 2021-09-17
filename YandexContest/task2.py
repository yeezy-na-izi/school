n = int(input())
shifr = []
for i in range(n):
    x = input().split()
    shifr.append([int(x[j]) for j in range(len(x)) if i != j])
out = []
for line in shifr:
    q = 0
    for el in line:
        q |= el
    out.append(q)
print(*out)