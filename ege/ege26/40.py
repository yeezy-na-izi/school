with open('26data/26-39.txt') as input_file:
    count, summa = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file])
    x = summa
    counter = 0
    for i in values:
        if 310 <= i <= 320:
            summa -= i
            counter += 1
    for i in values:
        if summa - i < 0:
            last = i
            break
        counter += 1
        summa -= i
    for i in range(summa, 0, -1):
        if values.count(values[values.index(last) - 1] + i):
            print(counter, x - summa + i)
            break
