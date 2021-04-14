from timeit import timeit

q = 0
for i in range(100):
    q += timeit('x = sum(range(10))')

z = 0
for i in range(10):
    z += timeit('x = sum(range(100))')
print(q)
print(z)