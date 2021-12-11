with open('26data/26-k5.txt') as input_file:
    useless, cheap, expensive = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file], reverse=True)
    print(values[expensive - 1], int(sum(values[-cheap:]) / cheap))
