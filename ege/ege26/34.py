with open('26data/26-j6.txt') as input_file:
    int(input_file.readline()) * 0.9
    files = [int(i) for i in input_file]
    files.sort()
    started_sum = sum(files) * 0.9
counter = -1
output = 0
for i in range(len(files)):
    if started_sum - sum(files[i:]) * 0.8 <= 0:
        output = files[i - 1]
        started_sum -= sum(files[i:]) * 0.8 - files[i - 1]
        break
    else:
        started_sum -= files[i]
        counter += 1
print(counter)
print(max(files))
print(started_sum * 1.25 + output)
