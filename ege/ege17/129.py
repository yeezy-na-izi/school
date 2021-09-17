x = [i for i in range(7525, 13486) if i % 6 and i % 7 == 0 and i % 9 and i % 14 and i % 21]
print(len(x), x[0])
