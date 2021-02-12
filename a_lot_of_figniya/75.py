from math import log


x = [i for i in range(138, 603885) if log(i, 3) == int(log(i, 3)) and len(set(str(i))) != len(str(i))]
print(x)
