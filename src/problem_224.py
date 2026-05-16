# Problem 224: https://projecteuler.net/problem=224
from array import array
from math import isqrt


LIMIT = 75_000_000


def ceil_sqrt(n):
    r = isqrt(n)
    return r if r * r == n else r + 1


def spf_upto(n):
    spf = array("I", range(n + 1))
    for i in range(4, n + 1, 2):
        spf[i] = 2
    for p in range(3, isqrt(n) + 1, 2):
        if spf[p] == p:
            for q in range(p * p, n + 1, 2 * p):
                if spf[q] == q:
                    spf[q] = p
    return spf


def factor(n, spf):
    fs = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        fs.append((p, e))
    return fs


def sqrt_minus_one_prime(p):
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    return pow(z, (p - 1) // 4, p)


def roots_prime_power(p, e):
    q = p**e
    if p % 4 == 3:
        return [], q

    r = sqrt_minus_one_prime(p)
    mod = p
    for _ in range(1, e):
        t = (-((r * r + 1) // mod) * pow(2 * r, -1, p)) % p
        r += t * mod
        mod *= p
    return [r, q - r], q


def extend_roots(roots, mod, rs, q):
    inv = pow(mod, -1, q)
    out = []
    for r in roots:
        for s in rs:
            out.append((r + mod * (((s - r) * inv) % q)) % (mod * q))
    return out, mod * q


def roots_from_factors(fs):
    roots = [0]
    mod = 1
    for p, e in fs:
        rs, q = roots_prime_power(p, e)
        if not rs:
            return [], 1
        roots, mod = extend_roots(roots, mod, rs, q)
    return roots, mod


def upper_a(u):
    r = isqrt(u * u + 4 * LIMIT * u - 4)
    a = (r - u) // 2
    while a * a + u * a + 1 > LIMIT * u:
        a -= 1
    while (a + 1) * (a + 1) + u * (a + 1) + 1 <= LIMIT * u:
        a += 1
    return a


def solve():
    umax = 0
    while True:
        u = umax + 2 if umax else 1
        a = u + ceil_sqrt(2 * u * u - 1)
        if 3 * a + u > LIMIT:
            break
        umax = u

    spf = spf_upto(umax)
    total = 0

    for u in range(1, umax + 1, 2):
        lo = u + ceil_sqrt(2 * u * u - 1)
        if lo & 1:
            lo += 1
        hi = upper_a(u)
        if hi & 1:
            hi -= 1
        if lo > hi:
            continue

        roots, mod = roots_from_factors(factor(u, spf))
        step = 2 * mod
        for r in roots:
            first = r if r % 2 == 0 else r + mod
            if first == 0:
                first = step
            if first < lo:
                first += ((lo - first + step - 1) // step) * step
            if first <= hi:
                total += (hi - first) // step + 1

    return total


if __name__ == "__main__":
    print(solve())
