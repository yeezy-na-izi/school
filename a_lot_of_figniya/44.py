x = [i for i in range(3912, 9194) if sum([int(j) for j in str(i)]) % 9 == 0 and i % (16 * 16) != 33]
print(len(x), x[-1])