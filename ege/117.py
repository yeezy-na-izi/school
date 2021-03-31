for i in range(10, 100):
    x = bin(i)[2:]
    x += x[-2]
    x += x[1]
    x = int(x, 2)
    if x > 170:
        print(i, x)