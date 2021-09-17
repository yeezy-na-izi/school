x = [i for i in range(2020, 647038) if sum([int(j) for j in str(i)]) < 10 and min(str(i)) not in str(i)[:3]]
print(len(x), sum(x) / len(x))
