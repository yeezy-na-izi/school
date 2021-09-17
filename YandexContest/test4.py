x = [int(i) for i in input().split()]
for i in x:
    print(bin(i)[2:])
out = []
out2 = []
for i in range(len(x)):
    out.append([])
    out2.append([])
    for j in range(len(x)):
        out[-1].append(-1 if i == j else bin(x[i] & x[j])[2:])
        out2[-1].append(-1 if i == j else x[i] & x[j])
print(*out, sep='\n')
print(*out2, sep='\n')