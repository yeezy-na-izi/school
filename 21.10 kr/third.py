from decimal import Decimal


def for_integer(integer_part, degree):
    number_to_return = ''
    if integer_part == 0:
        return '0'
    while integer_part:
        number_to_return += str(integer_part % degree)
        integer_part //= degree
    number_to_return = number_to_return[::-1]
    while number_to_return.startswith('0'):
        number_to_return = number_to_return[1:]
    return number_to_return


number = input().split('.')
сс = 3  # здесь поменять систему счистления
result = ''
ind = 0
f = False
if len(number) == 1:
    print(for_integer(int(number[0]), сс))
    exit()
else:
    float_part = Decimal('0.' + number[1])
    r = 0
    m = [float_part]
    i = 0
    f = True
    while float_part > 0 and i < 32:
        d = int(float_part * сс)
        result += str(d)
        float_part = float_part * сс - d
        if float_part in m:
            f = False
            ind = m.index(float_part)
            break
        m.append(float_part)
        i += 1
if f:
    print(for_integer(int(number[0]), сс) + '.' + result)
else:
    print(for_integer(int(number[0]), сс) + '.' + result[:ind] + '(' + result[ind:] + ')')
