# Problem 193: https://projecteuler.net/problem=193
from array import array
from math import isqrt


def mobius(n):
    mu = array("b", [0]) * (n + 1)
    composite = bytearray(n + 1)
    primes = []
    mu[1] = 1

    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1

        for p in primes:
            m = i * p
            if m > n:
                break
            composite[m] = 1
            if i % p == 0:
                break
            mu[m] = -mu[i]

    return mu


def solve():
    limit = (1 << 50) - 1
    root = isqrt(limit)
    mu = mobius(root)
    return sum(mu[d] * (limit // (d * d)) for d in range(1, root + 1))


if __name__ == "__main__":
    print(solve())
