def mtrx_snake(i, j, n, m):
    k = min(i, j, n - i - 1, m - j - 1)

    if k == i:
        return 4 * (k * m - k ** 2) + j - k + 1
    elif k == j:
        return 4 * (k * n - k ** 2) + 4 * m - 7 * k - i - 3
    elif k == m - j - 1:
        return 4 * (k * m - k ** 2) + m - 3 * k + i
    elif k == n - i - 1:
        return 4 * (k * n - k ** 2) + 3 * n - 5 * k - j - 2


n = int(input())
m = int(input())
mtrx = [[0 for j in range(m)] for i in range(n)]

print()
for i in range(n):
    for j in range(m):
        mtrx[i][j] = mtrx_snake(i, j, n, m)
        print(mtrx[i][j], end='\t')
    print()
