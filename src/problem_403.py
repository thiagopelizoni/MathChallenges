# Problem 403: https://projecteuler.net/problem=403

from math import isqrt


N = 10**12
MOD = 10**8


def summatory_lattice_points(n):
    modulus = 3 * MOD
    limit = isqrt(n)

    t = n * (n + 1) // 2
    axes = (t * t + 5 * t + 6 * n) % modulus

    t = limit * (limit + 1) // 2
    diagonal = (4 * t * t + 5 * t + 6 * limit) % modulus

    off_diagonal = 0
    for x in range(1, limit + 1):
        q = n // x
        tx = x * (x + 1) // 2 % modulus
        tq = q * (q + 1) // 2 % modulus
        dy = (tq - tx) % modulus
        off_diagonal = (
            off_diagonal
            + tq * tq
            - tx * tx
            + (3 * x * x + 5) * dy
            + 6 * (q - x)
        ) % modulus

    correction = ((n - 1) ** 3 + 5 * (n - 1) + 6) % modulus
    numerator = (axes + diagonal + 2 * off_diagonal - correction) % modulus
    return (1 + limit + numerator // 3) % MOD


def solve():
    return summatory_lattice_points(N)


if __name__ == "__main__":
    print(solve())
