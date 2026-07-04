# Problem 358: https://projecteuler.net/problem=358

from sympy import isprime, n_order


LEFT_PREFIX = 137
NEXT_PREFIX = 138
PREFIX_SCALE = 10**11
RIGHT_SUFFIX = 56_789
SUFFIX_MOD = 100_000


def candidate_prime():
    lo = PREFIX_SCALE // NEXT_PREFIX + 1
    hi = PREFIX_SCALE // LEFT_PREFIX
    residue = (-pow(RIGHT_SUFFIX, -1, SUFFIX_MOD)) % SUFFIX_MOD

    p = lo + (residue - lo) % SUFFIX_MOD
    while p <= hi:
        if isprime(p) and n_order(10, p) == p - 1:
            return p
        p += SUFFIX_MOD

    raise RuntimeError("no cyclic-number prime found")


def solve():
    p = candidate_prime()
    return 9 * (p - 1) // 2


if __name__ == "__main__":
    print(solve())
