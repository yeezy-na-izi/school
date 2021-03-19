def pprint(lst):
    for i in lst:
        # print(*[f'{j:4d}' for j in i], sep="")
        print(*i)
    print()


n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])
pprint(zip(*a[::-1]))
b = [[0] * n for _ in range(m)]
for i in range(n):
    for j in range(n):
        b[j][n - i - 1] = a[i][j]
pprint(b)