x = [i for i in range(100001, 900010) if i % 7 + i % 10 == 10 and not i % 11 and i % 5]
print(len(x), x[-1])