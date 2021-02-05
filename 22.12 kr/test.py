n, m = [int(i) for i in input().split()]
for i in range(n):
    for j in range(m):
        print((j + (m * i) + 2)  // 2, end=' ')
    print()
