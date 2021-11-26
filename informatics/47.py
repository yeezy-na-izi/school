x = [i for i in range(1031, 125889) if str(i)[-1] != '5' and int(i ** 0.5) == i ** 0.5]
print(len(x))
for i in x:
    if str(i)[-2:] == '36':
        print(i)
        break