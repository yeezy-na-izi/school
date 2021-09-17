from time import time

tim = time()
numbers = []
with open('73/27-73b.txt', 'r') as file_a:
    d = int(file_a.readline())
    for i in range(d):
        numbers.append(int(file_a.readline()))
out_numbers = numbers[::]
max_sum = 0
for i in range(1, d):
    for j in range(d):
        try:
            out_numbers[j] += numbers[j + i]
            if out_numbers[j] % 93 == 0 and out_numbers[j] % 2 and max_sum < out_numbers[j]:
                max_sum = out_numbers[j]

        except:
            break
    if i % 1000 == 0:
        print(i)
        print(time() - tim)
print(max_sum)
print(time() - tim)
