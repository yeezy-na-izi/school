x, y = [int(i) for i in input().split()]
z = []
for i in range(x):
    z.append(input().split())
k = int(input())
r = int(input())
cooun = 0
for i in z:
    for j in i:
        if len(j) == k:
            if sum(int(w) for w in j) % r == 0:
                cooun += 1
print(cooun)
