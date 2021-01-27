x = [i for i in range(2055, 9415) if i % 5 and i % 4 and i % 41 and sum([int(j) for j in str(i % 100)]) != 5]
z = 1
for i in x:
    z *= i
print(x[0], z % 1000)
