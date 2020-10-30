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


def for_period(some_part, degree):
    znam = ''
    chicl = ['', '']
    plus = '0'
    f = True
    for i in some_part[2:-1]:
        if '(' == i:
            f = False
            plus = '9'
        else:
            znam = plus + znam
            if f:
                chicl[1] += i
            chicl[0] += i
    if chicl[1] == '':
        chicl[1] = '0'
    return (int(chicl[0]) - int(chicl[1])) / int(znam)


def from_10_to_p(number, cc):
    result = ''
    ind = 0
    f = False
    if len(number) == 1:
        print(for_integer(int(number[0]), cc))
        exit()
    else:
        if '(' in number[1]:
            float_part = for_period('0.' + number[1], cc)
        else:
            float_part = Decimal('0.' + number[1])
        r = 0
        m = [float_part]
        i = 0
        f = True
        while float_part > 0 and i < 32:
            d = int(float_part * cc)
            result += str(d)
            float_part = float_part * cc - d
            if float_part in m:
                f = False
                ind = m.index(float_part)
                break
            m.append(float_part)
            i += 1
    if str(cc - 1) * 5 in result:
        result = result[:result.index(str(cc - 1) * 5)]
        result = str(int(result) + 1)
    if f:
        print(for_integer(int(number[0]), cc) + '.' + result)
    else:
        print(for_integer(int(number[0]), cc) + '.' + result[:ind] + '(' + result[ind:] + ')')
