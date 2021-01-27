x = [i for i in range(331, 8752) if len(str(i)) == (len(hex(i)) - 2) and i % 25 and not i % 5]
print(len(x), x[0])