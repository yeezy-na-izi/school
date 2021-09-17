from random import random
from time import time

from numba import njit

t = time()
all_point = 10000000000


@njit(fastmath=True)
def some_func(all_point):
    point_in_circle = 0
    for i in range(all_point):
        x = random()
        y = random()
        if x * x + y * y <= 1:
            point_in_circle += 1
    return point_in_circle


print(some_func(all_point) * 4 / all_point)
print(time() - t)


