# Problem 692: https://projecteuler.net/problem=692
from functools import lru_cache

N = 23416728348467685

fib = [1, 2]
while fib[-1] <= N:
    fib.append(fib[-1] + fib[-2])


@lru_cache(maxsize=None)
def G(n):
    if n == 0:
        return 0
    f = max(x for x in fib if x <= n)
    return G(f - 1) + f + G(n - f)


def solve():
    return G(N)


if __name__ == "__main__":
    print(solve())
