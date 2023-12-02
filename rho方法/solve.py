# -*- coding: utf-8 -*-
import random

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


def rho(n):
    x_nPlus1 = random.randint(1, n - 1)
    x_n = x_nPlus1
    temp = 2
    i = 0
    a = 1  # 此时a按照样例选取为1
    while True:
        i += 1
        x_nPlus1 = (x_nPlus1 * x_nPlus1 + a) % n  # f(x_n)函数
        d = gcd(abs(x_nPlus1 - x_n), n)
        if n > d > 1:
            return d
        if x_nPlus1 == x_n:
            a += 1
        if i == temp:
            x_n = x_nPlus1
            temp <<= 1


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
            
            print(N)
            # p = rho(N)
            q = N // p
            print("p*q==N? {}".format(p * q == N))
            plaintext = decrypt(p, q, e, c, N)
            print("%x" % plaintext)
