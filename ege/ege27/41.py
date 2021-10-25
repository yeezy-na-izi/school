summa1 = 0
summa2 = 0
summa3 = 0
min_delta = 1000000
for i in range(int(input())):
    data = [int(j) for j in input().split()]
    data.sort()
    summa1 += data[0]
    summa2 += data[1]
    summa3 += data[2]
    delta1 = data[1] - data[0]
    if delta1 < min_delta and delta1 % 2:
        min_delta = delta1

    delta1 = data[2] - data[0]
    if delta1 < min_delta and delta1 % 2:
        min_delta = delta1

if (summa3 + summa2) % 2:
    print(summa1)
else:
    print(summa1 + min_delta)
