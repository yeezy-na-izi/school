alphabet = '123456789'
counter = 0
output = set()
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                for e in alphabet:
                    for f in alphabet:
                        n1 = a + b + c + d + e + f
                        n2 = b + c + d + e + f + a
                        if (int(n1) + int(n2)) % 33 == 0:
                            if 525111 <= int(n1) <= 525799:
                                print(f'{a=} {b=} {c=} {d=} {e=} {f=}')
                                counter += 1
                                output.add(int(n1) + int(n2))
print(counter)
print(sorted(output))
print(len(output))