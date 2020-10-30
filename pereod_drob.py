def period(n, x=2):
    degree = 1
    integer = 0
    fractional = ['', '']
    y = 0
    z = 0
    n = n.split('.')
    for i in range(len(n[1])):
        if n[1][i] == '(':
            fractional[1] = n[1][i + 1:-1]
            break
        else:
            fractional[0] += n[1][i]
    for i in range(len(n[0]) - 1, -1, -1):
        if n[0][i].isdigit():
            integer += int(n[0][i]) * degree
        else:
            integer += (ord(n[0][i]) - 55) * degree
        degree *= x
    degree = 1
    deli = 2 ** (len(fractional[1]) + len(fractional[0])) - 2 ** len(fractional[0])

    for i in range(len(fractional[0]) - 1, -1, -1):
        if fractional[0][i].isdigit():
            y += int(fractional[0][i]) * degree
        else:
            y += (ord(fractional[0][i]) - 55) * degree
        degree *= x
    degree = 1
    if fractional[1] != '':
        fractional[1] = fractional[0] + fractional[1]
        for i in range(len(fractional[1]) - 1, -1, -1):
            if fractional[1][i].isdigit():
                z += int(fractional[1][i]) * degree
            else:
                z += (ord(fractional[1][i]) - 55) * degree
            degree *= x
    else:
        z = 2 ** len(n[1])
    if deli == 0:
        fractional = y / z
    else:
        fractional = (z - y) / deli
    print(integer + fractional)


period(input())
