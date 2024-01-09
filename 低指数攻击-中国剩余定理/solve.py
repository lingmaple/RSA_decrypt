# -*- coding: utf-8 -*-
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def chinese_remainder(p, s):
    if len(p) != len(s):
        raise RuntimeError("数组不等长")

    N = 1
    for i in range(len(p)):
        N *= s[i]

    x = 0
    for i in range(len(p)):
        Ni = N // s[i]
        gcd, xi, _ = extended_gcd(Ni, s[i])
        if gcd != 1:
            raise RuntimeError("b[i]不互质")
        x += p[i] * xi * Ni

    m = iroot(x % N, 5)[0]  # 开五次方
    return m


if __name__ == "__main__":
    n = []
    c = []

    for i in [3, 8, 12, 16, 20]:
        with open("低指数攻击-中国剩余定理/Frame{}".format(i), "rb") as file:
            nums = file.read()
            n.append(int(nums[0:256].strip(), 16))
            c.append(int(nums[512:768].strip(), 16))

    plaintext = chinese_remainder(c, n)
    # print("plaintext:%x" % plaintext)
    print("%s:" % hex(plaintext)[18:26])
    print("%s" % long_to_bytes(plaintext)[-8:])
