def pprint(lst):
    for i in lst:
        print(*[f'{j:4d}' for j in i], sep="")
    print()


n = int(input())
m = int(input())
matrix = [[j + 1 + n * i for j in range(m)] for i in range(n)]
x = len(matrix[0])
for i in range(x):
    matrix[i] = matrix[i][x // 2:] + matrix[i][:x // 2]
pprint(matrix)
