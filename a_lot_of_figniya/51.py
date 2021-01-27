x = [i for i in range(7 ** 6, 7 ** 7) if i % 3 == 2 and i % 8 != 3 and i % 12 != 5]
print(len(x), x[-1])