with open('26data/26-4.txt') as input_file:
    summa, count = [int(i) for i in input_file.readline().split()]
    values = sorted([int(i) for i in input_file])
    counter = 0
    for i in values:
        if summa - i < 0:
            number = summa + values[counter - 1]
            break
        counter += 1
        summa -= i
    new_counter = 0
    max_value = 0
    for i in values[counter:]:
        if number >= i:
            max_value = i
        else:
            break
    print(counter, max_value)
