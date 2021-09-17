x = [2]
z = 2
count = int(input())
while len(x) != count:
    z += 1
    for i in x:
        if z % i == 0:
            break
    else:
        x.append(z)
print(x[-1])