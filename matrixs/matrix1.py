def simple(i):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return 'NO'
    return 'YES'


print(simple(int(input())))
