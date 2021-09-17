x = [i for i in range(2595, 8401) if i % 13 and i % 2 == 0]
print(len(x), sum(x))
