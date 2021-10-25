spisok = [0] * 3001
spisok[2] = 1


def plus_1(x):
    return x + 1


def mul_3(x):
    return x + 3


def mul_4(x):
    return x + x - 1


# 1 10 25
# i = 2
# [0, 1, 1, 2, 3, 3, 4]
for i in range(1, 3000):
    try:
        spisok[mul_4(i)] += spisok[i]
    except:
        pass
    try:
        spisok[mul_3(i)] += spisok[i]
    except:
        pass
    try:
        spisok[plus_1(i)] += spisok[i]
    except:
        pass

print(spisok[19])
# x = spisok[10]
# spisok = [0] * 123456
# spisok[10] = 1
# for i in range(10):
#     ...
# print(x * spisok[25])
