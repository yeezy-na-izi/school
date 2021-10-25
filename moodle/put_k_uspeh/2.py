id_1 = [[], [], []]
id_2 = [[], [], []]
id_3 = [[], [], []]
for i in range(int(input())):
    number = int(input())
    if i % 3 == 0:
        id_1[number % 3].append(number)
    elif i % 3 == 1:
        id_2[number % 3].append(number)
    elif i % 3 == 2:
        id_3[number % 3].append(number)
# print(id_1)
# print(id_2)
# print(id_3)
id_3[0].sort()
output = -1
if len(id_3[0]) >= 2:
    output = id_3[0][-1] + id_3[0][-2]
if id_3[1] and id_3[2]:
    nu = max(id_3[1]) + max(id_3[2])
    if nu > output:
        output = nu
if id_1[0] and id_2[0]:
    nu = max(id_1[0]) + max(id_2[0])
    if nu > output:
        output = nu
if id_1[1] and id_2[2]:
    nu = max(id_1[1]) + max(id_2[2])
    if nu > output:
        output = nu
if id_1[2] and id_2[1]:
    nu = max(id_1[2]) + max(id_2[1])
    if nu > output:
        output = nu
print(output)
