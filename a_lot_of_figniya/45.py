x = [i for i in range(-9563, -3101) if not i % 7 and i % 11 and i % 23 and i % 10 != 8]
print(len(x), x[0])