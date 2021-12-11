with open('26data/26-k3.txt') as input_file:
    useless, winners, priser = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file], reverse=True)
    print(values[priser + winners - 1], values[winners - 1])
