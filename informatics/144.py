def is_prime(i):
    z = []
    for j in range(2, int(i) - 1):
        if not i % j:
            z.append(j)
    x = z[0]
    for q in z[1:]:
        x += 10
        if q != x:
            return False
    return True


def min_del(i):
    for j in range(1, i):
        if i % j:
            return i


def sums(i):
    return sum([int(j) for j in str(i)])


x = [i for i in range(834567, 1143210) if is_prime(i)]
for i in x:
    print(i, min_del(i))

