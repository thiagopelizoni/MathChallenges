# Problem 699: https://projecteuler.net/problem=699

from fractions import Fraction
from math import gcd, lcm

from sympy import divisor_sigma, divisors, factorint, nextprime


def solve(limit=10**14):
    total = 0
    q = 3
    while q <= limit:
        total += q
        s = int(divisor_sigma(q))
        bound = limit // q
        upper = Fraction(1)
        product = 1
        p = 2
        while product * p <= bound:
            product *= p
            upper *= Fraction(p, p - 1)
            p = int(nextprime(p))
            if p == 3:
                p = int(nextprime(p))

        def search(a, b, n, need, lo):
            if a < b or gcd(b, 3 * n) != 1:
                return
            if a == b:
                if need == 1:
                    yield n
                return
            remaining = bound // n
            required = lcm(b, need)
            if required > remaining:
                return
            if required > 1:
                factors = factorint(required)
                p = int(max(factors))
                if p < lo or p == 3 or n % p == 0:
                    return
                choices = [(p, p ** int(factors[p]), lo)]
            else:
                choices = []
                p = int(nextprime(lo - 1))
                while p <= remaining:
                    k = 0
                    power = 1
                    while power * p <= remaining:
                        power *= p
                        k += 1
                    if a * (p - 1) ** k >= b * p**k:
                        break
                    if p != 3 and n % p != 0:
                        choices.append((p, p, p + 1))
                    p = int(nextprime(p))
            for p, minimum, next_lo in choices:
                rest = need
                while rest % p == 0:
                    rest //= p
                power = p
                while power <= remaining:
                    if power >= minimum:
                        num = a * power
                        den = b * int(divisor_sigma(power))
                        g = gcd(num, den)
                        yield from search(num // g, den // g, n * power, rest, next_lo)
                    power *= p

        for d in divisors(s):
            last = upper.numerator * d // upper.denominator
            if bound // d <= last - d:
                for m in range(d, bound + 1, d):
                    if m == 1 or m % 3 == 0 or gcd(m, s) != d:
                        continue
                    sigma = int(divisor_sigma(m))
                    if sigma % (m // d) == 0 and sigma % q != 0:
                        total += q * m
            else:
                for c in range(d + 1, last + 1):
                    if c % q == 0:
                        continue
                    g = gcd(c, d)
                    for m in search(c // g, d // g, 1, d, 2):
                        if gcd(m, s) == d:
                            total += q * m
        q *= 3
    return total


if __name__ == "__main__":
    print(solve())
