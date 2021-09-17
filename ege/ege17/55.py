x = [i for i in range(1753, 7420) if i % 13 and i % 11 == 0]
print(len(x), sum(x))
