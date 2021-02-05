x, y = [int(i) for i in input().split()]
q = -1
z = []
for i in range(x):
    z.append([int(i) for i in input().split()[:y]])
coun = 0
mi = []
ma = []
for i in range(len(z)):
    mi.append([i, z[i].index(min(z[i]))])
for i in range(y):
    x = []
    for j in z:
        x.append(j[i])
    ma.append([x.index(max(x)), i])
for i in ma:
    if i in mi:
        print(i[0] + 1, i[1] + 1)
