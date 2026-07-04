# Problem 359: https://projecteuler.net/problem=359

from sympy import divisors


N = 71_328_803_586_048
MOD = 100_000_000


def first_person(f):
    if f == 1:
        return 1
    return f * f // 2


def first_square(f):
    if f == 1:
        return 2
    if f % 2 == 0:
        return f + 1
    return f


def person(f, r):
    a = first_person(f)
    s = first_square(f)

    if r % 2 == 1:
        k = (r - 1) // 2
        return a + 2 * k * k + (2 * s - 1) * k

    k = r // 2
    return s * s - a + (k - 1) * (2 * s + 2 * k - 1)


def solve():
    return sum(person(f, N // f) for f in divisors(N)) % MOD


if __name__ == "__main__":
    print(solve())
