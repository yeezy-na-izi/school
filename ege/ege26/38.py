with open('26data/26-j9.txt') as input_file:
    started_sum, useless = [int(i) for i in input_file.readline().split()]
    files = [int(i) for i in input_file]
    files.sort()

counter = 0
last = 0
for i in range(len(files) // 2):
    if started_sum - files[-i - 1] < 0:
        break
    else:
        counter += 1
        started_sum -= files[-i - 1]
        last = files[-i - 1]
        if started_sum - files[i] < 0:
            break
        else:
            counter += 1
            started_sum -= files[i]
            last = files[i]
print(counter)
print(last)