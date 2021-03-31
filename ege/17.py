def simple_del(number):
    y = set()
    for q in range(2, int((number ** 0.5)) + 1):
        if number % q == 0:
            if simple_number(number / q):
                y.add(number / q)
            if simple_number(q):
                y.add(q)
    if len(y) == 3:
        return True
    return False


def simple_number(number):
    for j in range(2, int(number ** 0.5 + 1)):
        if not number % j:
            return False
    return True


x = []
for i in range(10001, 50001):
    if simple_del(i):
        x.append(i)
print(len(x))
print(x[0])
