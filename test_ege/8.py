x = list('здание')
counter = 0
for a1 in x:
    for a2 in x:
        for a3 in x:
            for a4 in x:
                for a5 in x:
                    for a6 in x:
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if len(word) == len(
                            set(word)) and 'аи' not in word and 'ае' not in word and 'иа' not in word and 'ие' not in word and 'еи' not in word and 'еа':
                            counter += 1
print(counter)