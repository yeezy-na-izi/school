counter = 0
for a in range(1, 1001):
    b = 0
    for x in range(1, 1000):
        if not(not a % 7 and not 240 % x) <= (a % x <= 780 % x):
            b = 1
    if not b:
        counter += 1
print(counter)