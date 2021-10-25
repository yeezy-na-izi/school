summa = 0
min_delta = 300000
for i in range(int(input())):
    data = [int(j) for j in input().split()]
    data.sort(reverse=True)
    summa += data[0]
    delta1 = data[0] - data[1]
    if delta1 < min_delta and delta1 % 4:
        min_delta = delta1
    delta1 = data[0] - data[2]
    if delta1 < min_delta and delta1 % 4:
        min_delta = delta1
if summa % 4:
    print(summa)
elif min_delta != 300000:
    print(summa - min_delta)
else:
    print(0)
