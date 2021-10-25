print(sorted({2: 3, 100: 2, 99: 2, 101: 2}.items(), key=lambda x: (x[1], x[0])))
