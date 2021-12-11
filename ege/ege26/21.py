with open('26data/26-k1.txt') as input_file:
    summa, count = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file], reverse=True)
    print(values[count], sum(values[:count]) * 0.2)