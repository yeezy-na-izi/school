with open('27data/80/27-80b.txt') as input_file:
    first = []
    last = []
    last_index = False
    all_numbers = []
    count_5 = 0
    input_file.readline()
    for i in input_file:
        number = int(i)
        all_numbers.append(number)
        if count_5 < 1:
            first.append(number)
        if number % 5 == 0:
            count_5 += 1
            # last_index = number
        if count_5 == 20206:
            last_index = True
        if last_index:
            last.append(number)

print(count_5)

print(first)
print(last)
print(sum(all_numbers) - min(sum(first), sum(last)))