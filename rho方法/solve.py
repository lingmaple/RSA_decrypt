# -*- coding: utf-8 -*-
import random
from Crypto.Util.number import long_to_bytes


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


def pollard_rho(n):
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)

    if d == n:
        RuntimeError("None")
        return None
    else:
        # print(d)
        return d


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

            p = pollard_rho(N)
            q = N // p
            # print("p*q==N? {}".format(p * q == N))
            plaintext = decrypt(p, q, e, c, N)
            print("%s:" % hex(plaintext)[18:26])
            print("%s" % long_to_bytes(plaintext)[-8:])
