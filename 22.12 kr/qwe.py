count = 1

for i in range(0, 1048576):
    q = hex(i)[2:]
    if len(q) == 5:
        if len(set(q)) == len(q):
            for k in range(len(q) - 1):
                if int(q[k], 16) % 2 == 0 and int(q[k + 1], 16) % 2 == 0:
                    break
                if int(q[k], 16) % 2 == 1 and int(q[k + 1], 16) % 2 == 1:
                    break
            else:
                print(i)
                count += 1
print()
print(count)