x = [i for i in range(1529, 9483) if i % 4 == 1 and i % 5 == 3]
print(x[0], sum(x))

# 31
x = [i for i in range(5 ** 5, 10000) if i % 25 == 11 or i % 25 == 13]
print(len(x), x[0])

# 32
x = [i for i in range(1000, 6 ** 4) if i % 36 == 9 or i % 36 == 10]
print(len(x), x[-1])

# 40
x = [i for i in range(1871, 9198) if len(str(i)) != (len(hex(i)) - 2) and (i % 9 == 4 or i % 9 == 2)]
print(len(x), x[0])

# 41
x = [i for i in range(2371, 9433) if (i % 64 == 13 or i % 64 == 15) and i % 5 and i % 3]
print(len(x), x[-1])

# 42
x = [i for i in range(2371, 9433) if (i % 64 == 13 or i % 64 == 15) and i % 5 and i % 3]
print(len(x), x[0])
