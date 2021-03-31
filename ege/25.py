from numba import njit
from time import time

sec = time()


@njit
def strange_del(number):
    del_set = set()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            if (number // i) % 2 == 1:
                del_set.add(number // i)
            if i % 2 == 1:
                del_set.add(i)
        if len(del_set) > 5:
            return False
    if len(del_set) == 5:
        print(number, del_set)
        return True
    return False


x = []
for i in range(45000000, 50000001):
    if strange_del(i):
        x.append(i)
print(*x, sep='\n')
print(time() - sec)
