def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) - 1
    return f(n - 1) + 17


print(f(59102))
