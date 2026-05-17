# Problem 228: https://projecteuler.net/problem=228
from math import isqrt


def divisors(n):
    ds = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    return ds


def phi(n):
    ans = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            ans -= ans // p
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        ans -= ans // n
    return ans


def solve():
    ds = set()
    for n in range(1864, 1910):
        ds.update(divisors(n))
    return sum(phi(d) for d in ds)


if __name__ == "__main__":
    print(solve())
