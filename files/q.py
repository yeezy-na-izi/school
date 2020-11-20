a = open('input.txt', 'r', encoding='UTF-8')
b = open('output.txt', 'w')

listic = dict()
listic['9'] = 0
listic['10'] = 0
listic['11'] = 0
for stroka in a:
    stroka = stroka.split()
    if listic[stroka[2]] < int(stroka[3]):
        listic[stroka[2]] = int(stroka[3])

m = max(listic)
for i in listic:
    print(listic[i], end=' ', file=b)
