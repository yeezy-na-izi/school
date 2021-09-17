output = []
for i in range(4, 13):
    x = 3 ** i
    if len(set(str(x))) != len(str(x)):
        output.append(x)
print(output)
for i in output:
    x = sum([int(j) for j in str(i)])
    print(x)