# -*- coding: utf-8 -*-
from math import isqrt
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


def fermat(n):
    x = isqrt(n)
    y_2 = x * x - n
    y = isqrt(n)
    count = 0
    # 从根号n开始遍历找满足y**y = x * x - n的x和y
    while y * y != y_2:
        x = x + 1
        y_2 = x * x - n
        y = isqrt(y_2)
        count += 1
    p = x + y
    q = x - y
    return p, q


def decrypt(p, q, e, c, N):
    # 根据p,q求phi_n也即N的欧拉函数值
    phi_n = (p - 1) * (q - 1)
    # 求d
    d = mod_inverse(e, phi_n)  # 求欧拉值的模逆元
    plaintext = pow(c, d, N)
    return plaintext


if __name__ == "__main__":
    for i in [10, 14]:
        with open("费马方法/Frame{}".format(i), "rb") as file:
            nums = file.read()
            N = int(nums[0:256].strip(), 16)
            e = int(nums[256:512].strip(), 16)
            c = int(nums[512:768].strip(), 16)

            p, q = fermat(N)
            plaintext = decrypt(p, q, e, c, N)
            # print("plaintext:%x" % plaintext)
            print("%s:" % hex(plaintext)[18:26])
            print("%s" % long_to_bytes(plaintext)[-8:])
