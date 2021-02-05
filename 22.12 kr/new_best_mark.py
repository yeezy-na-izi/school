n, m = [int(i) for i in input().split()]
for i in range(n):
    for j in range(m):
        print((1 - ((i + j) % 2)) * (j + (m * i) + 2) // 2, end='\t')
    print()

