number = int(input())
output = []
while number > 1:
    if number % 3 == 0:
        number //= 3
        output.append(3)
    elif number % 2 == 0:
        number //= 2
        output.append(2)
    else:
        number -= 1
        output.append(1)
print(*output[::-1], sep='')
number = int(input())
variants = [[] for i in range(number * 3 + 1)]
for i in range(1, number):

    if not variants[i + 1] or len(variants[i + 1]) >= len(variants[i]) + 1:
        variants[i + 1] = variants[i] + [1]

    if not variants[i * 2] or len(variants[i * 2]) >= len(variants[i]) + 1:
        variants[i * 2] = variants[i] + [2]

    variants[i * 3] = variants[i] + [3]

print(*variants[number], sep='')
