def check(n):
    for j in range(2, int(n ** 0.5 + 1)):
        if n % j == 0 and j != n // j and j * (n // j) == n and prime(j) and prime(n//j):
            return True
    return False


def prime(n):
    for w in range(2, int(n ** 0.5 + 1)):
        if n % w == 0:
            return False
    return True


q = []
for i in range(125697, 190235):
    if check(i):
        q.append(i)
print(max(q), len(q))
