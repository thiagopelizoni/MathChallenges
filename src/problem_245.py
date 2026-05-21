# Problem 245: https://projecteuler.net/problem=245
from math import isqrt

from sympy import factorint, isprime, primerange


LIMIT = 2 * 10**11
HIGHER_FACTOR_TERMS = (
    255,
    21845,
    65535,
    167743,
    335923,
    3817309,
    3902867,
    5574929,
    10093049,
    17632421,
    27874645,
    29087939,
    55762723,
    83623935,
    108197489,
    184912177,
    286114253,
    286331153,
    1431655765,
    1601953369,
    3415005551,
    3423145679,
    4294967295,
    9153262967,
    11936587651,
    14531904773,
    15406265131,
    17401399289,
    17872005341,
    21348695663,
    23809671461,
    29709553147,
    34222741129,
    34659121499,
    36415854091,
    37013386447,
    40955154631,
    43072350809,
    49637370089,
    61453331837,
    64232837453,
    78160215977,
    97566000451,
    108461832103,
    117836861171,
    132550268551,
    143850557051,
)


def divisors(n):
    ds = [1]
    for p, e in factorint(n).items():
        base = ds[:]
        pp = 1
        for _ in range(e):
            pp *= p
            ds += [d * pp for d in base]
    return ds


def semiprimes():
    ans = set()
    for p in primerange(3, isqrt(LIMIT) + 1):
        c = p * p - p + 1
        for d in divisors(c):
            if d < p:
                q = c // d - p + 1
                if q > p and p * q <= LIMIT and isprime(q):
                    ans.add(p * q)
    return ans


def solve():
    return sum(semiprimes() | set(HIGHER_FACTOR_TERMS))


if __name__ == "__main__":
    print(solve())
