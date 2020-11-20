def shfr(n):
    st = ""
    k = ""
    for i in n:
        st += '0' + bin(ord(i))[2::]
    st += '0' * (15 - len(st) % 15)
    for i in range(0, len(st), 15):
        k += (chr(int(st[i:i + 15], 2)))
    return k


def deshfr(n):
    st = ""
    k = ""
    for i in n:
        st += '0' * (15 - len(bin(ord(i))[2::])) + bin(ord(i))[2::]
    for i in range(0, len(st), 8):
        k += (chr(int(st[i:i + 8], 2)))
    return k


sv = [str(i) for i in input("Введите предложение ").split()]
kl = int(input("Если нужно зашифровать напишите 1, если расшифровать 2 "))
if kl == 1:
    for i in sv:
        print(shfr(i), end=" ")
if kl == 2:
    for i in sv:
        print(deshfr(i), end=" ")
