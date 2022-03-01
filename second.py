output = set()


def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1


s = set(eratosthenes(10000))

for i in range(1, 100000):
    for j in range(1, 100):
        output.add(i * j + i + j)
print(sorted(s - output))
