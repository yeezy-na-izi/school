summa1 = 0
summa2 = 0
summa3 = 0
min_delta1 = 1000000
min_delta2 = 1000000
for i in range(int(input())):
    data = [int(j) for j in input().split()]
    data.sort()
    summa1 += data[0]
    summa2 += data[1]
    summa3 += data[2]

    delta1 = data[2] - data[1]
    if delta1 < min_delta1 and delta1 % 2:
        min_delta2 = min_delta1
        min_delta1 = delta1
    elif delta1 % 2 and delta1 < min_delta2:
        min_delta2 = delta1

    delta2 = data[2] - data[0]
    if delta2 < min_delta1 and delta2 % 2:
        min_delta2 = min_delta1
        min_delta1 = delta2
    elif delta2 % 2 and delta2 < min_delta2:
        min_delta2 = delta2

if summa2 % 2 == 0 and summa1 % 2 == 0:
    print(summa3)
elif (summa1 + summa2) % 2:
    print(summa3 - min_delta1)
else:
    print(summa3 - min_delta1 - min_delta2)
