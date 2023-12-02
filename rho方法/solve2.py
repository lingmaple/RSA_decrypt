from Crypto.Util.number import getPrime, isPrime
flag = 'BCNS{***************}'
nbits = 2048
gbits = 1000
g = getPrime(int(gbits))
while True:
    a = getPrime(int(nbits * 0.5) - gbits)
    p = 2 * g * a + 1
    if isPrime(p):
        break

while True:
    b = getPrime(int(nbits * 0.5) - gbits)
    q = 2 * g * b + 1
    if p != q and isPrime(q):
        break
N = p * q
e = 65537

def str2int(s):
    return int(s.encode('hex'), 16)

with open('pubkey.txt', 'w') as f:
    f.write(str(e) + '\n')
    f.write(str(N) + '\n')

plain = str2int(flag)

c = pow(plain, e, N)
with open('cipher.txt', 'w') as f:
    f.write(hex(c))