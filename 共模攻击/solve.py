# -*- coding: utf-8 -*-
from Crypto.Util.number import long_to_bytes


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


def solve(n, c1, c2, e1, e2):
    d, s1, s2 = extended_gcd(e1, e2)

    # 求模逆元
    if s1 < 0:
        s1 = -s1
        c1 = mod_inverse(c1, n)

    elif s2 < 0:
        s2 = -s2
        c2 = mod_inverse(c2, n)

    m = pow(c1, s1, n) * pow(c2, s2, n) % n
    return m


if __name__ == "__main__":
    with open("共模攻击/Frame0", "rb") as file:
        nums = file.read()
        N = int(nums[0:256].strip(), 16)
        e1 = int(nums[256:512].strip(), 16)
        c1 = int(nums[512:768].strip(), 16)

    with open("共模攻击/Frame4", "rb") as file:
        nums = file.read()
        N = int(nums[0:256].strip(), 16)
        e2 = int(nums[256:512].strip(), 16)
        c2 = int(nums[512:768].strip(), 16)

    plaintext = solve(N, c1, c2, e1, e2)
    # print("plaintext:%x" % plaintext)
    print("%s:" % hex(plaintext)[18:26])
    print("%s" % long_to_bytes(plaintext)[-8:])
