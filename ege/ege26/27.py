with open('26data/26-J2.txt') as input_file:
    useless = int(input_file.readline())
    values = sorted([int(i) for i in input_file])
    mediana = values[useless // 2]
    averange = sum(values) / useless
    counter = 0
    for i in values:
        if averange <= i <= mediana:
            counter += 1
    print(counter)
