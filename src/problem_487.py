# Problem 487: https://projecteuler.net/problem=487
from sympy import primerange

K = 10000
N = 10**12
LO = 2 * 10**9
HI = LO + 2000


def power_sum_mod(m, x, p, ifac):
    d = m + 1
    ys = [0] * (d + 1)
    for j in range(1, d + 1):
        ys[j] = (ys[j - 1] + pow(j, m, p)) % p
    if x <= d:
        return ys[x]
    num = den = 0
    for j in range(d + 1):
        w = (1 if (d - j) % 2 == 0 else -1) * ifac[j] % p * ifac[d - j] % p
        t = w * pow((x - j) % p, -1, p) % p
        num = (num + ys[j] * t) % p
        den = (den + t) % p
    return num * pow(den, -1, p) % p


def S_mod(p):
    r = N % p
    fac = [1] * (K + 3)
    for i in range(1, K + 3):
        fac[i] = fac[i - 1] * i % p
    ifac = [1] * (K + 3)
    ifac[K + 2] = pow(fac[K + 2], -1, p)
    for i in range(K + 2, 0, -1):
        ifac[i - 1] = ifac[i] * i % p
    fk = power_sum_mod(K, r, p, ifac)
    fk1 = power_sum_mod(K + 1, r, p, ifac)
    return ((N + 1) % p * fk - fk1) % p


def solve():
    return sum(S_mod(p) for p in primerange(LO, HI + 1))


if __name__ == "__main__":
    print(solve())
