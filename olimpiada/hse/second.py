import time

import self as self

qwe = time.time()
numbers = set()
number = 0
max_number = 0
devision_max_on_number = 0
for i in range(1, 100000000):
    n_devisions = 1
    x = i
    n_max = 1
    while x != 1:
        if x not in numbers:
            numbers.add(x)
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
                if x / i > n_devisions:
                    n_devisions = x / i
                    n_max = x
        else:
            break
    if n_devisions > devision_max_on_number:
        devision_max_on_number = n_devisions
        max_number = n_max
        number = i
print(devision_max_on_number)
print(max_number)
print(number)
print(time.time() - qwe)