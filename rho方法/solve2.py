# -*- coding: utf-8 -*-


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = extended_gcd(b, a % b)
    return d, y, x - (a // b) * y


def mod_inverse(a, m):
    d, x, y = extended_gcd(a, m)
    if d != 1:
        raise ValueError()
    return x % m


def mapx(x, n):
    x = (pow(x, n - 1, n) + 3) % n  # pow(x,n-1,n)是为了减小数值，加速运算，
    return x


def pollard_rho(x1, x2, n):
    while True:
        x1 = mapx(x1, n)
        x2 = mapx(mapx(x2, n),n)
        p = gcd(x1 - x2, n)
        if p == n:
            print("fail")
            return
        elif p != 1:
            print("p: " + str(p))
            print("q: " + str(n / p))
            break


def decrypt(p, q, e, c, N):
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    plaintext = pow(c, d, N)
    return plaintext


if __name__ == "__main__":
    for i in [6, 19]:
        with open("rho方法/Frame{}".format(i), "rb") as file:
            nums = file.read()
            N = int(nums[0:256].strip(), 16)
            e = int(nums[256:512].strip(), 16)
            c = int(nums[512:768].strip(), 16)

            p = pollard_rho(1, 1, N)
            q = N // p
            print("p*q==N? {}".format(p * q == N))
            plaintext = decrypt(p, q, e, c, N)
            print("%x" % plaintext)
