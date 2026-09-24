# Problem 633: https://projecteuler.net/problem=633

from mpmath import mp


def solve():
    k = 7
    a = [0]
    for j in range(1, k + 1):
        s = mp.nsum(
            lambda m: mp.binomial(m - 1, j - 1) * mp.primezeta(2 * m),
            [j, mp.inf],
        )
        a.append((-1) ** (j + 1) * s / j)

    coefficients = mp.taylor(lambda z: mp.exp(mp.polyval(a[::-1], z)), 0, k)
    c = coefficients[k] / mp.zeta(2)
    return mp.nstr(c, 5, strip_zeros=False, min_fixed=0, max_fixed=0)


if __name__ == "__main__":
    print(solve())
