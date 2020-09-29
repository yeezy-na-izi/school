import time

start = time.time()


def to_10(n, x):
    st = 1
    z = 0
    q = 0
    n = str(n).split('.')
    if len(n) == 2:
        y = x ** len(n[1])
        for i in range(len(n[1]) - 1, -1, -1):
            if n[1][i].isdigit():
                z += int(n[1][i]) * st
            else:
                z += (ord(n[1][i]) - 55) * st
            st *= x
    else:
        y = 1
    st = 1
    for i in range(len(n[0]) - 1, -1, -1):
        if n[0][i].isdigit():
            q += int(n[0][i]) * st
        else:
            q += (ord(n[0][i]) - 55) * st
        st *= x

    print(z, y)
    z += y * q
    number = convert(z, y)
    print(number)


def convert(numerator, denominator):
    ans = str(numerator // denominator) + "."
    l = {}
    index = 0
    numerator = numerator % denominator
    l[numerator] = index
    t = False
    while t == False:
        if numerator == 0:
            break
        digit = numerator * 10 // denominator
        numerator = numerator * 10 - (numerator * 10 // denominator) * denominator
        if numerator not in l:
            ans += str(digit)
            index += 1
            l[numerator] = index
            t = False
        else:
            ans += str(digit) + ")"
            ans = ans[:l.get(numerator) + len(ans[:ans.index(".") + 1])] + "(" + ans[l.get(numerator) + len(
                ans[:ans.index(".") + 1]):]
            t = True
    return ans


to_10('', 2)
time.sleep(1)
print("--- %s seconds ---" % (time.time() - start))
