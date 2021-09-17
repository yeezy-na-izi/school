for i in range(int(input())):
    n, d = [int(x) for x in input().split()]
    x = (n + 1 // 2)
    y = x // (d + 1)
    print(y)
