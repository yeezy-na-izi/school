import re

amounts = {}
for i in range(int(input())):
    number = int(''.join(re.findall(r'[0-9]', input())))
    if number in amounts:
        amounts[number] += 1
    else:
        amounts[number] = 1

fil = []
for i in amounts:
    if amounts[i] <= 5:
        fil.append(i)

print(len(fil))
print(*fil, sep='\n')
