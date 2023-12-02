def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mapx(x):
    x = (pow(x, n - 1, n) + 3) % n  # pow(x,n-1,n)是为了减小数值，加速运算，
    return x


def pollard_rho(x1, x2):
    while True:
        x1 = mapx(x1)
        x2 = mapx(mapx(x2))
        p = gcd(x1 - x2, n)
        if p == n:
            print("fail")
            return
        elif p != 1:
            print("p: " + str(p))
            print("q: " + str(n / p))
            break


def main():
    pollard_rho(1, 1)
    return


n = 839475
main()
