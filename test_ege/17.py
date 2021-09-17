def check(n):
    counter = 0
    for i in [7, 11, 13, 19]:
        if n % i:
            counter += 1
    return counter == 2


x = []
for i in range(20000, 30001):
    if check(i):
        x.append(i)
print(len(x), sum(x) / len(x))
