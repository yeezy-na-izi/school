all_numbers = 0
numbers_two = 0
numbers_three = 0
numbers_six = 0
for i in range(int(input())):
    number = int(input())
    if number % 6 == 0:
        numbers_six += 1
    elif number % 3 == 0:
        numbers_three += 1
    elif number % 2 == 0:
        numbers_two += 1
    else:
        all_numbers += 1
# print(f'{all_numbers = }\n{numbers_two = }\n{numbers_three = }\n{numbers_six = }')
print((all_numbers + numbers_two + numbers_three) * numbers_six + sum(range(numbers_six)) + numbers_two * numbers_three)
