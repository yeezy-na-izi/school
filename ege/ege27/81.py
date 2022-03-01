way = '27data/81/27-81a.txt'

with open(way) as input_file:
    input_file.readline()
    counter = 0  # Количество элементов которые удовлетвояют условию
    all_numbers = []
    for i in input_file:
        number = int(i)
        all_numbers.append(number)
        if number % 2 == 1:  # меняется от задачи
            counter += 1

with open(way) as input_file:
    input_file.readline()
    d = 13  # меняется от задачи
    count = counter % d  # Насколько больше элементов чем нужно
    counter_copy = counter
    counter = 0  # Количество элементов которые удовлетвояют условию
    start = []
    end = []
    for i in input_file:
        number = int(i)
        if counter < count:
            start.append(number)
        if counter_copy - count <= counter:
            end.append(number)
        if number % 2 == 1:  # меняется от задачи
            counter += 1


def get_min(first_array, second_array, amount):
    second_array = second_array[::-1]  # reverse так как мы идем с конца
    first = []
    su = 0  # промежуточная сумма
    for el in first_array:
        su += el
        if el % 2 == 1:  # меняется от задачи
            first.append(su)
            su = 0
    su = 0  # проме жуточная сумма
    second = []
    for el in second_array:
        su += el
        if el % 2 == 1:  # меняется от задачи
            second.append(su)
            su = 0
    min_sum = float('inf')
    for index in range(amount + 1):
        possible_variant = first[:count - index] + second[:index]
        if sum(possible_variant) < min_sum:
            min_sum = sum(possible_variant)
    return min_sum


print(sum(all_numbers) - get_min(start, end, count))
# Сложность 2 * n + 3 * d(15 строчка) + 1
