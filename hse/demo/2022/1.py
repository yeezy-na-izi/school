carriage_dict = dict()
subsequence = list()
for i in range(int(input())):
    information = input().split()
    if information[0] == 'add':
        subsequence.append([int(information[1]), information[2]])
        if information[2] in carriage_dict:
            carriage_dict[information[2]] += int(information[1])
        else:
            carriage_dict[information[2]] = int(information[1])
    elif information[0] == 'delete':
        count = int(information[1])
        while count != 0:
            if count < subsequence[-1][0]:
                subsequence[-1][0] -= count
                carriage_dict[subsequence[-1][1]] -= count
                count = 0
            else:
                carriage_dict[subsequence[-1][1]] -= subsequence[-1][0]
                count -= subsequence[-1][0]
                subsequence = subsequence[:-1]
    elif information[0] == 'get':
        if information[1] in carriage_dict:
            print(carriage_dict[information[1]])
        else:
            print(0)
print(carriage_dict)
