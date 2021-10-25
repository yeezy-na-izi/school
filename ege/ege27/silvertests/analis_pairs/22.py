numbers = [[] for i in range(140)]
for i in range(int(input())):
    number = int(input())
    numbers[number % 140].append(number)
max_7 = 0
max_number_not_max_7 = 0
for i in numbers:
    for j in i:
        if j % 7 == 0 and j > max_7:
            max_7 = j
        elif j > max_number_not_max_7 and j % 140 != max_7 % 140:
            max_number_not_max_7 = j
if max_7 and max_number_not_max_7:
    print(max_7, max_number_not_max_7)
else:
    print(0, 0)
