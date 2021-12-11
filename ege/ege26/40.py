with open('26data/26-39.txt') as input_file:
    count, summa = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file])
    counter_new = 0
    for i in values:
        if 310 <= i <= 320:
            summa -= i
            counter_new += 1
    print(summa)
    counter = 0
    for i in values:
        if summa - i < 0:
            break
        counter += 1
        summa -= i
    print(values.index(133))
    print(counter + counter_new)
    print(summa)
