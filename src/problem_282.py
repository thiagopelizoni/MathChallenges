# Problem 282: https://projecteuler.net/problem=282

from functools import cache


MOD = 14**8
STABLE_HEIGHT = 20


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def crt_pair(a, m, b, n):
    return (a + m * ((b - a) * pow(m, -1, n) % n)) % (m * n)


def exact_tower_cap(h, cap):
    x = 2
    for _ in range(1, h):
        if x >= cap:
            return cap
        x = 2**x
    return min(x, cap)


@cache
def tetration_mod(h, mod):
    if mod == 1:
        return 0
    if h == 1:
        return 2 % mod

    ans = 0
    cur = 1
    for p, e in factor(mod):
        q = p**e
        if p == 2:
            exp = exact_tower_cap(h - 1, e)
            r = 0 if exp >= e else pow(2, exp, q)
        else:
            r = pow(2, tetration_mod(h - 1, (p - 1) * p ** (e - 1)), q)

        ans = crt_pair(ans, cur, r, q)
        cur *= q

    return ans


def solve():
    a4 = tetration_mod(7, MOD) - 3
    stable = tetration_mod(STABLE_HEIGHT, MOD) - 3
    return (1 + 3 + 7 + 61 + a4 + 2 * stable) % MOD


if __name__ == "__main__":
    print(solve())
