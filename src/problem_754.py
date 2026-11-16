# Problem 754: https://projecteuler.net/problem=754


def solve(n=10**8, mod=1_000_000_007):
    values = []
    l = 1
    while l <= n:
        q = n // l
        values.append(q)
        l = n // q + 1
    values.reverse()

    fact = {0: 1}
    invfact = {0: 1}
    products = {}
    f = b = 1
    start = 1
    for m in values:
        for k in range(start, m + 1):
            b = b * f % mod
            f = f * k % mod
        fact[m] = f
        invfact[m] = pow(f, -1, mod)
        products[m] = b
        start = m + 1

    g = {}
    counts = {}
    for m in values:
        denominator = 1
        pairs = m * (m - 1) // 2
        l = 2
        while l <= m // 2:
            q = m // l
            r = m // q
            base = fact[r] * invfact[l - 1] % mod
            denominator = denominator * pow(base, counts[q], mod) % mod
            denominator = denominator * pow(g[q], r - l + 1, mod) % mod
            pairs -= (r - l + 1) * counts[q]
            l = r + 1
        counts[m] = pairs
        g[m] = products[m] * pow(denominator, -1, mod) % mod
    return g[n]


if __name__ == "__main__":
    print(solve())
