with open('26data/26-k4.txt') as input_file:
    useless, winners = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file], reverse=True)
    print(int(sum(values[winners:winners * 2]) / winners), int(sum(values[:winners]) / winners))
