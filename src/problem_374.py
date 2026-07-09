# Problem 374: https://projecteuler.net/problem=374

from math import isqrt


N = 10**14
MOD = 982451653


def block_position(n):
    k = (isqrt(8 * n + 9) - 3) // 2
    while (k + 1) * (k + 4) // 2 <= n:
        k += 1
    while k * (k + 3) // 2 > n:
        k -= 1
    return k, n - k * (k + 3) // 2


def sum_fm(n, mod):
    if n <= 0:
        return 0

    kmax, rem = block_position(n)
    inv2 = pow(2, -1, mod)
    ans = 1 % mod
    fact = 2 % mod
    harmonic = (inv2 + pow(3, -1, mod)) % mod

    for k in range(1, kmax):
        block = fact * ((k + 2) * harmonic + (k + 3) * inv2) % mod
        ans = (ans + k * block) % mod
        fact = fact * (k + 2) % mod
        harmonic = (harmonic + pow(k + 3, -1, mod)) % mod

    if kmax:
        if rem <= kmax:
            part = 0
            for t in range(kmax - rem + 2, kmax + 3):
                part = (part + pow(t, -1, mod)) % mod
            block = fact * (kmax + 2) * part % mod
        else:
            block = fact * ((kmax + 2) * harmonic + (kmax + 3) * inv2) % mod
        ans = (ans + kmax * block) % mod

    return ans


def solve():
    return sum_fm(N, MOD)


if __name__ == "__main__":
    print(solve())
