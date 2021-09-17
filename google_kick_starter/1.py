from math import prod

x = int(input())
alf = 'abcdefghijklmnopqrstuvwxyz'
for i in range(x):
    z = []
    s, n = [int(_) for _ in input().split()]
    word = [alf.index(i) for i in input()]
    q = []
    if len(word) == 1:
        print(f'Case #{i + 1}: {word[0] - 1}')
        break
    for j in range((len(word) + 1) // 2):
        q.append(min(word[j], word[-j - 1]) + 1)
    print(f'Case #{i + 1}: {prod(q)}')
