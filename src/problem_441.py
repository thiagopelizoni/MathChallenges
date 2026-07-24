# Problem 441: https://projecteuler.net/problem=441

from array import array

from sympy import sieve


N = 10_000_000


def solve():
    half = N // 2
    mu = array("b", sieve.mobiusrange(1, half + 1))
    h = array("d", [0.0]) * (N + 1)
    h2 = array("d", [0.0]) * (N + 1)
    tri = array("d", [0.0]) * (N + 1)

    s = s2 = c = c2 = 0.0
    for k in range(1, N + 1):
        inv = 1.0 / k
        y = inv - c
        t = s + y
        c = (t - s) - y
        s = t
        h[k] = s

        y = inv * inv - c2
        t = s2 + y
        c2 = (t - s2) - y
        s2 = t
        h2[k] = s2

    s = c = 0.0
    for m in range(1, N):
        k = (m - 1) // 2
        delta = 0.0
        if k:
            delta = (
                -h[k] / (m - k)
                + 1.0 / m
                + (h[k] - 1 + h[m - 1] - h[m - k]) / (m + 1)
            )
        if m % 2 == 0:
            k = m // 2
            delta += h[k] / (k + 1)
        y = delta - c
        t = s + y
        c = (t - s) - y
        s = t
        tri[m + 1] = s

    def pairs(k):
        return (h[k] * h[k] - h2[k]) / 2

    def harmonic_sum(k):
        return (k + 1) * h[k] - k

    def preceding_sum(k):
        return 0.0 if k <= 1 else k * h[k - 1] - (k - 1)

    totals = [0.0] * 5
    errors = [0.0] * 5

    def add(i, value):
        y = value - errors[i]
        t = totals[i] + y
        errors[i] = (t - totals[i]) - y
        totals[i] = t

    for d in range(1, half + 1):
        md = mu[d - 1]
        if not md:
            continue
        inv = 1.0 / d
        inv2 = inv * inv
        k = half // d
        m = N // d
        a = N // (2 * d) + 1

        add(0, md * k * inv)
        add(1, md * pairs(k) * inv2)
        add(2, md * (m * (h[m] - h[a - 1]) - (m - a + 1)) * inv)
        add(
            3,
            md
            * (
                (N + 1) * (pairs(m) - pairs(a - 1)) * inv2
                - (preceding_sum(m) - preceding_sum(a - 1)) * inv
            ),
        )
        add(4, md * (harmonic_sum(m - a) * inv - N * tri[m] * inv2))

    return f"{sum(totals) - 1:.4f}"


if __name__ == "__main__":
    print(solve())
