def is_prime(i):
    for j in range(2, int(i ** 0.5) + 1):
        if not i % j:
            return False
    return True


def sum_35(i):
    x = sum([int(j) for j in str(i)])
    if x > 35:
        return True
    return False


def sums(i):
    return sum([int(j) for j in str(i)])


x = [i for i in range(33333, 55555) if is_prime(i) and sum_35(i)]
for i in x:
    print(i, sums(i))
