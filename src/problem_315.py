# Problem 315: https://projecteuler.net/problem=315

from sympy import primerange


A = 10_000_000
B = 20_000_000
SEG = (
    frozenset("abcefg"),
    frozenset("cf"),
    frozenset("acdeg"),
    frozenset("acdfg"),
    frozenset("bcdf"),
    frozenset("abdfg"),
    frozenset("abdefg"),
    frozenset("abcf"),
    frozenset("abcdefg"),
    frozenset("abcdfg"),
)


def digits(n):
    return [int(c) for c in reversed(str(n))]


def digit_sum(n):
    return sum(int(c) for c in str(n))


def lit(n):
    return sum(len(SEG[d]) for d in digits(n))


def change(a, b):
    da = digits(a)
    db = digits(b)
    total = 0

    for i in range(max(len(da), len(db))):
        x = SEG[da[i]] if i < len(da) else frozenset()
        y = SEG[db[i]] if i < len(db) else frozenset()
        total += len(x - y) + len(y - x)

    return total


def chain(n):
    out = [n]

    while n >= 10:
        n = digit_sum(n)
        out.append(n)

    return out


def sam(n):
    return 2 * sum(lit(k) for k in chain(n))


def max_clock(n):
    c = chain(n)
    return lit(c[0]) + sum(change(a, b) for a, b in zip(c, c[1:])) + lit(c[-1])


def solve():
    return sum(sam(p) - max_clock(p) for p in primerange(A, B))


if __name__ == "__main__":
    print(solve())
