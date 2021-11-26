def command_1(number):
    return number + 1


def command_2(number):
    return number + 5


def command_3(number):
    return number * 3


variants = [command_1, command_2, command_3]
all_numbers = set()  # Так как множество не хранит повторяющиеся элементы
for x1 in variants:
    for x2 in variants:
        for x3 in variants:
            for x4 in variants:
                '''Количество вложенных циклов = количеству команд'''
                number = x1(x2(x3(x4(1))))  # В центре первоначальное число
                all_numbers.add(number)

print(len(all_numbers))
