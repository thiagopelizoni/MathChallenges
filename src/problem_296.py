# Problem 296: https://projecteuler.net/problem=296

from sympy import factorint


N = 100_000


def floor_sum(n, a, m):
    ans = 0
    b = 0
    n += 1

    while True:
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m

        y = a * n + b
        if y < m:
            return ans

        n = y // m
        b = y % m
        a, m = m, a


def divs_mu(n):
    ds = [(1, 1)]
    for p in factorint(n):
        ds += [(d * p, -mu) for d, mu in ds]
    return ds


def coprime_count(ds, x):
    return sum(mu * (x // d) for d, mu in ds)


def coprime_floor_sum(ds, q, g, x):
    return sum(mu * floor_sum(x // d, g, q // d) for d, mu in ds)


def solve():
    total = 0

    for q in range(2, N // 3 + 1):
        m = N // q
        xhi = q // 2
        ds = divs_mu(q)
        nhi = coprime_count(ds, xhi)

        for g in range(2, 2 * m // 3 + 1):
            h = max(1, 2 * g - m)
            lo = (h * q + g - 1) // g
            if lo > xhi:
                continue

            a = coprime_floor_sum(ds, q, g, xhi)
            b = coprime_floor_sum(ds, q, g, lo - 1)
            c = nhi - coprime_count(ds, lo - 1)
            total += a - b - (h - 1) * c

    return total


if __name__ == "__main__":
    print(solve())
