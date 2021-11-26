from math import prod

x = [i for i in range(8800, 55535) if prod([int(j) for j in str(i)]) > 35 and '7' in str(i)]
print(len(x), x[-1])
