n = int(input())
string = input()
x = ''.join(sorted(set(input())))
vivod = ''
for i in x:
    if string.count(i) > 1:
        vivod += 2
