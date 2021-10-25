variants = [[0, []] for i in range(1001)]
number, useless = [int(i) for i in input().split()]
bidons = [int(i) for i in input().split()]
variants[0][0] = number


def change_variants(i, bidon):
    if variants[i][0] - bidon >= 0:
        if variants[i + bidon][1]:
            if len(variants[i + bidon][1]) > len(variants[i][1]) + 1:
                variants[i + bidon] = [variants[i][0] - bidon, variants[i][1] + [bidon]]
        else:
            variants[i + bidon] = [variants[i][0] - bidon, variants[i][1] + [bidon]]


for i in range(number + 1):
    for j in bidons:
        change_variants(i, j)

if len(variants[number][1]) == 0:
    print(-1)
else:
    print(len(variants[number][1]))
    print(*sorted(variants[number][1], reverse=True))
