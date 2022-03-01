def from_big_to_small(n, p, k):
    outp = ''
    for i in n:
        st = ''
        if i.isdigit():
            b = int(i)
        else:
            b = ord(i) - 55
        while b:
            ost = b % p
            st = str(ost) + st
            b //= p
        outp += '0' * (k - len(st)) + st
    return outp.lstrip("0")


def from_small_to_big(n, p, k):
    outp = ""
    n = '0' * ((k - len(n) % k) % k) + n
    for i in range(len(n) // k):
        num = n[i * k: (i + 1) * k]
        mult = 1
        s = 0
        for j in range(k - 1, -1, -1):
            s += int(num[j]) * mult
            mult *= p
        if s >= 10:
            outp += chr(s + 55)
        else:
            outp += str(s)
    return outp


def rod_cc(number, cc, degree, boolean):
    if boolean == '1':
        main_def = from_small_to_big
    else:
        main_def = from_big_to_small
    print(main_def(number[0], cc, degree), end='')
    if len(number) > 1:
        print(',', end='')
        number = number[1]
        print(
            main_def(number.ljust((len(number) + degree - len(number) % degree) * int(len(number) % degree != 0), '0'),
                     cc,
                     degree))
