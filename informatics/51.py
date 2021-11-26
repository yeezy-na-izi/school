x = [i for i in range(1005, 147871) if '1' not in str(i) and sum([int(j) for j in str(i) if int(j) > 5]) % 3]
print(len(x))
for i in x[::-1]:
    if str(i)[-1] == '8':
        print(i)
        break
