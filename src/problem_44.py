# Problem 44: https://projecteuler.net/problem=44
from math import isqrt

def pent(n):
    return n * (3 * n - 1) // 2

def is_pent(x):
    y = 24 * x + 1
    r = isqrt(y)
    return r * r == y and (r + 1) % 6 == 0

def solve():
    vals = []
    n = 1
    best = None

    while True:
        pk = pent(n)

        for pj in reversed(vals):
            d = pk - pj
            if best is not None and d >= best:
                break
            if is_pent(pk + pj) and is_pent(d):
                best = d
                return best

        vals.append(pk)
        n += 1

if __name__ == "__main__":
    print(solve())