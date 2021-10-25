n, m = [int(i) for i in input().split()]
matrix = []
# matrix.append([0] * (m + 1))
for i in range(n):
    matrix.append([int(j) for j in input().split()])



flag = 0
for i in range(n):
    if matrix[i][0] == 0:
        flag = 1
    if flag:
        matrix[i][0] = 0

flag = 0
for i in range(m):
    if matrix[0][i] == 0:
        flag = 1
    if flag:
        matrix[0][i] = 0

if matrix[0][0] == 0:
    print('Impossible')
    exit()

for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            x = way[i][j + 1] + way[i + 1][j] - 1
            if x >= 0:
                way[i + 1][j + 1] = x + matrix[i][j]

if way[-1][-1]:
    print(way[-1][-1])
else:
    print('Impossible')
# 3 5
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
