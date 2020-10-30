number = int(input())
listic = [0] * number
for i in range(number):
    a = int(input()) - 1
    listic[a] = number - i
[print(i) for i in listic]