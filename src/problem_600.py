# Problem 600: https://projecteuler.net/problem=600

from math import comb


def solve(n=55106):
    total = 0
    reflected = 0
    for t in range((n - 6) // 3 + 1):
        m = (n - 3 * t) // 2
        weight = 1 if t == 0 else 2
        total += weight * comb(m, 3)
        k = (m - 1) // 2
        reflected += weight * k * (m - k - 1)

    total += 2 * (n // 6) + 2 * comb(n // 3, 2) + comb(n // 2, 3)
    m = n // 2
    k = (m - 1) // 2
    total += 3 * reflected + 3 * k * (m - k - 1)
    return total // 12


if __name__ == "__main__":
    print(solve())
