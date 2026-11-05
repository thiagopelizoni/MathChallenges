# Problem 707: https://projecteuler.net/problem=707

from sympy import GF
from sympy.polys.rings import ring


def path(n, q):
    if n == 0:
        return q.ring.one, q.ring.zero
    x = q.ring.gens[0]
    a, b = path(n // 2, q)
    a = (a * a).rem(q)
    b = (b * b).rem(q)
    if n % 2:
        return (x * a).rem(q), a + b
    return a + b, (x * b).rem(q)


def solve(w=199, n=199):
    mod = 1_000_000_007
    R, x = ring("x", GF(2))
    a, b = R.one, x + 1
    for _ in range(2, w + 1):
        a, b = b, (x + 1) * b + a
    factors = b.factor_list()[1]

    total = 0
    h, following = 1, 1
    for _ in range(n):
        u, power = h + 1, 1
        while u % 2 == 0:
            u //= 2
            power *= 2
        nullity = 0
        for q, e in factors:
            if q == x:
                nullity += min(e, power - 1)
            elif not path(u - 1, q)[0]:
                nullity += q.degree() * min(e, 2 * power)
        total = (total + pow(2, w * h - nullity, mod)) % mod
        h, following = following, h + following
    return total


if __name__ == "__main__":
    print(solve())
