def from_small_to_big(number, p, k):
    number = '0' * ((k - len(number) % k) % k) + number
    output = ""
    for i in range(len(number) // k):
        num = number[i * k: (i + 1) * k]
        degree = 1
        s = 0
        for j in range(k - 1, -1, -1):
            s += int(num[j]) * degree
            degree *= p
        if s >= 10:
            output += chr(s + 55)
        else:
            output += str(s)
    return output


number = input()
number = number.split(',')
print(from_small_to_big(number[0], 3, 3), end='')
if len(number) > 1:
    print(',', end='')
    number = number[1]
    print(from_small_to_big(number.ljust((len(number) + 3 - len(number) % 3) * int(len(number) % 3 != 0), '0'), 3, 3))
