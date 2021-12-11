with open('26data/26-39.txt') as input_file:
    count, summa = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file])
    counter = 0
    for i in values:
        if 180 <= i <= 200:
            summa -= i
            counter += 1
    print(summa)
    for i in values:
        if summa - i < 0:
            break
        counter += 1
        summa -= i
    print(values.count(129))
    print(counter)
    print(summa)
