n, m = [int(i) for i in input().split()]
matrix = []
# matrix.append([0] * (m + 1))
for i in range(n):
    matrix.append([int(j) for j in input().split()])

way = [[0] * m for i in range(n)]
flag = 0
for i in range(n):
    if matrix[i][0] == 0:
        flag = 1
    if flag:
        matrix[i][0] = 0
    else:
        way[i][0] = 1

flag = 0
for i in range(m):
    if matrix[0][i] == 0:
        flag = 1
    if flag:
        matrix[0][i] = 0
    else:
        way[0][i] = 1

for i in range(1, n):
    for j in range(1, m):
        if matrix[i][j]:
            way[i][j] = way[i - 1][j] + way[i][j - 1]

if way[-1][-1]:
    print(way[-1][-1])
else:
    print('Impossible')