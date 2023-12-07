# -*- coding: utf-8 -*-
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


def decrypt(p, q, e, c, N):
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    plaintext = pow(c, d, N)
    return plaintext


if __name__ == "__main__":
    with open("rho p-1方法/Frame2", "rb") as file:
        nums = file.read()
        N = int(nums[0:256].strip(), 16)
        e = int(nums[256:512].strip(), 16)
        c = int(nums[512:768].strip(), 16)

    r, k = 2, 2
    while True:
        r = pow(r, k, N)
        res = gcd(r - 1, N)
        if res != 1 and res != N:
            q = N // res
            break
        k += 1
    plaintext = decrypt(res, q, e, c, N)
    # print("plaintext:%x" % plaintext)
    print("%s:" % hex(plaintext)[18:26])
    print("%s" % long_to_bytes(plaintext)[-8:])
