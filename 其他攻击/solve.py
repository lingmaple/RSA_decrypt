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


def solve(N, p, q, e, c):
    phi = (p - 1) * (q - 1)
    inv = mod_inverse(e, phi)
    return pow(c, inv, N)


if __name__ == "__main__":
    with open("其他攻击/Frame1", "rb") as file:
        nums = file.read()
        N1 = int(nums[0:256].strip(), 16)
        e1 = int(nums[256:512].strip(), 16)
        c1 = int(nums[512:768].strip(), 16)

    with open("其他攻击/Frame18", "rb") as file:
        nums = file.read()
        N2 = int(nums[0:256].strip(), 16)
        e2 = int(nums[256:512].strip(), 16)
        c2 = int(nums[512:768].strip(), 16)

    p = gcd(N1, N2)
    q1 = N1 // p
    q2 = N2 // p

    plaintext1 = solve(N1, p, q1, e1, c1)
    plaintext2 = solve(N2, p, q2, e2, c2)
    # print("plaintext:%x" % plaintext1)
    print("%s:" % hex(plaintext1)[18:26])
    print("%s" % long_to_bytes(plaintext1)[-8:])
    # print("plaintext:%x" % plaintext2)
    print("%s:" % hex(plaintext2)[18:26])
    print("%s" % long_to_bytes(plaintext2)[-8:])
