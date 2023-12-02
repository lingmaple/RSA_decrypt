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


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def main():
    with open("共模攻击/Frame0", "rb") as file:
        nums = file.read()
        N = int(nums[0:256].strip(), 16)
        e1 = int(nums[256:512].strip(), 16)
        c1 = int(nums[256:512].strip(), 16)

    with open("共模攻击/Frame4", "rb") as file:
        nums = file.read()
        N = int(nums[0:256].strip(), 16)
        e2 = int(nums[256:512].strip(), 16)
        c2 = int(nums[256:512].strip(), 16)

    s = egcd(e1, e2)
    s1, s2 = s[1], s[2]

    if s1 < 0:
        s1 = -s1
        c1 = mod_inverse(c1, N)
    elif s2 < 0:
        s2 = -s2
        c2 = mod_inverse(c2, N)

    m = pow(c1, s1, N) * pow(c2, s2, N) % N
    print(N)
    print(m)
    print("%x" % m)


if __name__ == "__main__":
    main()
