x = [i for i in range(-7018, -3790) if not i % 6 and i % 7 and i % 19 and i % 10 != 2]
print(len(x), x[0])