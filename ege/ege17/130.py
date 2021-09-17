x = [i for i in range(5883, 15907) if i % 13 and (i % 9 == 0 or i % 23 == 0) and i % 18 and i % 19 and i % 22]
print(len(x), x[-1])
