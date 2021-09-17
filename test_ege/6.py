for x in range(1000):
    S = x
    S = S // 8
    N = 2
    while S <= 102:
        S = S + 4
        N = N * 2 - 1
    if N == 257:
        print(x)
