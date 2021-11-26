with open('27data/11/27-11b.txt') as file_x:
    summa = 0
    min1 = [1000001] * 2
    min2 = [1000001] * 2
    min3 = 1000001
    min4 = 1000001
    min5 = 1000001
    file_x.readline()
    for i in file_x:
        numbers = sorted([int(j) for j in i.split()])
        summa += max(numbers)
        x = numbers[2] - numbers[1]
        if x % 8 == 1:
            if x < min1[0]:
                min1[1] = min1[0]
                min1[0] = x
            elif x < min2[1]:
                min1[1] = x
        elif x % 8 == 2:
            if x < min2[0]:
                min2[1] = min2[0]
                min2[0] = x
            elif x < min2[1]:
                min2[1] = x
        elif x % 8 == 3:
            min3 = min(min3, x)
        elif x % 8 == 4:
            min4 = min(min4, x)
        elif x % 8 == 5:
            min5 = min(min5, x)
        x = numbers[2] - numbers[0]
        if x % 8 == 1:
            if x < min1[0]:
                min1[1] = min1[0]
                min1[0] = x
            elif x < min2[1]:
                min1[1] = x
        elif x % 8 == 2:
            if x < min2[0]:
                min2[1] = min2[0]
                min2[0] = x
            elif x < min2[1]:
                min2[1] = x
        elif x % 8 == 3:
            min3 = min(min3, x)
        elif x % 8 == 4:
            min4 = min(min4, x)
        elif x % 8 == 5:
            min5 = min(min5, x)
print(summa - min2[0])
print(summa % 8)
print(min1)
print(min2)
print(min3)
print(min4)
print(min5)
