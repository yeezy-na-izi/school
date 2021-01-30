x = [i for i in range(2848, 109500) if '9' in str(i) and sum([int(j) for j in str(i) if int(j) > 5]) % 3]
print(len(x))
for i in x[::-1]:
    if str(i)[-1] == '8':
        print(i)
        break
