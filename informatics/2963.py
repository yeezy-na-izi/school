number = int(input())
variants = [[] for i in range(number * 3 + 1)]

for i in range(1, number):
    if not variants[i + 1] or len(variants[i + 1]) > len(variants[i]):
        variants[i + 1] = variants[i] + [1]

    if not variants[i * 2] or len(variants[i * 2]) > len(variants[i]):
        variants[i * 2] = variants[i] + [2]

    variants[i * 3] = variants[i] + [3]

print(*variants[number], sep='')
