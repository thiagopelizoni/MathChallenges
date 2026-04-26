# Problem 130: https://projecteuler.net/problem=130

from itertools import count

from sympy import isprime


def repunit_order(n):
    r = 1 % n
    k = 1
    while r:
        r = (10 * r + 1) % n
        k += 1
    return k


def solve():
    vals = []

    for n in count(3, 2):
        if n % 5 and not isprime(n):
            a = repunit_order(n)
            if (n - 1) % a == 0:
                vals.append(n)
                if len(vals) == 25:
                    return sum(vals)


if __name__ == "__main__":
    print(solve())
