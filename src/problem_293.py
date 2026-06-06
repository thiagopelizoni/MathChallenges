# Problem 293: https://projecteuler.net/problem=293

from sympy import isprime, primerange


LIM = 10**9
primes = list(primerange(2, 30))


def admissible(i, n, xs):
    if i == len(primes):
        return

    n *= primes[i]
    while n < LIM:
        xs.append(n)
        admissible(i + 1, n, xs)
        n *= primes[i]


def fortunate(n):
    m = 3
    while not isprime(n + m):
        m += 2
    return m


def solve():
    xs = []
    admissible(0, 1, xs)
    return sum({fortunate(n) for n in xs})


if __name__ == "__main__":
    print(solve())
