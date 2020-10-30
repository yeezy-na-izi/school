for x in range(1000):
    n = x
    a = 0

    b = 0

    i = 0

    while x > 0:

        i = i + 1

        c = x % 10

        if i % 2 == 0:

            a = a + c

        else:

            b = b + c

        x = x // 10
    if a == 3 and b == 2:
        print(n)

