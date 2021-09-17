for i in range(int(input())):
    numb = int(input())
    count = 0
    for j in range(1, numb + 1):
        n = 1
        for n in range(1, numb + j * n):
            if (2 * j + n - 1) / 2 * n == numb:
                count += 1
            if (2 * j + n - 1) / 2 * n > numb:
                break
    print(f'Case #{i + 1}: {count}')
