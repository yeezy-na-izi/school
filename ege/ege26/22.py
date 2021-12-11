with open('26data/26-k2.txt') as input_file:
    summa, count = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file])[count:-count]
    x = sum(values) / len(values)
    for i in values:
        if abs(sum(values) / len(values) - i) < x:
            x = i
    print(i, sum(values) / len(values))
