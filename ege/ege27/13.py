from functools import cache
from time import time

tim = time()


@cache
def two_or_seven(number):
    return_obj = set()
    if number % 7 == 0:
        return_obj.add(7)
    if number % 2 == 0:
        return_obj.add(2)
    return return_obj


def last_n(number, some_counter):
    for i in range(len(some_counter)):
        if some_counter[-i - 1] <= number - 7:
            return len(some_counter) - i
    return None


def first_n(number, some_counter):
    for i in range(len(some_counter)):
        if some_counter[i][1] > number[1] + 6:
            return i
    return None


strings = []
with open('13/27-13b.txt', 'r') as file_a:
    d = int(file_a.readline())
    counter = 0
    while 1:
        try:
            x = two_or_seven(int(file_a.readline()))
            if x:
                strings.append([x, counter])
            counter += 1
        except:
            break

two_counter = []
seven_counter = []
counter = 0
for i in strings:
    if i[0] == {2, 7}:
        two_counter.append(i[1])
        seven_counter.append(i[1])
        if i[1] > 6:
            counter += i[1] - 6
        t = d - i[1] - 7 - (len(strings) - first_n(i, strings))
        if t > 0:
            counter += t
    elif i[0] == {2}:
        two = last_n(i[1], seven_counter)
        if two is not None:
            counter += two
        two_counter.append(i[1])
    elif i[0] == {7}:
        seven = last_n(i[1], two_counter)
        if seven is not None:
            counter += seven
        seven_counter.append(i[1])
print(counter)

print(time() - tim)
