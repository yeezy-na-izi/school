for i in range(500000, 1000001):
    mx = int(i ** 0.5) + 1
    cot = 0
    a = []
    for j in range(2, mx):
        if i % j == 0 and i // j - j < 91:
            cot += 1
            a.append(i // j)
        if cot == 3:
            print(i, a[0])
            break
