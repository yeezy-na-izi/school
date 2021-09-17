from sys import stdin

slot = int(input())
sums = []
for line in stdin:
    x = [int(i) for i in line.split()[-3:]]
    if min(x) >= 40:
        sums.append(sum(x))
if len(sums) <= slot:
    print(0)
else:
    sums.sort()
    x = sums[-slot:]
    if sums.count(x[0]) > slot:
        if sums[-1] != x[0]:
            print(1)
        else:
            try:
                print(x[0])
            except:
                print(1)
    elif x[0] in sums[:-slot]:
        print(x[0])
    else:
        print(0)
