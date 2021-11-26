x = [i for i in range(4563, 7913) if not i % 7 and sum([int(j) for j in str(i)[::3]]) > 10]
print(len(x), x[-1])
