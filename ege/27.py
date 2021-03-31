one = []
two = []
three = []
for i in range(int(input())):
    x = int(input())
    if x % 3 == 0:
        one.append(x)
        one.sort()
        if len(one) > 3:
            one = one[1:]
    elif x % 3 == 1:
        two.append(x)
        two.sort()
        if len(two) > 3:
            two = two[1:]
    else:
        three.append(x)
        three.sort()
        if len(three) > 3:
            three = three[1:]
print(sum(one))
print(sum(two))
print(sum(three))
print(three[-1] + two[-1] + one[-1])
# a 2697
# b 299986167

