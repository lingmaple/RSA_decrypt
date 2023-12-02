# 扩展的欧几里得算法，求最大公约数和系数 x、y。
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


# 如果方程组无解，返回 -1。
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


# 示例
# x = 2(mod 5)
# x = 3(mod 7)
# x = 1(mod 3)
# 答案
# x = 52
# p = [2, 3, 1]
# s = [5, 7, 3]
# print(chinese_remainder(p, s))
p = []
e = []
s = []
for i in [3, 8, 12, 16, 20]:
    with open("Frame{}".format(i), "rb") as file:
        nums = file.read()
        p.append(int(nums[0:256].strip(), 16))
        # p.append(int(nums[0:256].strip(), 16) ** int(nums[256:512].strip(), 16))
        # e.append(int(nums[256:512].strip(),16))
        s.append(int(nums[512:768].strip(), 16))

print(chinese_remainder(p, s))
