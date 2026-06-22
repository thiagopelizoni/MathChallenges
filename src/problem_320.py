# Problem 320: https://projecteuler.net/problem=320

from sympy import primerange


POWER = 1_234_567_890
LIM = 1_000_000
MOD = 10**18


def smallest_prime_factors(lim):
    spf = [0] * (lim + 1)

    for p in primerange(2, lim + 1):
        spf[p] = p
        for n in range(p * p, lim + 1, p):
            if spf[n] == 0:
                spf[n] = p

    return spf


def digit_sum(n, p):
    total = 0
    while n:
        total += n % p
        n //= p
    return total


def inv_legendre(p, e):
    target = (p - 1) * e
    m = target // p

    while p * m - digit_sum(m, p) < target:
        m += 1

    return p * m


def solve():
    spf = smallest_prime_factors(LIM)
    exps = [0] * (LIM + 1)
    best = 0
    ans = 0

    for i in range(2, LIM + 1):
        n = i
        while n > 1:
            p = spf[n]
            a = 0

            while n % p == 0:
                a += 1
                n //= p

            exps[p] += a
            cand = inv_legendre(p, exps[p] * POWER)
            if cand > best:
                best = cand

        if i >= 10:
            ans = (ans + best) % MOD

    return ans


if __name__ == "__main__":
    print(solve())
