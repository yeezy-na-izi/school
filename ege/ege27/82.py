way = '27data/82/27-82b.txt'


def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    for number in range(5, int(n ** 0.5) + 1, 6):
        if n % number == 0 or n % (number + 2) == 0:
            return False
    return True


with open(way) as input_file:
    input_file.readline()
    counter = 0  # Количество элементов которые удовлетвояют условию
    all_numbers = []
    for i in input_file:
        number = int(i)
        all_numbers.append(number)
        if is_prime(number):  # меняется от задачи
            counter += 1

with open(way) as input_file:
    input_file.readline()
    d = 9  # меняется от задачи
    count = counter % d  # Насколько больше элементов чем нужно
    counter_copy = counter
    counter = 0  # Количество элементов которые удовлетвояют условию
    start = []
    end = []
    for i in input_file:
        number = int(i)
        if counter < count:
            start.append(number)
        if is_prime(number):  # меняется от задачи
            counter += 1
        if counter_copy - count < counter:
            end.append(number)


def get_min(first_array, second_array, amount):
    second_array = second_array[::-1]  # reverse так как мы идем с конца
    first = []
    su = 0  # промежуточная сумма
    for el in first_array:
        su += el
        if is_prime(el):  # меняется от задачи
            first.append(su)
            su = 0
    su = 0  # промежуточная сумма
    second = []
    for el in second_array:
        su += el
        if is_prime(el):  # меняется от задачи
            second.append(su)
            su = 0
    min_sum = 1234567891
    for index in range(amount + 1):
        possible_variant = first[:count - index] + second[:index]
        if sum(possible_variant) < min_sum:
            min_sum = sum(possible_variant)
    return min_sum


print(sum(all_numbers) - get_min(start, end, count))
# Сложность 2 * n + 3 * d(15 строчка) + 1
