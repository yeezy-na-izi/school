from copy import deepcopy

n, sec = [int(i) for i in input().split()]
a = [[0 for i in range(n + 2)]]
for i in range(n):
    a.append([0] + [int(i) for i in input().split()] + [0])
a.append([0 for i in range(n + 2)])
b = []
for _ in range(sec):
    b = [[0 for i in range(n + 2)]]
    for i in range(1, n + 1):
        b.append([0])
        for j in range(1, n + 1):
            x = a[i - 1][j - 1] + a[i][j - 1] + a[i + 1][j - 1] + a[i - 1][j] + a[i + 1][j] + a[i - 1][j + 1] + a[i][
                j + 1] + a[i + 1][j + 1]
            if x == 3:
                b[-1].append(1)
            elif x == 2 and a[i][j] == 1:
                b[-1].append(1)
            else:
                b[-1].append(0)
        b[-1].append(0)
    b.append([0 for i in range(n + 2)])
    a = deepcopy(b)
for i in a[1:-1]:
    print(*i[1:-1])
