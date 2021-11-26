x = [i for i in range(5903, 174203) if
     len(set(str(i))) == len(str(i)) and len([int(j) for j in str(i) if int(j) > 4]) == 3]
print(len(x))
print(x)