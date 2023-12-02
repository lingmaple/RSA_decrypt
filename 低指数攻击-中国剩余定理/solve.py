# -*- coding: utf-8 -*-

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def chinese_remainder(p, s):
    if len(p) != len(s):
        raise ValueError("长度不匹配")

    n = len(p)
    # 检查 b[i] 是否互质
    for i in range(n - 1):
        for j in range(i + 1, n):
            if extended_gcd(s[i], s[j])[0] != 1:
                raise ValueError("存在 b[i] 不互质")

    # 计算方程组的通解
    N = 1
    for i in range(n):
        N *= s[i]

    x = 0
    for i in range(n):
        Ni = N // s[i]
        gcd, xi, _ = extended_gcd(Ni, s[i])
        if gcd != 1:
            raise ValueError("存在 b[i] 不互质")

        x += p[i] * xi * Ni

    return x % N

n = []
c = []

for i in [3, 8, 12, 16, 20]:
    with open("低指数攻击-中国剩余定理/Frame{}".format(i), "rb") as file:
        nums = file.read()
        n.append(int(nums[0:256].strip(), 16))
        c.append(int(nums[512:768].strip(), 16))

print(chinese_remainder(c, n))

