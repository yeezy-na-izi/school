x = []

for i in range(500000, 1000001):
    f = True
    kol = 0
    k = int(i ** 0.5)
    for j in range(k, k - 51, -1):
        if not i % j:
            if i // j - j <= 90:
                kol += 1
                if kol == 3:
                    if f:
                        dma = i // k
                    break
            else:
                break
    if kol == 3:
        x.append((i, dma))
print(x)
