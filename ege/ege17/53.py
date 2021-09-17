x = [i for i in range(10, 1179, 2) if i % 10 not in [0, 2, 6, 8] and i % 100 != 14]
print(sum(x), x[0])
