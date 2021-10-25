strings_count, domino_count = [int(i) for i in input().split()]
dominoes = []
for i in range(strings_count):
    dominoes.append([int(i) for i in input().split()])
print(*dominoes, sep='\n')
variants = []
