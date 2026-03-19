# Problem 12: https://projecteuler.net/problem=12
from functools import lru_cache

@lru_cache(maxsize=None)
def tau(n):
    total = 1
    d = 2

    while d * d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            total *= e + 1
        d += 1

    if n > 1:
        total *= 2

    return total

def solve():
    n = 1
    while True:
        if n % 2 == 0:
            a = n // 2
            b = n + 1
        else:
            a = n
            b = (n + 1) // 2

        if tau(a) * tau(b) > 500:
            return n * (n + 1) // 2

        n += 1

if __name__ == "__main__":
    print(solve())