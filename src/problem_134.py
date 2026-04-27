# Problem 134: https://projecteuler.net/problem=134

from sympy import primerange


def solve():
    primes = list(primerange(5, 1_000_100))
    total = 0

    for p1, p2 in zip(primes, primes[1:]):
        if p1 > 1_000_000:
            break

        m = 10 ** len(str(p1))
        k = (-p1 * pow(m, -1, p2)) % p2
        total += p1 + m * k

    return total


if __name__ == "__main__":
    print(solve())
