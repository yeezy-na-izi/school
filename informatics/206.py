n, m = [int(i) for i in input().split()]


def factorial(x):
    obj = 1
    for i in range(2, x):
        obj *= i
    return obj


print(int(factorial(n + m - 1) // (factorial(n) * factorial(m))))
