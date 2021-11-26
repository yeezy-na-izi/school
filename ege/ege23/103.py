def command_1(number):
    return number + 1


def command_2(number):
    return number + 2


def command_3(number):
    return number * 2


variants = [command_1, command_2, command_3]
counter = 0
for x1 in variants:
    for x2 in variants:
        for x3 in variants:
            for x4 in variants:
                for x5 in variants:
                    for x6 in variants:
                        '''Количество вложенных циклов = количеству команд'''
                        number = x1(x2(x3(x4(x5(x6(1))))))  # В центре первоначальное число
                        if number == 20:
                            counter += 1
print(counter)
