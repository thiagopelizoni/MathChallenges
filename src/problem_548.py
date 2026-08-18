# Problem 548: https://projecteuler.net/problem=548

from math import comb, log

from sympy import factorint, primerange


LIMIT = 10**16


def gozinta(exponents):
    length = sum(exponents)
    exact = [0] * (length + 1)

    for slots in range(1, length + 1):
        weak = 1
        for e in exponents:
            weak *= comb(e + slots - 1, e)
        exact[slots] = weak
        for used in range(1, slots):
            exact[slots] -= comb(slots, used) * exact[used]

    return sum(exact)


def solve():
    primes = list(primerange(2, 100))
    total = 1

    def search(pos, largest, least, exponents):
        nonlocal total
        power = 1

        for e in range(1, largest + 1):
            power *= primes[pos]
            next_least = least * power
            if next_least > LIMIT:
                break

            pattern = exponents + (e,)
            g = gozinta(pattern)
            if g <= LIMIT:
                factors = tuple(sorted(factorint(g).values(), reverse=True))
                if factors == pattern:
                    total += g

            search(pos + 1, e, next_least, pattern)

    search(0, int(log(LIMIT, 2)), 1, ())
    return total


if __name__ == "__main__":
    print(solve())
