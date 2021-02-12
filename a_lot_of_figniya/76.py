x = [i for i in range(1007, 746001) if
     max(str(i)) == str(i)[0] and str(i).count('5') >= 2 and not str(i).count('5') % 2 and str(i).startswith('50')]
print(max(x))
