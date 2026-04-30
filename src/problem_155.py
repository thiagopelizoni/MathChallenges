# Problem 155: https://projecteuler.net/problem=155

from math import gcd


def add(x, y):
    a, b = x
    c, d = y
    p = a * d + b * c
    q = b * d
    g = gcd(p, q)
    return p // g, q // g


def series(x, y):
    a, b = x
    c, d = y
    p = a * c
    q = a * d + b * c
    g = gcd(p, q)
    return p // g, q // g


def solve():
    n = 18
    exact = [set() for _ in range(n + 1)]
    values = {(1, 1)}
    exact[1].add((1, 1))

    for k in range(2, n + 1):
        cur = set()
        for a in range(1, k // 2 + 1):
            for x in exact[a]:
                for y in exact[k - a]:
                    cur.add(add(x, y))
                    cur.add(series(x, y))
        exact[k] = cur
        values.update(cur)

    return len(values)


if __name__ == "__main__":
    print(solve())
