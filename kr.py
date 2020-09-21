def pk_p(n, p, k):
    outp = ''
    for i in n:
        st = ''
        if i.isdigit():
            b = int(i)
        else:
            b = ord(i) - 55
        while b:
            ost = b % p
            st = str(ost) + st
            b //= p
        outp += '0' * (k - len(st)) + st
    return outp.lstrip("0")


def p_pk(n, p, k):
    outp = ""
    n = '0' * ((k - len(n) % k) % k) + n
    for i in range(len(n) // k):
        num = n[i * k: (i + 1) * k]
        mult = 1
        s = 0
        for j in range(k - 1, -1, -1):
            s += int(num[j]) * mult
            mult *= p
        if s >= 10:
            outp += chr(s + 55)
        else:
            outp += str(s)
    return outp
