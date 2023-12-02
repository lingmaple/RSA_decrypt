from functools import reduce


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def CRT(items):
    N = reduce(lambda x, y: x * y, (i[1] for i in items))
    result = 0
    for a, n in items:
        m = N // n
        d, r, s = extended_gcd(n, m)
        if d != 1:
            raise Exception("Input not pairwise co-prime")
        result += a * s * m
    return result % N, N


p = []
s = []

for i in [3, 8, 12, 16, 20]:
    with open("Frame{}".format(i), "rb") as file:
        nums = file.read()
        p.append(int(nums[0:256].strip(), 16))

        s.append(int(nums[512:768].strip(), 16))


data = list(zip(p, s))
x, N = CRT(data)
plaintext = gmpy2.iroot(gmpy2.mpz(x), e)[0].digits()
print("明文为：%x" % int(plaintext))
