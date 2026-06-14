# Problem 308: https://projecteuler.net/problem=308

from sympy import prime, primerange


N = 10_001


def spf_table(n):
    spf = [0] * (n + 1)

    for p in primerange(2, n + 1):
        spf[p] = p
        for k in range(p * p, n + 1, p):
            if spf[k] == 0:
                spf[k] = p

    return spf


def divsum_tail(n, q):
    total = 0
    i = q

    while i <= n:
        v = n // i
        j = n // v
        total += v * (j - i + 1)
        i = j + 1

    return total


def candidate_cost(m, spf):
    if spf[m] == m:
        q = 1
        h = 1 + divsum_tail(m - 1, q)
        return 6 * m * (m - q) + 2 * m - 2 * q - 1 + 2 * h

    q = m // spf[m]
    h = 1 + divsum_tail(m - 1, q)
    return 6 * m * (m - q) + 3 * m - q - 2 + 2 * h


def solve():
    p = prime(N)
    spf = spf_table(p)
    total = 1
    primes = 0

    for m in range(2, p + 1):
        total += candidate_cost(m, spf) + 1
        if m < p and spf[m] == m:
            primes += m

    return total + primes


if __name__ == "__main__":
    print(solve())
